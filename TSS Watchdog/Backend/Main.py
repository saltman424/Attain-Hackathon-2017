import time

import TweetScanner as ts


api = ts.start()
while ts.running():
    time.sleep(60)