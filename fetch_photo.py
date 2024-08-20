#!/usr/bin/env python3
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

google_photos = build('photoslibrary', 'v1', credentials=creds, static_discovery=False)

#day, month, year = ('0', '6', '2019')  # Day or month may be 0 => full month resp. year
#date_filter = [{"day": day, "month": month, "year": year}]  # No leading zeroes for day an month!
nextpagetoken = 'Dummy'
filtered_items = []
while nextpagetoken != '':
    nextpagetoken = '' if nextpagetoken == 'Dummy' else nextpagetoken
    results = google_photos.mediaItems().search(
            body={"filters":  {"featureFilter": {"includedFeatures": ['FAVORITES']}, "mediaTypeFilter": {"mediaTypes": ['PHOTO']}},
                  "pageSize": 100, "pageToken": nextpagetoken}).execute()
    # The default number of media items to return at a time is 25. The maximum pageSize is 100.
    items = results.get('mediaItems', [])
    nextpagetoken = results.get('nextPageToken', '')
    for item in items:
        if (item['mediaMetadata']['width'] < item['mediaMetadata']['height']):
#			print("{} {} {} {}\nURL: {}\n{} x {}".format(item['filename'], item['mimeType'], item.get('description', '- -'), item['mediaMetadata']['creationTime'], item['productUrl'], item['mediaMetadata']['width'], item['mediaMetadata']['height']))
            filtered_items.append(item)

print("Size of list is: {}".format(len(filtered_items)))
random_index = random.randint(0,len(filtered_items)-1)
lucky_item = filtered_items[random_index]
print("{} {} {} {}\nURL: {}\n{} x {}".format(lucky_item['filename'], lucky_item['mimeType'], lucky_item.get('description', '- -'), lucky_item['mediaMetadata']['creationTime'], lucky_item['productUrl'], lucky_item['mediaMetadata']['width'], lucky_item['mediaMetadata']['height']))

#https://developers.google.com/photos/library/guides/access-media-items#base-urls
#url = lucky_item['baseUrl'] + '=w384-h640-c-d'
url = lucky_item['baseUrl'] + '=w384-h640-c-d'

myfile = requests.get(url)

open('pic/Image.jpg', 'wb').write(myfile.content)
