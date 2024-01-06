from datetime import datetime

from bunnet import Document, Link

from app.models import Author


class Post(Document):
    title: str
    body: str
    author: Link[Author]
    create_date: datetime = datetime.now()
    publish_date: datetime = datetime.now()
