import requests

EMAIL_SERVICE_URL = "http://localhost:3000/dev/send-email"


def send_email(action, email, name, doctor=None, time=None):
    payload = {
        "action": action,
        "email": email,
        "name": name,
        "doctor": doctor,
        "time": time
    }
    try:
        requests.post(EMAIL_SERVICE_URL, json=payload)
    except Exception as e:
        print("Email service error:", e)