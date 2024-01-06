from flask import jsonify
from lorem import sentence, paragraph

from app.models import Author, Post
from app.routes.public import public


def create_author(nick: str):
    author = Author.find_one(Author.nick == nick).run()
    if not author:
        Author(
            nick='sgaduuw',
            first_name='Eelco',
            last_name='Wesemann'
        ).save()
    return author


def create_ipsum_post(nick: str) -> None:
    Post(
        title=sentence(),
        body=paragraph(),
        author=Author.find_one(Author.nick == nick).run()
    ).save()


@public.route('/')
def index():
    author = create_author(nick='sgaduuw')
    create_ipsum_post(author.nick)
    q_posts = Post.find(fetch_links=True).to_list()

    posts = [{
        'author': q.author.nick,
        'title': q.title,
        'body': q.body,
        'publish_date': q.publish_date
    } for q in q_posts]

    context = {
        'posts': posts
    }
    return jsonify(context)
