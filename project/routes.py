from project import app
from flask import render_template, request
from project.models import Post

@app.route('/')
def index():
    q = request.args.get('q')
    if q:
        posts = Post.query.filter(Post.number.contains(q)).all()
    else:
        posts = dict()
    return render_template("index.html", posts=posts)