#### SongsOfTheDay

A python script that grabs the top 5 songs from the last 24 hours from the listentothis subreddit and sends an email with links to the songs.

##### Setup:
Install required packages:
```
pip install -r requirements.txt
```

Create creds.py:
```
mv creds.example.py creds.py
```

Edit creds.py with the appropriate info. A Gmail account and Reddit account are required. A Reddit ID and secret can be obtained by creating an authorized app https://www.reddit.com/prefs/apps

Add recipient email addresses to recipients.py.

Run schedule_send_songs.py:
```
nohup python3 schedule_send_songs.py &
```
This will schedule a job to run at 1AM every day to send the email. Edit JOB_RUN_TIME in schedule_send_songs.py to change the time the job runs.

Alternatively uncomment the last 2 lines of get_songs.py and run as needed with:
```
python3 get_songs.py
```
or
```
chmod +x get_songs.py
./get_songs.py
```
