from WordCloud import WordCloud
import TweetClassifier as tc
import TwitterConnectionDetails as tcd


threshold_score = 0.1
basis_wordcloud = WordCloud().load("basis_wordcloud.json")


def is_suspicious(user):
    score = 0

    tweets = tcd.api.user_timeline(screen_name=user.screen_name, count=100)

    average_buzzword_results = average_buzzword_score(user, tweets)
    score += average_buzzword_results[0]

    #wordcloud_results = wordcloud_score(user, tweets)
    #score += wordcloud_results[0]
    for tweet in tweets:
        basis_wordcloud.add_words_from(tweet.text)
    basis_wordcloud.save_as("basis_wordcloud.json")

    return score >= threshold_score, score


def average_buzzword_score(user, tweets):
    total_score = 0
    for tweet in tweets:
        total_score += tc.buzzword_score(tweet.text)[0]
    return total_score / len(tweets), "Sorry no information to give right now"


def wordcloud_score(user, tweets):
    max_score = threshold_score

    wordcloud = WordCloud()
    for tweet in tweets:
        wordcloud.add_words_from(tweet.text)

    return max_score * basis_wordcloud.similarity_to(wordcloud), "Sorry no information to give right now"