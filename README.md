# profile-picture-updater
A script that is intended to run as a cron job, that every day updates my twitter profile picture via an API as well as tweets a stock price.

For it to work you must have Twitter Developer access.

For now I can't update my profile via the twitter v2 api but I'm finished with the auto tweeting

I've set it to the following chronjob:
```29 16 * * 1-5 TZ=Europe/Stockholm if [ $(date +\%u) -lt 6 ]; then /path/to/python /path/to/script.py; fi```