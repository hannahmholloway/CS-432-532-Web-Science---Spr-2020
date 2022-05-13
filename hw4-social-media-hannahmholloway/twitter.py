import tweepy
from tweepy import *
import time
import os
CONSUMER_KEY = "lYUHPYN8uCL84oesFXnhH9FSh"
CONSUMER_SECRET = "wCPmeGp2s5v0mLq3c56aa5PjJMzpV2YxNhy2XAPRuUsMNPrS6X"

OAUTH_TOKEN = "4856503619-PLk2k6r2pOg33ldUCGOrNaQXJSFVnUk3oRNNweX"
OAUTH_TOKEN_SECRET = "SUaYa2LCic9edYkV9fP43R6qKBw03ynKemMQ0bm4G9qOy"

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN,OAUTH_TOKEN_SECRET)
api=tweepy.API(auth)
users = []
fdata=open('twitter.data.raw','w')
user=api.get_user('hollowayhannah_')
users.append({'count':user.followers_count,'name':'Hannah'})

for user in tweepy.Cursor(api.followers, screen_name="hollowayhannah_",count=200).items():
	#users.append(user) 
	users.append(dict({'name':user.screen_name,'count':user.followers_count}))
for tu in users:
	fdata.write(str(tu['count'])+"\t"+tu['name']+'\n')
os.system('sort -n -k1 twitter.data.raw > twitter.data')
fdata.close()
