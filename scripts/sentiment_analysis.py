# sentiment_analysis.py

from csv import *
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


'''
    2045776 -- total tweets                                                                                                              
    413273  tweets talking only about Trum                                                                                
    172028  tweets talking only about Clinton 

    A VOTE value of 1 : voting for Clinton
                    0 : voting for Trump
                    
    The machine learning algorithm I used here was the sentiment analyzer - vaderSentiment
'''



# function to read in the file and convert it to 2D list
def read_file(filename):
    with open(filename, 'r') as f:
        data = [row for row in reader(f.read().splitlines())]
    return data


# this function determines the 'vote' of a tweet based off the compounded sentiment score
def get_vote(sentiment, candidate):
    if candidate == "clinton":
        #if sentiment >= 0:
            #vote = 1
        #elif sentiment < 0:
            #vote = 0
            
        if sentiment >= 0.05:
            vote = 1
        elif sentiment <= -0.05:
            vote = 0
        else:
            vote = -99  # in between are neutral sentimenst which dont get a vote
        
    elif candidate == "trump":
        #if sentiment >= 0:
            #vote = 0
        #elif sentiment < 0:
            #vote = 1
            
        if sentiment >= 0.05:
            vote = 0
        elif sentiment <= -0.05:
            vote = 1
        else:
            vote = -99  # in between are neutral sentimenst which dont get a vote
            
    return vote
    
    
    

def main():
    data =  read_file('election_tweets.csv')
    data = data[1:len(data)]  # get rid of column labels
    
    newfile = open('election_tweets_sentiment2.csv', 'wb')
    write = writer(newfile)
    write.writerow(['datetime', 'user_id', 'url', 'text',
                'usernameTweet', 'ID', 'nbr_retweet', 'nbr_reply', 'nbr_favorite', 'Clinton_sent', 'Trump_sent', 'VOTE'])

    
    hillary_words = ["hillary", "imwithher", "clinton", "hilary"]
    donald_words = ["donald", "trump", "maga"]
    
    analyser = SentimentIntensityAnalyzer()
    
    print len(data)
    i = 0
    j = 0
    for row in data:
        tweet = row[3]
        
        # try to match tweets related to hillary 
        if any(s in tweet.lower() for s in hillary_words) and not any(s in tweet.lower() for s in donald_words):
            hill_sent = analyser.polarity_scores(tweet).get("compound")
            donald_sent = -99
            vote = get_vote(hill_sent, "clinton")
            
            datetime = row[0]
            user_id = row[1]
            url = row[2]
            usernameTweet = row[4]
            ID = row[5]
            nbr_retweet = row[6]
            nbr_reply = row[7]
            nbr_favorite = row[8]
            
            r = [datetime, user_id, url, tweet,
                usernameTweet, ID, nbr_retweet, nbr_reply, nbr_favorite, hill_sent, donald_sent, vote]
            write.writerow(r)
            j += 1
        
        # try to match tweets related to donald 
        if any(s in tweet.lower() for s in donald_words) and not any(s in tweet.lower() for s in hillary_words):
            donald_sent = analyser.polarity_scores(tweet).get("compound")
            hill_sent = -99
            vote = get_vote(donald_sent, "trump")
            
            datetime = row[0]
            user_id = row[1]
            url = row[2]
            usernameTweet = row[4]
            ID = row[5]
            nbr_retweet = row[6]
            nbr_reply = row[7]
            nbr_favorite = row[8]
            
            r = [datetime, user_id, url, tweet,
                usernameTweet, ID, nbr_retweet, nbr_reply, nbr_favorite, hill_sent, donald_sent, vote]
            write.writerow(r)
            i += 1
        

    
    print i, " tweets talking only about trump"
    print j, " tweets talking only about clinton"



if __name__ == "__main__":
    main()
    
    

