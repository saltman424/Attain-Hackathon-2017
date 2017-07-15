import TweetProcessor as tp
from WordCloud import WordCloud


threshold_score = 3


def is_suspicious(status):
    score = 0

    buzzword_results = buzzword_score(status.text)
    score += buzzword_results[0]

    wordcloud_results = wordcloud_score(status.text)
    score += wordcloud_results[0]

    return score >= threshold_score, score


def buzzword_score(text):
    text = text.lower()

    # List of words or phrases that indicate a suspicious tweet
    #  (List is in disjunctive normal form)
    buzzwords = [
        [["kill myself"],5],
        [["hurt"],1],
        [["hate"],1],
        [["pain"],2],
        [["depress"],4], # handles depressed or depression, or other variants
        [["make", "pay"],4],
        [["suicid"],2],
        [["better","dead"],6],
        [["bullied"],2],
        [["feel","trapped"],4],
        [["anger"],1],
        [["angry"],2],
        [["deserve"], 1],
        [["abuse"],2],
        [["no","reason","live"],5],
        [["want","dead"],3],
        [["wish","dead"],3],
        [["feel","empty"],4],
        [["empty inside"],6],
        [["feel","worthless"],3],
        [["end","life"],5],
        [["want","escape"],1],
        [["miss","so","much"],3],
        [["feel","lonely"],3],
        [["burden","others"],3],
        [["cut","myself"],1],
        [["cut","wrist"],3],
        [["lonely"],1],
        [["I "],0.5],
        [[" me"],0.5],
        [["myself"],0.5],
        [["again"],1],

        [["clinton"],-2],
        [["trump"],-2],
        [["politic"],-2],
        [["democrat"],-2],
        [["republic"],-2],
        [[" bot "], -2],
        [["govern"], -2]
    ]

    suspicious_series = []

    score = 0
    for series in buzzwords:
        suspicious = True
        for buzzword in series[0]:
            if buzzword not in text:
                suspicious = False
        if suspicious:
            suspicious_series.append(series[0])
            score += series[1]
    return score,suspicious_series


def wordcloud_score(text):
    text.lower()

    max_score = 3 * threshold_score
    wordcloud = WordCloud(text)
    return max_score * wordcloud.similarity_to(tp.basis_wordcloud),"Sorry no information to give right now"