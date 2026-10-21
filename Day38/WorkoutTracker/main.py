import os.path
import requests

from datetime import datetime

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build


SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets"
]

SPREADSHEET_ID = "1FrpQcSguBQ3G-NCjV05UDVTAZk-V5XxkVWmEEJ9eA_o"

SHEET_RANGE = "Workouts!A:E"

EXERCISE_API = "https://exercise-api.com/v1/exercises"


def get_credentials():

    credentials = None

    if os.path.exists("token.json"):

        credentials = Credentials.from_authorized_user_file(
            "token.json",
            SCOPES
        )

    if not credentials or not credentials.valid:

        if credentials and credentials.expired and credentials.refresh_token:

            credentials.refresh(Request())

        else:

            flow = InstalledAppFlow.from_client_secrets_file(
                "credentials.json",
                SCOPES
            )

            credentials = flow.run_local_server(
                port=0
            )

        with open("token.json", "w") as token:

            token.write(credentials.to_json())

    return credentials


def get_exercises():

    response = requests.get(
        EXERCISE_API
    )

    response.raise_for_status()

    return response.json()


def add_workout(service):

    exercise_name = input(
        "Enter exercise name: "
    )

    duration = input(
        "Enter duration in minutes: "
    )

    notes = input(
        "Enter notes: "
    )

    now = datetime.now()

    date = now.strftime(
        "%Y-%m-%d"
    )

    time = now.strftime(
        "%H:%M:%S"
    )

    values = [[
        date,
        time,
        exercise_name,
        duration,
        notes
    ]]

    body = {
        "values": values
    }

    service.spreadsheets().values().append(
        spreadsheetId=SPREADSHEET_ID,
        range=SHEET_RANGE,
        valueInputOption="USER_ENTERED",
        insertDataOption="INSERT_ROWS",
        body=body
    ).execute()

    print(
        "Workout saved successfully!"
    )


def main():

    credentials = get_credentials()

    service = build(
        "sheets",
        "v4",
        credentials=credentials
    )

    add_workout(service)


if __name__ == "__main__":
    main()
