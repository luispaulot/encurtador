import pytz
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
from .models import Url


def remove_url():
	result = Url.objects.filter(expired_at__lte=datetime.now())
	result.delete()


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(remove_url, 'interval', minutes=10)
    scheduler.start()