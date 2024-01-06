from flask import render_template
from app.routes.public import public

from app.models import Author, Post

@public.route('/')
def index():
    context = {}
    return render_template('index.j2', **context)