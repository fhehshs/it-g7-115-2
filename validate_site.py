#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""驗證課程網站 content/chXX.py 結構。用法：python validate_site.py <site_dir>"""
import sys, os, re, importlib, glob

def main(site):
    sys.path.insert(0, site)
    errors, warns = [], []
    files = sorted(glob.glob(os.path.join(site, 'content', 'ch[0-9][0-9].py')))
    if not files:
        errors.append('找不到 content/chXX.py')
    for f in files:
        name = os.path.splitext(os.path.basename(f))[0]
        try:
            m = importlib.import_module(f'content.{name}')
        except Exception as e:
            errors.append(f'{name}: import 失敗 → {e}'); continue
        slides = getattr(m, 'SLIDES', None)
        quizzes = getattr(m, 'QUIZZES', {})
        chapters = getattr(m, 'CHAPTERS', [])
        if not slides:
            errors.append(f'{name}: 缺 SLIDES'); continue
        ids = [s.get('id') for s in slides]
        if ids != list(range(1, len(ids) + 1)):
            errors.append(f'{name}: SLIDES id 未從 1 連號: {ids[:8]}...')
        for s in slides:
            if not s.get('title') or not s.get('html'):
                errors.append(f"{name}: slide {s.get('id')} 缺 title/html")
            for mm in re.finditer(r'<[0-9]', s.get('html', '')):
                warns.append(f"{name}: slide {s.get('id')} 內含未跳脫的 '<數字'（改用 &lt;）")
            qk = s.get('quiz')
            if qk and qk not in quizzes:
                errors.append(f"{name}: slide {s.get('id')} quiz key '{qk}' 不在 QUIZZES")
        for qk, qv in quizzes.items():
            for i, q in enumerate(qv.get('questions', [])):
                opts = q.get('options', [])
                if not (isinstance(q.get('answer'), int) and 0 <= q['answer'] < len(opts)):
                    errors.append(f'{name}: {qk} 第{i+1}題 answer 超出選項範圍')
                if not q.get('explain'):
                    warns.append(f'{name}: {qk} 第{i+1}題缺 explain')
        for c in chapters:
            if not (1 <= c.get('start', 0) <= len(slides)):
                errors.append(f"{name}: CHAPTERS '{c.get('name')}' start 超出範圍")
        print(f"✔ {name}: {len(slides)} slides, {sum(len(v['questions']) for v in quizzes.values())} questions")
    print()
    for w in warns: print('⚠', w)
    for e in errors: print('✘', e)
    print('\n結果：', '通過 ✅' if not errors else f'{len(errors)} 個錯誤 ❌')
    return 1 if errors else 0

if __name__ == '__main__':
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else '.'))
