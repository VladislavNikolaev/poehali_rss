from datetime import datetime

from sqlalchemy import Column, String, Text, DateTime

from app import db


class Topic(db.Model):

    url = Column(String(2000), primary_key=True)
    title = Column(String(250), nullable=False)
    body = Column(Text)
    published = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated = Column(DateTime, default=datetime.utcnow, nullable=False)

    def __init__(self, url, title, published, updated, body):
        self.url = url
        self.title = title
        self.published = published
        self.updated = updated
        self.body = body
