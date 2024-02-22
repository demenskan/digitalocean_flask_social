from flask import render_template
from posts import bp
from extensions import db
from models.post import Post

@bp.route('/')
def index():
    posts = Post.query.all()
    return render_template('posts/index.html', posts=posts)

@bp.route('/categories/')
def categories():
    return render_template('posts/categories.html')
