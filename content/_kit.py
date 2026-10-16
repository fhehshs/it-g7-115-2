# -*- coding: utf-8 -*-
"""各章共用的 HTML 片段（全部輸出行內 style，與第一學期版型一致）。
白底投影片（bg='white'）用深色字；navy / teal / purple 底用淺色字。"""

PALETTE = {
    'blue':   ('#eff6ff', '#1e40af'),
    'green':  ('#f0fdf4', '#166534'),
    'yellow': ('#fefce8', '#854d0e'),
    'purple': ('#f5f3ff', '#5b21b6'),
    'red':    ('#fef2f2', '#991b1b'),
    'teal':   ('#f0fdfa', '#115e59'),
    'orange': ('#fff7ed', '#9a3412'),
    'gray':   ('#f8fafc', '#334155'),
}
ACCENT = {'blue': '#2563eb', 'green': '#16a34a', 'yellow': '#f59e0b', 'purple': '#7c3aed',
          'red': '#dc2626', 'teal': '#0d9488', 'orange': '#ea580c', 'gray': '#64748b'}


def title(text):
    return f"<h2 class='slide-title'>{text}</h2>\n"


def lead(text, color='teal'):
    """頁首定義框：灰底＋左側色條"""
    return (f"<div style='background:#f1f5f9;border-radius:10px;padding:12px 16px;margin-bottom:14px;"
            f"border-left:4px solid {ACCENT[color]};'>"
            f"<p style='margin:0;color:#0f172a;font-size:.93rem;line-height:1.7;'>{text}</p></div>\n")


def card(color, head, body, icon='', center=False):
    bg, fg = PALETTE[color]
    align = 'text-align:center;' if center else ''
    ic = f"<div style='font-size:1.8rem;'>{icon}</div>" if icon else ''
    return (f"<div style='background:{bg};padding:14px;border-radius:10px;{align}'>{ic}"
            f"<strong style='color:{fg};font-size:.9rem;'>{head}</strong>"
            f"<div style='font-size:.8rem;color:#475569;margin-top:6px;line-height:1.7;'>{body}</div></div>")


def grid(cols, *cards, gap=10):
    return (f"<div style='display:grid;grid-template-columns:repeat({cols},1fr);gap:{gap}px;margin-bottom:12px;'>"
            + ''.join(cards) + "</div>\n")


def note(text, color='blue', icon='💬'):
    """頁尾提示框"""
    bg, _ = PALETTE[color]
    return (f"<div style='background:{bg};padding:11px 16px;border-radius:8px;border-left:4px solid {ACCENT[color]};'>"
            f"<p style='color:#374151;font-size:.88rem;margin:0;line-height:1.7;'>{icon} {text}</p></div>\n")


def table(headers, rows, widths=None):
    ths = ''.join(
        f"<th style='padding:9px 12px;text-align:left;font-size:.8rem;{'width:' + widths[i] + ';' if widths else ''}'>{h}</th>"
        for i, h in enumerate(headers))
    trs = ''
    for i, r in enumerate(rows):
        bg = '#f8fafc' if i % 2 else '#fff'
        tds = ''.join(f"<td style='padding:8px 12px;border-top:1px solid #e2e8f0;font-size:.8rem;color:#334155;"
                      f"vertical-align:top;line-height:1.6;'>{c}</td>" for c in r)
        trs += f"<tr style='background:{bg};'>{tds}</tr>"
    return (f"<table style='width:100%;border-collapse:collapse;border-radius:10px;overflow:hidden;"
            f"border:1px solid #e2e8f0;margin-bottom:12px;'><tr style='background:#1E3A5F;color:#fff;'>{ths}</tr>{trs}</table>\n")


def steps(items, color='blue'):
    """編號步驟清單（直向）"""
    bg, fg = PALETTE[color]
    out = "<div style='display:flex;flex-direction:column;gap:8px;margin-bottom:12px;'>"
    for i, (head, body) in enumerate(items, 1):
        out += (f"<div style='display:flex;gap:12px;align-items:flex-start;background:{bg};border-radius:10px;padding:10px 14px;'>"
                f"<div style='width:28px;height:28px;border-radius:50%;background:{ACCENT[color]};color:#fff;display:flex;"
                f"align-items:center;justify-content:center;font-weight:700;font-size:.85rem;flex-shrink:0;'>{i}</div>"
                f"<div><strong style='color:{fg};font-size:.88rem;'>{head}</strong>"
                f"<div style='font-size:.8rem;color:#475569;margin-top:3px;line-height:1.6;'>{body}</div></div></div>")
    return out + "</div>\n"


