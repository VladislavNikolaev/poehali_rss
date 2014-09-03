import os

from flask import Flask, request, redirect, url_for
from flask.ext.sqlalchemy import SQLAlchemy
from werkzeug.contrib.atom import AtomFeed


SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']


app = Flask(__name__)
app.config.from_object(__name__)
db = SQLAlchemy(app)


from db import Topic


@app.route('/')
def home():
    return redirect(url_for('feed'))


@app.route('/topics.atom')
def feed():
    feed = AtomFeed('Recent Articles', feed_url=request.url, url=request.url_root)
    for topic in db.session.query(Topic).order_by(Topic.date.desc()).limit(20).all():
        feed.add(topic.title, topic.body, content_type='html', url=topic.url, published=topic.date)
    db.session.rollback()
    return feed.get_response()
