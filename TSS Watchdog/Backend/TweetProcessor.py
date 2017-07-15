import TweetClassifier as tc
import UserClassifier as uc


def process_status(status):
    if not status.retweeted and "RT @" not in status.text:
        print(status.text)
        if status.id is not None and status.user.screen_name is not None:
            print("https://www.twitter.com/" + status.user.screen_name + "/status/" + str(status.id))

        is_suspicious_tweet, tweet_score = tc.is_suspicious(status)
        print("Tweet suspiciousness: " + str(tweet_score) + " / " + str(tc.threshold_score))
        if is_suspicious_tweet:
            is_suspicious_user, user_score = uc.is_suspicious(status)
            print("User suspiciousness: " + str(user_score) + " / " + str(uc.threshold_score))
            if is_suspicious_user:
                print("**********************************************************************************************************************************************************")
                print("*********************************** Suspicious User: " + user_to_string(status.user) + " ***********************************")
                print("**********************************************************************************************************************************************************")
        print("")



def user_to_string(user):
    output = "["
    vals = 0
    if user.name is not None:
        output += "name = '" + user.name + "'"
        vals += 1
    if user.screen_name is not None:
        if vals > 0:
            output += ", "
        output += " screen_name = '" + user.screen_name + "', profile_url = https://twitter.com/" + user.screen_name
        vals += 1
    output += "]"
    return output