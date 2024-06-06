import smtplib
from datetime import datetime

from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask


def send_email(subject, body, to):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login("your_email@gmail.com", "your_password")
    message = f"Subject: {subject}\n\n{body}"
    server.sendmail("your_email@gmail.com", to, message)
    server.quit()


def schedule_notification(event):
    scheduler = BackgroundScheduler()
    event_time = event.start_time
    scheduler.add_job(
        func=send_email,
        trigger="date",
        run_date=event_time,
        args=[
            f"Event Reminder: {event.title}",
            f'Your event "{event.title}" is starting now.',
            "recipient_email@example.com",
        ],
    )
    scheduler.start()
