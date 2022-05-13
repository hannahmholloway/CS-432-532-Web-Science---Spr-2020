import tweepy
from tweepy import *
import time
import os

CONSUMER_KEY = ""
CONSUMER_SECRET = ""

OAUTH_TOKEN = ""
OAUTH_TOKEN_SECRET = ""

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN,OAUTH_TOKEN_SECRET)
api=tweepy.API(auth)

fdata=open('thepopulars.txt','w')
user=api.get_user('SenWarren')
fdata.write('SenWarren'+'\n')

for user in tweepy.Cursor(api.friends, screen_name="SenWarren",count=100).items():
	#users.append(user) 
	fdata.write(user.screen_name+',\n')
fdata.close()