def video_slot(slide_id):
    return f"<div id='video-section-{slide_id}' class='video-section'></div>\n"


def yt(query, title, desc):
    """YouTube 搜尋按鈕（不綁定特定影片 ID，避免影片下架失效）"""
    return {'query': query, 'title': title, 'desc': desc}


def cover(emoji, title_text, en, tags, week):
    tag_html = ''.join(f"<span style='background:rgba(255,255,255,0.15);color:#e0f2fe;padding:8px 18px;border-radius:20px;'>{t}</span>"
                       for t in tags)
    return f"""
<div style='text-align:center;padding:24px 20px;'>
  <div style='font-size:66px;margin-bottom:14px;'>{emoji}</div>
  <h1 style='font-size:2.6rem;font-weight:900;color:#fff;margin-bottom:10px;'>{title_text}</h1>
  <h2 style='font-size:1.25rem;font-weight:400;color:#93c5fd;margin-bottom:24px;'>{en}</h2>
  <div style='display:flex;justify-content:center;gap:12px;flex-wrap:wrap;margin-bottom:22px;'>{tag_html}</div>
  <p style='color:#bfdbfe;font-size:1.05rem;'>七年級第二學期 ｜ {week}</p>
</div>
"""


def quiz_cover(title_text, sub):
    return f"""
<div style='text-align:center;padding:44px 20px;'>
  <div style='font-size:54px;margin-bottom:16px;'>📝</div>
  <h1 style='font-size:2rem;color:#fff;margin-bottom:10px;'>{title_text}</h1>
  <p style='color:#e9d5ff;font-size:1rem;'>{sub}</p>
  <p style='color:#c4b5fd;font-size:.85rem;margin-top:18px;'>按「下一頁 →」開始作答</p>
</div>
"""


def dark_section(emoji, heading, sub, points):
    """teal 底的轉場／重點頁"""
    pts = ''.join(f"<div style='background:rgba(255,255,255,.12);border-radius:10px;padding:12px 14px;'>"
                  f"<strong style='color:#fff;font-size:.9rem;'>{h}</strong>"
                  f"<p style='color:#ccfbf1;font-size:.8rem;margin-top:5px;line-height:1.7;'>{b}</p></div>" for h, b in points)
    return f"""
<div style='text-align:center;padding:12px 10px 4px;'>
  <div style='font-size:48px;margin-bottom:8px;'>{emoji}</div>
  <h2 style='font-size:1.6rem;font-weight:800;color:#fff;margin-bottom:6px;'>{heading}</h2>
  <p style='color:#ccfbf1;font-size:.95rem;margin-bottom:16px;'>{sub}</p>
</div>
<div style='display:grid;grid-template-columns:repeat({min(len(points), 3)},1fr);gap:10px;'>{pts}</div>
"""


def recap(heading, items, question, next_text):
    cards = ''.join(f"<div style='background:rgba(255,255,255,.1);border-radius:10px;padding:13px;'>"
                    f"<strong style='color:#93c5fd;font-size:.9rem;'>{h}</strong>"
                    f"<p style='color:#e2e8f0;font-size:.8rem;margin-top:5px;line-height:1.7;'>{b}</p></div>" for h, b in items)
    return f"""
<h2 style='color:#fff;font-size:1.5rem;font-weight:700;margin-bottom:14px;'>📌 {heading}</h2>
<div style='display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-bottom:14px;'>{cards}</div>
<div style='background:linear-gradient(90deg,rgba(13,148,136,.35),rgba(107,63,160,.35));border-radius:10px;padding:16px 20px;text-align:center;'>
  <p style='color:#fff;font-size:1.02rem;font-weight:700;margin:0;'>{question}</p>
  <p style='color:#cbd5e1;font-size:.82rem;margin-top:6px;'>{next_text}</p>
</div>
"""


