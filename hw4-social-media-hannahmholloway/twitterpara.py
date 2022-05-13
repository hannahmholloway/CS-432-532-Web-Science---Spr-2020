import tweepy
import time
import csv

csv_writer = csv.writer(open("following_count.csv", "wb"))
csv_writer1 = csv.writer(open("following_count_without_me.csv", "wb"))
csv_writer.writerow(['Name','num_following'])
csv_writer1.writerow(['Name','num_following'])
ACCESS_TOKEN = ''  # Variables that contains the user credentials to access Twitter API 
ACCESS_SECRET = ''
CONSUMER_KEY = ''
CONSUMER_SECRET = ''
count = 0

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)   #Authentication is handled by the tweepy.AuthHandler class
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)


api = tweepy.API(auth) # Construct the API instance

for user in tweepy.Cursor(api.friends, screen_name="hollowayhannah_").items():
	csv_writer.writerow([user.screen_name,int(user.friends_count)])
	csv_writer1.writerow([user.screen_name,int(user.friends_count)])
	count=count +1 # to count number of friends of mln
csv_writer.writerow(['hollowayhannah_',count]) 
