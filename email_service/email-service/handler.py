import json
import smtplib
import os
from email.mime.text import MIMEText


SMTP_EMAIL = os.environ.get("SMTP_EMAIL")
SMTP_PASSWORD = os.environ.get("SMTP_PASSWORD")


def send_email(event, context):
    body = event.get("body")
    if isinstance(body, str):
        body = json.loads(body)
    print("REQUEST BODY:", body)
    action = body.get("action")
    to_email = body.get("email")
    name = body.get("name")
    if action == "SIGNUP_WELCOME":
        subject = "Welcome to HMS"
        message = f"Hello {name}, welcome to the Hospital Management System."
    elif action == "BOOKING_CONFIRMATION":
        doctor = body.get("doctor")
        time = body.get("time")
        subject = "Appointment Confirmed"
        message = f"Your appointment with Dr {doctor} is confirmed at {time}."
    else:
        subject = "HMS Notification"
        message = "Notification from HMS"
    try:
        msg = MIMEText(message)
        msg["Subject"] = subject
        msg["From"] = SMTP_EMAIL
        msg["To"] = to_email
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(SMTP_EMAIL, SMTP_PASSWORD)
        server.sendmail(SMTP_EMAIL, to_email, msg.as_string())
        server.quit()
        print("EMAIL SENT SUCCESSFULLY")
    except Exception as e:
        print("EMAIL ERROR:", str(e))

    return {
        "statusCode": 200,
        "body": json.dumps({"message": "done"})
    }