def rubric_box(a, b, c, d, label='📏 評分規準'):
    return (f"<div style='background:#fffbeb;border-radius:10px;padding:14px;'>"
            f"<strong style='color:#92400e;font-size:.9rem;'>{label}</strong>"
            f"<p style='font-size:.78rem;color:#334155;margin-top:6px;line-height:1.8;'>"
            f"<strong style='color:#059669;'>A</strong> {a}<br><strong style='color:#2563eb;'>B</strong> {b}<br>"
            f"<strong style='color:#d97706;'>C</strong> {c}<br><strong style='color:#dc2626;'>D</strong> {d}</p></div>")


def two_col(left, right, ratio='1.2fr 1fr'):
    return f"<div style='display:grid;grid-template-columns:{ratio};gap:12px;'>{left}{right}</div>\n"


FLOW_SHAPES = {
    # 形狀: (clip-path 或圓角, 底色, 字色)
    'start': ('border-radius:999px;', '#1e3a5f', '#fff'),       # 開始／結束：橢圓
    'process': ('border-radius:4px;', '#dbeafe', '#1e3a8a'),     # 處理：矩形
    'io': ('clip-path:polygon(10% 0,100% 0,90% 100%,0 100%);', '#dcfce7', '#14532d'),  # 輸入／輸出：平行四邊形
    'decision': ('clip-path:polygon(50% 0,100% 50%,50% 100%,0 50%);', '#fef3c7', '#78350f'),  # 決策：菱形
    'loop': ('clip-path:polygon(8% 0,92% 0,100% 50%,92% 100%,8% 100%,0 50%);', '#ede9fe', '#4c1d95'),  # 迴圈：六邊形
}


def flow_node(shape, text, width=200):
    clip, bg, fg = FLOW_SHAPES[shape]
    pad = '22px 26px' if shape == 'decision' else '9px 14px'
    w = width + 60 if shape == 'decision' else width
    return (f"<div style='{clip}background:{bg};color:{fg};width:{w}px;padding:{pad};text-align:center;"
            f"font-size:.8rem;font-weight:600;line-height:1.4;'>{text}</div>")


def flow(nodes, width=200):
    """直式流程圖。nodes: [(shape, text, side)]；side 是右側說明（例如「否 → 回到加熱」），可為空字串"""
    out = "<div style='display:flex;flex-direction:column;align-items:flex-start;gap:0;'>"
    for i, (shape, text, side) in enumerate(nodes):
        side_html = (f"<div style='font-size:.75rem;color:#b45309;font-weight:600;margin-left:10px;'>{side}</div>"
                     if side else '')
        out += (f"<div style='display:flex;align-items:center;'>"
                f"<div style='width:{width + 60}px;display:flex;justify-content:center;'>{flow_node(shape, text, width)}</div>"
                f"{side_html}</div>")
        if i < len(nodes) - 1:
            out += (f"<div style='width:{width + 60}px;text-align:center;color:#64748b;font-size:.95rem;line-height:1.3;'>↓</div>")
    return out + "</div>\n"


def code_block(lines, caption=''):
    """Scratch／虛擬碼用的積木風格區塊"""
    # 顏色對應 Scratch 3 積木分類
    colors = {'event': '#ffbf00', 'motion': '#4c97ff', 'look': '#9966ff', 'ctrl': '#ffab19',
              'sense': '#5cb1d6', 'op': '#59c059', 'var': '#ff8c1a', 'pen': '#0fbd8c', 'plain': '#64748b'}
    out = "<div style='background:#f8fafc;border:1px solid #e2e8f0;border-radius:10px;padding:12px 14px;margin-bottom:10px;'>"
    if caption:
        out += f"<div style='font-size:.75rem;color:#64748b;margin-bottom:8px;'>{caption}</div>"
    for kind, text, indent in lines:
        out += (f"<div style='margin-left:{indent * 22}px;margin-bottom:4px;display:inline-block;width:auto;'>"
                f"<span style='display:inline-block;background:{colors[kind]};color:#fff;border-radius:6px;"
                f"padding:5px 12px;font-size:.8rem;font-weight:600;'>{text}</span></div><br>")
    return out + "</div>\n"
