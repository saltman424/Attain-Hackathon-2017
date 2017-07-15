import time

import TweetScanner as ts


ts.start()
while ts.running():
    time.sleep(60)