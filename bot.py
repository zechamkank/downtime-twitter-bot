import urllib
import time
import tweepy

# Fill in API details and WEBSITE prior to running
CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_TOKEN = ''
ACCESS_TOKEN_SECRET = ''
WEBSITE = '' # URL of website to monitor
POLLING_TIME = 60 # Interval (in seconds) to check if site is up
DOWNTIME_MESSAGE = "Our site is currently down at the moment. Thank you for your patience." #Tweet for when site goes down
DOWNTIME_FINISHED_MESSAGE = "Our site is back up! Thanks again for your patience." #Tweet for when site comes back up

#Creating API instance
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)


def site_is_up(site):
    try :
        return (urllib.request.urlopen(WEBSITE).getcode() == 200)
    except:
        return False
    
def downtime_started():
    api.update_status(DOWNTIME_MESSAGE)
    while (not site_is_up(WEBSITE)):
        if site_is_up(WEBSITE):
            downtime_finished()
        time.sleep(POLLING_TIME)

def downtime_finished():
    api.update_status(DOWNTIME_FINISHED_MESSAGE)
    print("Site went back up at %r" % time.ctime())

def main_loop():
	while True:        
		if site_is_up(WEBSITE):
			print("Site is up")
			time.sleep(POLLING_TIME)
		else:
			print("Site went down at %r" % time.ctime())
			downtime_started()
			
main_loop()
