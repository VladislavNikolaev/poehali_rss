from apscheduler.schedulers.blocking import BlockingScheduler

from app import db
from db import Topic
from parser import parse_list, parse_page


sched = BlockingScheduler()


@sched.scheduled_job('interval', minutes=10)
def scrape():
    for url, title in parse_list():
        topic = db.session.query(Topic).filter(Topic.url == url).first()
        if topic:
            continue
        body = parse_page(url)
        db.session.add(Topic(url, title, body))
    db.session.commit()


sched.start()
