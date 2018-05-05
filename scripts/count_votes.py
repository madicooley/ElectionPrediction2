# count_votes.py

from csv import *
import datetime 

'''
    This script counts votes for each candidate per day.
'''

# function to read in the file and convert it to 2D list
def read_file(filename):
    with open(filename, 'r') as f:
        data = [row for row in reader(f.read().splitlines())]
    return data


# This function converts the dates to a standard format
def convert_date(date):
    vec = date.split('-')
    year = vec[0]
    month = vec[1]
    day = vec[2]
    #print int(month), int(year), int(day)
    date = datetime.date(int(year), int(month), int(day))
    # print date
    
    startdate = datetime.date(2016, 07, 10)
    enddate = datetime.date(2016, 11, 07)
    
    if date < startdate or date > enddate: #and int(day) < 10:
        return "continue"
    else:
        date = month+"/"+day+"/"+year
        return date
    


def main():
    # data =  read_file('election_tweets.csv') 
    data =  read_file('election_tweets_sentiment2.csv') 
    data = data[1:len(data)]  # get rid of column labels
    
    newfile = open('election_tweets_counts6.csv', 'wb')
    write = writer(newfile)
    write.writerow(["Date", "Total_Number_Tweets", "Votes_forTrump", "Percent_forTrump", "Votes_forClinton", "Percent_forClinton"])
    
    row = data[0]   # row 65 is where 2016-07-10 is
    date = row[0].split(' ')[0]
    num = 0
    i = 0
    trumpvotes = 0
    clintvotes = 0
    # counts the number of tweets tweeted per day
    for row in data:
        datenew = row[0].split(' ')[0]

        if date == datenew:    
            #print int(row[11])
            if int(row[11]) == 0:
                trumpvotes += 1
                num += 1
            elif int(row[11]) == 1:
                clintvotes += 1
                num += 1
            elif int(row[11]) == -99:   # neutral votes
                continue

        elif date != datenew:
            percenttrump = float(trumpvotes) / num * 100
            percentclint = float(clintvotes) / num * 100
            d = convert_date(date)
            
            if d == "continue":
                date = datenew
                num = 0
                trumpvotes = 0
                clintvotes = 0
            else:
                r = [d, num, trumpvotes, percenttrump, clintvotes, percentclint]
                write.writerow(r)
                date = datenew
                num = 0
                trumpvotes = 0
                clintvotes = 0
            
        i += 1
        

if __name__ == "__main__":
    main()

