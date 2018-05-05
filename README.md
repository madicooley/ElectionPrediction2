# Predicting Election Outcome From Twitter.


# Dependencies

1. Tweepy

	pip install tweepy

2. Plotly

	pip install plotly

3. Pandas

	pip install pandas


4. TweetScraper

	https://github.com/jonbakerfish/TweetScraper


5. Vader Sentiment

	pip install vaderSentiment



# Process:

* As a note, all scripts were written in Python2.7


1. Collected tweets with the command "scrapy crawl TweetScraper -a query='#Election2016'"

2. Converted the many text files containing tweets into one csv file with 'process_files.py' created the file 'election_tweets.csv'

3. Ran 'election_tweets.csv' through the script 'converdata_counts.py' to the total number of tweets collected. This created the file 'election_tweetscounts1.csv'

4. Ran the file 'election_tweets.csv' through 'sentiment_analysis.py' this created the sentiment scores for each candidate. This created the file 'election_tweetssentiment2.csv'

5. Ran 'election_tweetssentiment2.csv' through 'count_votes.py' to count the number of votes per candidate.

6. Ran 'pop.csv' through 'convert_pop_2party.py' in order to convert the polling data to reflect a two party race. This created 'pop_2party.csv'

7. Ran the jupyter notebook 'graph.ipynb' to generate all of the relevant plots. 











