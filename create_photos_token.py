from __future__ import print_function
import datetime
import pickle
import os.path
import random
import requests
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from os.path import join, dirname
#from oauth2client import file

#lpicks a random photo from Google photos that is marked as a Favorite that is a photo and in portrait mode

SCOPES = ['https://www.googleapis.com/auth/photoslibrary.readonly']

creds = None
# The file token.pickle stores the user's access and refresh tokens, and is
# created automatically when the authorization flow completes for the first
# time.

#store = file.Storage(join(dirname(__file__), 'token.photos'))
#creds = store.get()

if not os.path.exists('credentials.json'):
    print("credentials file is missing")
    quit()
if os.path.exists('token.photos'):
    with open('token.photos', 'rb') as token:
        creds = pickle.load(token)
# If there are no (valid) credentials available, let the user log in.
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(
            'credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open('token.photos', 'wb') as token:
        pickle.dump(creds, token)

