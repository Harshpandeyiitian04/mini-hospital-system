from google_auth_oauthlib.flow import Flow

def get_google_flow():
    flow = Flow.from_client_secrets_file(
        "credentials.json",
        scopes=[
            "https://www.googleapis.com/auth/calendar"
        ],
        redirect_url="http://127.0.0.1:8000/oauth/callback/"
    )

    return flow