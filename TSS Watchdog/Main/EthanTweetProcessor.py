import tweepy
import nltk
import TweetClassifier as tc
import Helper as h
import io

countedWords = dict()

def process_status(status):
    logfile = open("newlog.txt", "w")
    if not status.retweeted and "RT @" not in status.text:
        print(status.text)
        if tc.is_suspicious(status):
            tokenized = nltk.word_tokenize(status.text)

            for word in tokenized:
                if word in countedWords: 
                    x = countedWords[word]
                    countedWords[word] = x + 1
                else:
                    countedWords[word] = 1

            sortedList = sorted(countedWords.items(), key=lambda x: x[1], reverse=True)
            print(sortedList)
            convertToString = ",".join("(%s,%s)" % tup for tup in sortedList)

            with io.open("testfile", "w", encoding="utf-8") as file:
                file.write(convertToString)
        print("")





