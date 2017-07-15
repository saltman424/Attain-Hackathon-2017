import TweetScanner as ts
import UserScanner as uc
import time

ts.connect()
while ts.running():
    time.sleep(60)