from flask import render_template
from main import bp

@bp.route('/')
def index():
    return render_template('index.html')
