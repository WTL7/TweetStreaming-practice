import sys
import tweepy
import pandas as pd
import csv

from time import gmtime, strftime
current_time=strftime("%Y-%m-%d %Hh%Mm", gmtime())

TwitterData=pd.DataFrame(columns=['User','Coordinates','Date','Tweet'])   # create empty dataframe

keywords=["corn","soy","bean"]

consumer_key=" "
consumer_secret=" "
access_key=" "
access_secret=" "

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)


# Open/Create a file to append data
csvFile = open('Twitter_IA_MN_NE_%s.csv'%current_time, 'wb')
#Use csv Writer
csvWriter = csv.writer(csvFile)
csvWriter.writerow(['User','Latitude','Longitude','Date','Tweet']) #entity

class CustomStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        #if exact_word_match("corn", status.text):
        if any(keyword in status.text.lower() for keyword in keywords):    
            if status.geo is not None: 
                csvWriter.writerow([status.user.id,status.geo['coordinates'][0],status.geo['coordinates'][1],status.created_at,status.text.encode('utf-8')])  #writing and arranging all information in csv     
                print "IA_MN_NE ",status.created_at,status.text
                 
    def on_error(self, status_code):
        print >> sys.stderr, 'Encountered error with status code:', status_code
        return True # Don't kill the stream

    def on_timeout(self):
        print >> sys.stderr, 'Timeout...'
        return True # Don't kill the stream
#try:    
sapi = tweepy.streaming.Stream(auth, CustomStreamListener())  
    # IA MN NE
sapi.filter(locations=[-100.70,39.87,-91.20,48.48])  # Each bounding box should be specified as a pair of longitude and latitude pairs, with the southwest corner of the bounding box coming first    
#except (UnicodeEncodeError, UnicodeDecodeError):
#    print "*****************Found unicode error***************"   
#csvFile.close()        