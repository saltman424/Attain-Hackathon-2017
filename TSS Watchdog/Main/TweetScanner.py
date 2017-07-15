import tweepy

import TweetProcessor as tp
import EthanTweetProcessor as etp


auth1 = tweepy.OAuthHandler("i4SQAovlLNQhflgfFy1pMVVT6",                                # Consumer Key
                                "F0FK9sOkOD3DmOMOivPESfQP2Vx6da2addUE0FApd1qVurtybK")   # Consumer Secret
auth1.set_access_token("886035091448893442-hOwTGGgxrbWyO72GQPI48I9WBkCVhsd",            # Access token
                          "Vb2iNiH266zAwYr6J8iNLEflS4h8JS8KlUY6JbPFoOCun")              # Access Secret

auth2 = tweepy.OAuthHandler("4gZUSeRuqL2UtxaTuE6VzAokz",                                # Consumer Key
                                "OHwKB9GVSnhX8iOKSJt6w8ipWpxm6em1c2WiqIE6tHSZ7V6oc0")   # Consumer Secret
auth2.set_access_token("886115828797779968-P0bFhQC1o7lLihY4IvHUtdIMTOz51oi",            # Access token
                          "YDQ5wNQINZGVyoCaZ9weh72QyEj2RXk186XLrfYx6SPCh")              # Access Secret

curr_auth = auth2


class ScanningStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        etp.process_status(status)

    def on_error(self, status_code):
        print("Error while trying to stream! (Error code: ",status_code,")")

        # 420 == Error given from failing to connect to the Streaming API too many times
        if status_code == 420:
            print("Rate limit error!")
            return False


def running():
    return True


def start():
    print("Setting up authentication")

    print("Getting API")
    api = tweepy.API(curr_auth)

    print("Initializing Stream")
    stream = tweepy.Stream(auth = api.auth, listener = ScanningStreamListener())
    stream.filter(track=["depress", "bullied", "pain", "hurting", "lonely"], languages=["en"])
    print("Finished connecting")