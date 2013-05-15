import sys
import json

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    #sent_file = open("AFINN-111.txt")
    #tweet_file = open("output.txt")
    
    scores = {}
    for line in sent_file:
        term, score = line.split("\t")
        scores[term] = int(score)
    
    data = {}
    datas = []
    for line in tweet_file:
        data = json.loads(line)
        datas.append(data)
    
    text_list = []
    total_sents = []
    for i in range(len(datas)):
        if datas[i].has_key('text') == True:
            total_sent = 0
            text_string = datas[i]['text']
            text_list = text_string.split()
            for word in text_list:
                if word in scores.keys():
                    total_sent += scores[word]
            total_sents.append(total_sent)
        else:
            total_sents.append(0)
        print total_sents[i]

if __name__ == '__main__':
    main()
