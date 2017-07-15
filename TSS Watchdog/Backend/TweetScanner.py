import tweepy

import TweetProcessor as tp
import EthanTweetProcessor as etp

import TwitterConnectionDetails as tcd

is_running = True

class ScanningStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        tp.process_status(status)

    def on_error(self, status_code):
        print("Error while trying to stream! (Error code: ",status_code,")")

        # 420 == Error given from failing to connect to the Streaming API too many times
        if status_code == 420:
            print("Rate limit error!")
            is_running = False
            return False


def running():
    return is_running


def start():
    print("Setting up connection")
    tcd.connect()

    print("Initializing Stream")
    stream = tweepy.Stream(auth = tcd.api.auth, listener = ScanningStreamListener())
    stream.filter(track=["depress", "bullied", "abuse", "hurting", "lonely", "empty inside", "kill myself"], languages=["en"])
    if is_running:
        print("Streaming tweets")