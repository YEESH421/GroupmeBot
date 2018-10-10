import app

from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()
@sched.scheduled_job('cron', hour=21, minute=53)
def scheduled_job():
    app.getQuote()
sched.start()
