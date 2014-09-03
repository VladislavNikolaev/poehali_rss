from datetime import datetime

from sqlalchemy import Column, String, Text, DateTime

from app import db


class Topic(db.Model):

    url = Column(String(2000), primary_key=True)
    title = Column(String(250), nullable=False)
    body = Column(Text)
    date = Column(DateTime, default=datetime.utcnow, nullable=False)

    def __init__(self, url, title, body):
        self.url = url
        self.title = title
        self.body = body
