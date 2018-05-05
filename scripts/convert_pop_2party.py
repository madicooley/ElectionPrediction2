# convert_pop_2party.py

"""
    This script converts the percentages in the pop.csv file to represent a two 
    party race in order to be compared to the twitter data.

"""

from csv import *
import re


# function to read in the file and convert it to 2D list
def read_file(filename):
    with open(filename, 'rU') as f:
        data = [row for row in reader(f.read().splitlines())]
        # data = [row for row in reader(re.split(r'\t', f.read()))]
    return data


# this function finds the adjusted predicted percentages to represent a two party race
# APC1 = PC1 / PC1 + PC2
# where PC1: percentage for candidate 1
# PC2: percentage for candidate 2
# and APC1 is the adjusted percentage for candidate 1
# returns a tuple (APC1, APC2)
def find_adjusted(PC1, PC2):
    APC1 = PC1 / (PC1 + PC2)
    APC2 = PC2 / (PC1 + PC2)
    
    return APC1*100, APC2*100
    
    
    
    
def main():
    data =  read_file('pop.csv')
    data = data[1:len(data)]  # get rid of column labels
    
    newfile = open('pop_2party.csv', 'wb')
    write = writer(newfile)
    write.writerow(["Date", "N", "Trump", "Clinton", "sediff", "Lo", "Up", "Converted_Trump", "Converted_Clinton"])
    
    i = 0
    for row in data:
        row = re.split(r'\t+', row[0])
        #print row[0]
        adj_trump, adj_clinton = find_adjusted(float(row[2]), float(row[3]))
        print adj_trump, adj_clinton
        
        r = [row[0], row[1], row[2], row[3], row[4], row[5], row[6], adj_trump, adj_clinton]
        write.writerow(r)
                
    
    
if __name__ == "__main__":
    main()
    
    
    
    
    
