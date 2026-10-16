#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""把 Flask 課程網站匯出成靜態網頁（docs/），供 GitHub Pages 使用。
投影片與測驗資料直接內嵌在各章 HTML，因此直接雙擊 docs/index.html 也能離線瀏覽。
用法：python make_static.py   （之後內容有更新，重跑一次再 push 即可）"""
import json, os, re, shutil
from app import app, load_ch, apply_enhancements, N_CHAPTERS

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, 'docs')

def write(name, html):
    with open(os.path.join(OUT, name), 'w', encoding='utf-8') as f:
        f.write(html)

def main():
    shutil.rmtree(OUT, ignore_errors=True)
    os.makedirs(os.path.join(OUT, 'data'), exist_ok=True)
    client = app.test_client()

    static_src = os.path.join(ROOT, 'static')
    if os.path.isdir(static_src):
        shutil.copytree(static_src, os.path.join(OUT, 'static'),
                        ignore=shutil.ignore_patterns('.DS_Store', 'Thumbs.db'))

    # 首頁
    html = client.get('/').get_data(as_text=True)
    html = re.sub(r'href="/ch/\$\{ch\.n\}"', 'href="ch${ch.n}.html"', html)
    html = html.replace('href="/rubric"', 'href="rubric.html"')
    write('index.html', html)

    # 評量規準
    html = client.get('/rubric').get_data(as_text=True)
    write('rubric.html', html.replace('href="/"', 'href="index.html"'))

    # 各章頁面：資料內嵌（window.__SLIDES__ / __QUIZZES__），另存一份 JSON
    for n in range(1, N_CHAPTERS + 1):
        ch = load_ch(n)
        slides = apply_enhancements(ch.SLIDES, n)
        for s in slides:  # 播放器會讀這幾個欄位，補齊預設值
            s.setdefault('bg', 'white')
            s.setdefault('quiz', None)
            s.setdefault('chart', None)
            s.setdefault('video', None)
        slides_js = json.dumps(slides, ensure_ascii=False).replace('</', '<\\/')
        quizzes_js = json.dumps(ch.QUIZZES, ensure_ascii=False).replace('</', '<\\/')

        html = client.get(f'/ch/{n}').get_data(as_text=True)
        html = html.replace(f"fetch('/api/slides/{n}')", 'Promise.resolve({json:()=>window.__SLIDES__})')
        html = html.replace(f"fetch('/api/quizzes/{n}')", 'Promise.resolve({json:()=>window.__QUIZZES__})')
        html = html.replace('href="/"', 'href="index.html"')
        html = html.replace('<body>', f'<body>\n<script>window.__SLIDES__={slides_js};'
                                      f'window.__QUIZZES__={quizzes_js};</script>', 1)
        assert '/api/' not in html, f'ch{n} 仍有未轉換的 /api/ 路徑'
        write(f'ch{n}.html', html)
        json.dump(slides, open(os.path.join(OUT, f'data/slides-{n}.json'), 'w', encoding='utf-8'),
                  ensure_ascii=False)
        json.dump(ch.QUIZZES, open(os.path.join(OUT, f'data/quizzes-{n}.json'), 'w', encoding='utf-8'),
                  ensure_ascii=False)

    open(os.path.join(OUT, '.nojekyll'), 'w').close()
    print(f'✅ 靜態網站已輸出到 docs/（{len(os.listdir(OUT))} 個項目）')

if __name__ == '__main__':
    main()
