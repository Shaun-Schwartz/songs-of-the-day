#### SongsOfTheDay

A python script that grabs the top 5 songs from the last 24 hours from the listentothis subreddit and sends an email with links to the songs

```
mv creds.example.py creds.py
```

Edit creds.py with the appropriate info. A Reddit ID and secret can be obtained by creating an authorized app https://www.reddit.com/prefs/apps


Add recipient email addresses to recipients.py and run
```
python3 send_songs.py
```
or
```
chmod +x send_songs.py
./send_songs.py
```

Setup a cron job to run the script once a day at 2:30AM:

Run:
```
crontab -e
```
and add:
```
30 2 * * * /path/to/script
```
