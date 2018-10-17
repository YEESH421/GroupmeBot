import app

from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()
@sched.scheduled_job('cron', hour=15, minute=59)
def scheduled_job():
    app.getQuote()
sched.start()
