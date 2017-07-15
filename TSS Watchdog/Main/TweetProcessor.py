import TweetClassifier as tc
import Helper as h


def process_status(status):
    if not status.retweeted and "RT @" not in status.text:
        print(status.text)
        if tc.is_suspicious(status):
            print("************************************************************* Suspicious User: " + h.user_to_string(
                status.user) + " *************************************************************")
        print("")