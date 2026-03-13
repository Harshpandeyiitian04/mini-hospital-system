from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build


def create_calendar_event(user_token, summary, start_time, end_time):
    creds = Credentials(**user_token)
    service = build("calendar", "v3", credentials=creds)
    event = {
        "summary": summary,
        "start": {
            "dateTime": start_time,
            "timeZone": "UTC"
        },
        "end": {
            "dateTime": end_time,
            "timeZone": "UTC"
        }
    }
    event = service.events().insert(
        calendarId="primary",
        body=event
    ).execute()
    return event["id"]