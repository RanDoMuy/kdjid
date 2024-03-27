from .task import increase_profit_balance
from apscheduler.schedulers.background import BackgroundScheduler

def start():
    scheduler= BackgroundScheduler()
    scheduler.add_job(increase_profit_balance, 'interval', seconds=7200)
    scheduler.start()