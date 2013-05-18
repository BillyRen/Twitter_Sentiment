# -*- coding: utf-8 -*-
import sys
import json

def main():
    #Read files from command line
    tweet_file = open(sys.argv[1])
    
    #Read files directly
    #tweet_file = open("output.txt")
    
    tweet = {}
    tweets = []
    for line in tweet_file:
        tweet = json.loads(line)
        tweets.append(tweet)
    
    hashtags = {}
    for tweet in tweets:
        if tweet.has_key('entities') == True:
            if tweet['entities']['hashtags']:
                hashtag = tweet['entities']['hashtags'][0]['text']
                if hashtag not in hashtags.keys():
                    hashtags[hashtag] = 1
                else:
                    hashtags[hashtag] += 1              
    
    i = 0
    for hashtag in hashtags:
        if i < 10:
            print hashtag, '\t', hashtags[hashtag]
            i += 1
               
if __name__ == '__main__':
    main()