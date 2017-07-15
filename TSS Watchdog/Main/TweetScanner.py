import tweepy

class ScanningStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        print("Status:",end=' ')
        print(status.text)
        print()

    def on_error(self, status_code):
        print("Error while trying to stream! (Error code: ",status_code,")")
        #420 == Error given from failing to connect to the Streaming API too many times
        if status_code == 420:
            print("Rate limit error!")
            return False

def running():
    return True

def connect():
    print("Setting up authentication")

    auth = tweepy.OAuthHandler("i4SQAovlLNQhflgfFy1pMVVT6",                         # Consumer Key
                           "F0FK9sOkOD3DmOMOivPESfQP2Vx6da2addUE0FApd1qVurtybK")    # Consumer Secret

    auth.set_access_token("886035091448893442-hOwTGGgxrbWyO72GQPI48I9WBkCVhsd",      # Access token
                           "Vb2iNiH266zAwYr6J8iNLEflS4h8JS8KlUY6JbPFoOCun")         # Access Secret

    print("Getting API")
    api = tweepy.API(auth)

    print("Initializing Stream")
    stream = tweepy.Stream(auth = api.auth, listener = ScanningStreamListener())
    stream.filter(locations=[-180,-90,180,90])
    print("Finished connecting")