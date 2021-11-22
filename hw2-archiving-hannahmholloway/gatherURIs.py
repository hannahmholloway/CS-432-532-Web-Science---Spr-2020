import urllib
import json
import tweepy
import sys
import time

ACCESS_TOKEN = '157985123-WFvzlfDa8KStBZzevMfQBTM7fi8zKHYl2LQpTfGr'  
ACCESS_SECRET = 'lSax0XLwIimJ4VVbuU5OY9BpBic4vsSFi0riAq3DPvTxU'
CONSUMER_KEY = 'wTSsHE3PTA3ZZPiaKHEiQnLtf'
CONSUMER_SECRET = 'UblYYCmNYIEffAY4T4QHGHXwAWMFqiueXdxf35xZFhoK3AECP1'
i=0

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)  
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)


api = tweepy.API(auth) 

var=sys.argv[1] 						
list_of_urls=set()  			
output_file=open('links','a')				
Final_results = tweepy.Cursor(api.search,q=var).items()
while True:
	try:
		status = Final_results.next()
		element=status._json
		one_element={} 
		
		i=i+1
		for url in element['entities']['urls']: 
			if len(list_of_urls) == 1000: 
				break
			else:
				response=urllib.urlopen(url['url'])
				final_url=response.url
				print response.getcode()
				print final_url
				print len(list_of_urls)
				if response.getcode()==200: 
					if final_url in list_of_urls:
						break
					else:
						one_element['tweet_id'] = element['id_str']  
						one_element['date_of_creation'] = element['user']['created_at']
						list_of_urls.add(final_url)
						one_element['url']=final_url
						output_file.write(json.dumps(one_element)+'\n') 
						
		if len(list_of_urls) == 1000:  
			break	
	except tweepy.TweepError :
		time.sleep(60 * 1)
        continue
print len(list_of_urls)
