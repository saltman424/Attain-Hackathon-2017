import tweepy

auth1 = tweepy.OAuthHandler("i4SQAovlLNQhflgfFy1pMVVT6",                                # Consumer Key
                                "F0FK9sOkOD3DmOMOivPESfQP2Vx6da2addUE0FApd1qVurtybK")   # Consumer Secret
auth1.set_access_token("886035091448893442-hOwTGGgxrbWyO72GQPI48I9WBkCVhsd",            # Access token
                          "Vb2iNiH266zAwYr6J8iNLEflS4h8JS8KlUY6JbPFoOCun")              # Access Secret

auth2 = tweepy.OAuthHandler("i4SQAovlLNQhflgfFy1pMVVT6",                                # Consumer Key
                                "F0FK9sOkOD3DmOMOivPESfQP2Vx6da2addUE0FApd1qVurtybK")   # Consumer Secret
auth2.set_access_token("886035091448893442-hOwTGGgxrbWyO72GQPI48I9WBkCVhsd",            # Access token
                          "Vb2iNiH266zAwYr6J8iNLEflS4h8JS8KlUY6JbPFoOCun")              # Access Secret

curr_auth = auth2


def connect():
    global api
    api = tweepy.API(curr_auth)