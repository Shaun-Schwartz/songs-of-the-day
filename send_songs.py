#!/usr/bin/env python3.6
import requests
import requests.auth
import json
from creds import *
from send_email import send_email
from recipients import RECIPIENTS

USER_AGENT = "SongsOfTheDay/0.1 by %s" %(REDDIT_USER)
NUM_OF_SONGS = 5 # Maximum is 25

def get_token():
    client_auth = requests.auth.HTTPBasicAuth(CLIENT_ID, CLIENT_SECRET)
    post_data = {"grant_type": "password", "username": REDDIT_USER, "password": REDDIT_PWD}
    headers = {"User-Agent": USER_AGENT}
    response = requests.post("https://www.reddit.com/api/v1/access_token", auth=client_auth, data=post_data, headers=headers).json()
    return response['access_token']

def get_songs():
    token = get_token()
    msgText = ''
    headers = {"Authorization": f'bearer {token}', "User-Agent": USER_AGENT}
    response = requests.get("https://oauth.reddit.com/r/listentothis/top/?t=day/.json", headers=headers).json()
    for i in range(NUM_OF_SONGS):
        try:
            title = response["data"]["children"][i]["data"]["secure_media"]["oembed"]["title"]
            thumbnail = response["data"]["children"][i]["data"]["secure_media"]["oembed"]["thumbnail_url"]
            media_url = response["data"]["children"][i]["data"]["url"]
            link = "https://www.reddit.com" + response["data"]["children"][i]["data"]["permalink"]
            msgText += f"{i+1}: {title} \n{media_url} \n{link} \n \n \n "
        except:
            pass
    return msgText

msg = get_songs()

send_email(EMAIL_USER, EMAIL_PWD, RECIPIENTS, "SongsOfTheDay", msg)
