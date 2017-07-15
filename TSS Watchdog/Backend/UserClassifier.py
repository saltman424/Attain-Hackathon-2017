import TweetClassifier as tc
import TwitterConnectionAPI as tca
import TweetProcessor as tp
from WordCloud import WordCloud

threshold_score = 0.2


def is_suspicious(user):

    score = 0

    tweets = tca.get_tweets_from(user)
    if tweets is None:
        return False, None

    average_buzzword_results = average_buzzword_score(user, tweets)
    score += average_buzzword_results[0]

    wordcloud_results = wordcloud_score(user, tweets)
    score += wordcloud_results[0]

    average_sentiment_results = average_sentiment_score(user, tweets)
    score += average_sentiment_results[0]

    return score >= threshold_score, score


def average_buzzword_score(user, tweets):
    total_score = 0

    for tweet in tweets:
        total_score += tc.buzzword_score(tweet.text)[0]

    return total_score / len(tweets), "Sorry no information to give right now"


def wordcloud_score(user, tweets):
    max_score = 2 * threshold_score

    wordcloud = WordCloud()
    for tweet in tweets:
        wordcloud.add_words_from(tweet.text)

    return max_score * wordcloud.similarity_to(tp.basis_wordcloud), "Sorry no information to give right now"

def average_sentiment_score(user, tweets):
    total_score = 0

    for tweet in tweets:
        total_score += tc.sentiment_score(tweet.text)[0]

    return total_score / len(tweets), "Sorry no information to give right now"


def profile_nn_score(user):
    return 0