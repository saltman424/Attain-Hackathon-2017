import TweetScanner as ts
import UserClassifier as uc
import time

ts.connect()
while ts.running():
    time.sleep(60)