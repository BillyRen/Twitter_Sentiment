import sys
import json

def main():
    #Read files from command line
    #sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[1])
    
    #Read files directly
    #sent_file = open("AFINN-111.txt")
    #tweet_file = open("output_20.txt")
    
    tweet = {}
    tweets = []
    for line in tweet_file:
        tweet = json.loads(line)
        tweets.append(tweet)
        
    #Calculate total words in all tweets
    text_list = {}
    total_words = 0
    for i in range(len(tweets)):
        if tweets[i].has_key('text') == True:
            total_word = 0
            text_string = tweets[i]['text']
            text_list[i] = text_string.split()
            
            for word in text_list[i]:
                total_word += 1
            
            total_words += total_word
    
    #Calculate word counts
    word_list = {}
    for i in range(len(tweets)):
        if tweets[i].has_key('text') == True:
            total_word = 0
            text_string = tweets[i]['text']
            text_list[i] = text_string.split()
            
            for word in text_list[i]:
                if word not in word_list.keys():
                    word_list[word] = 1
                else:
                    word_list[word] += 1
    word_freq = {}
    for word in word_list.keys():
        word_freq[word] = word_list[word] / total_words
        print word, '\t', float(word_freq[word])
        #print word,'\t',word_list[word],'\t',word_freq[word]
                    
    #print "total words", total_words                
if __name__ == '__main__':
    main()