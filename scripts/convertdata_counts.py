# convertdata_counts.py

from csv import *

'''
    This script counts ALL tweets for each day and creates a csv with dates, and 
    counts of tweets tweeted that day. This does not guarantee that these tweets were
    all writted in the US or about the US election.
'''

# function to read in the file and convert it to 2D list
def read_file(filename):
    with open(filename, 'r') as f:
        data = [row for row in reader(f.read().splitlines())]
    return data


def main():
    # data =  read_file('election_tweets.csv') 
    data =  read_file('election_tweets_sentiment.csv') 
    data = data[1:len(data)]  # get rid of column labels
    
    newfile = open('election_tweets_counts2.csv', 'wb')
    write = writer(newfile)
    write.writerow(["Date","Number_Tweets"])
    
    row = data[0]
    date = row[0].split(' ')[0]
    num = 0
    i = 0
    # counts the number of tweets tweeted per day
    for row in data:
        datenew = row[0].split(' ')[0]
        if date == datenew:
            num += 1
        elif date != datenew:
            r = [date, num]
            write.writerow(r)
            date = datenew
            num = 0
            
        



if __name__ == "__main__":
    main()


