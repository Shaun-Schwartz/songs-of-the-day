import requests
import requests.auth
import json
from creds import *
from send_email import send_email

USER_AGENT = "SongsOfTheDay/0.1 by %s" %(REDDIT_USER)

def get_token():
    client_auth = requests.auth.HTTPBasicAuth(CLIENT_ID, CLIENT_SECRET)
    post_data = {"grant_type": "password", "username": REDDIT_USER, "password": REDDIT_PWD}
    headers = {"User-Agent": USER_AGENT}
    response = requests.post("https://www.reddit.com/api/v1/access_token", auth=client_auth, data=post_data, headers=headers).json()
    return response['access_token']

def get_songs():
    token = get_token()
    headers = {"Authorization": f'bearer {token}', "User-Agent": USER_AGENT}
    response = requests.get("https://oauth.reddit.com/r/listentothis/top/?t=day/?limit=1/.json", headers=headers).json()
    return response["data"]["children"][0]["data"]["secure_media"]["oembed"]["thumbnail_url"]


print(get_songs())

# recipients = ["me@shaunschwartz.com"]
#
# https://www.reddit.com/r/hip_hop/
# https://www.reddit.com/r/listentothis/
#
# send_email(EMAIL_USER, EMAIL_PWD, recipients, "LyricOfTheDay", lyrics[rn])
