import TweetScanner as ts
import UserScanner as us
import time

ts.connect()
while ts.running():
    time.sleep(60)