# process_files.py


import os
import glob
import json
from csv import *
from datetime import datetime
import re                               # Regular expressions to clean tweets


"""

    Once the twitterScraper collected all of the tweets I wanted, they were all in separate files in json format.
    So this script loops through each file and pulls the data all into a csv file.

"""



# This function removes links, special characters in tweets 
def clean_tweet(tweet):
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())


# This function returns a compounded sentiment score between [-1, 1]
# 1 - highly positive sentiment, -1 - highly negative sentiment
# NOTE: Need to make this so it gets a sentiment towards Hillary and one towards Donald
def get_tweet_sentiment(tweet):
        sent = analyser.polarity_scores(tweet)
        return sent.get("compound")



path = 'C:/Users/madim/Anaconda2/envs/MachineLearning/Scripts/TweetScraper/Data/tweet/'

newfile = open('election_tweets.csv', 'wb')
write = writer(newfile)
write.writerow(['datetime', 'user_id', 'url', 'text',
                'usernameTweet', 'ID', 'nbr_retweet', 'nbr_reply', 'nbr_favorite', 'Hillary_sent', 'Donald_sent'])

print "starting"

for filepath in glob.glob(os.path.join(path, '*')):
    with open(filepath) as f:
        #content = f.read()
        content = json.load(f)
        datetime = content.get('datetime').encode("utf8")
        is_reply = content.get('is_reply')
        is_retweet = content.get('is_retweet')
        user_id = content.get('user_id')
        url = content.get('url')
        text = clean_tweet(content.get('text').encode("utf8"))
        usernameTweet = content.get('usernameTweet').encode("utf8")
        ID = content.get('ID')
        nbr_retweet = content.get('nbr_retweet')
        nbr_reply = content.get('nbr_reply')
        nbr_favorite = content.get('nbr_favorite')
        
        # get tweets between 2016-05-08 , 2017-01-07  ( two months before and after the poll data)
        if "2017-01-08" in datetime:
            break
        
        # dont count retweets or replies
        if is_reply == False and is_retweet == False:
            # NOTE: get sentiments here
            hill_sent = -99
            donald_sent = -99
            
            r = [datetime, user_id, url, text,
                usernameTweet, ID, nbr_retweet, nbr_reply, nbr_favorite, hill_sent, donald_sent]
            write.writerow(r)
    
    
    
print "done"
