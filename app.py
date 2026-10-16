# -*- coding: utf-8 -*-
import sys, os, importlib, copy
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from flask import Flask, render_template, jsonify, abort
from content.enhancements import ENHANCEMENTS

app = Flask(__name__)
N_CHAPTERS = 10

def load_ch(n):
    if not 1 <= n <= N_CHAPTERS:
        abort(404)
    return importlib.import_module(f'content.ch{n:02d}')

def apply_enhancements(slides, chapter_n):
    """將 enhancements.py 的內容合併到投影片清單"""
    ch_enh = ENHANCEMENTS.get(chapter_n, {})
    if not ch_enh:
        return slides
    result = []
    for slide in slides:
        sid = slide.get('id')
        if sid in ch_enh:
            s = copy.copy(slide)
            enh = ch_enh[sid]
            if 'video' in enh:
                s['video'] = enh['video']
            if 'html_append' in enh:
                s['html'] = s.get('html', '') + enh['html_append']
            if 'html_prepend' in enh:
                s['html'] = enh['html_prepend'] + s.get('html', '')
            result.append(s)
        else:
            result.append(slide)
    return result

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/rubric')
def rubric():
    return render_template('rubric.html')

@app.route('/ch/<int:n>')
def chapter(n):
    ch = load_ch(n)
    slides = apply_enhancements(ch.SLIDES, n)
    return render_template('slides.html', chapter_n=n, home_url='/',
                           total_slides=len(slides), chapters=ch.CHAPTERS)

@app.route('/api/slides/<int:n>')
def api_slides(n):
    ch = load_ch(n)
    return jsonify(apply_enhancements(ch.SLIDES, n))

@app.route('/api/quizzes/<int:n>')
def api_quizzes(n):
    return jsonify(load_ch(n).QUIZZES)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
