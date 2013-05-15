import sys
import json

def main():
    #Read files from command line
    #sent_file = open(sys.argv[1])
    #tweet_file = open(sys.argv[2])
    
    #Read files directly
    sent_file = open("AFINN-111.txt")
    tweet_file = open("output_20.txt")
    
    scores = {}
    for line in sent_file:
        term, score = line.split("\t")
        scores[term] = int(score)
    
    tweet = {}
    tweets = []
    for line in tweet_file:
        tweet = json.loads(line)
        tweets.append(tweet)
    
    text_list = []
    for i in range(len(tweets)):
        if tweets.has_key('text') == True:
            text_string = tweets[i]['text']
            text_list[i] = text_string.split()
            
            for word in text_list[i]:
                
if __name__ == '__main__':
    main()