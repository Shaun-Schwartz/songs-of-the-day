#!/usr/bin/env python3.6
import schedule
import time
from get_songs import get_songs
from creds import *
from send_email import send_email
from recipients import RECIPIENTS

JOB_RUN_TIME = "01:00"

def job():
    msg = get_songs
    send_email(EMAIL_USER, EMAIL_PWD, RECIPIENTS, "SongsOfTheDay", get_songs())

schedule.every().day.at(JOB_RUN_TIME).do(job)

while True:
    schedule.run_pending()
    time.sleep(60)
