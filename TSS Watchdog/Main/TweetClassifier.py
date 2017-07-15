import UserClassifier as uc


threshold_score = 2


def is_suspicious(status):
    if is_suspicious_tweet(status):
        return uc.is_suspicious(status.user)
    else:
        return False


def is_suspicious_tweet(status):
    score = 0

    buzzword_results = buzzword_score(status.text)
    score += buzzword_results[0]

    return score >= threshold_score


def buzzword_score(text):
    # List of words or phrases that indicate a suspicious tweet
    #  (List is in disjunctive normal form)
    buzzwords = [
        [["kill myself"],8],
        [["hurt"],3],
        [["hate"],1],
        [["pain"],2],
        [["depress"],5], # handles depressed or depression, or other variants
        [["make", "pay"],4],
        [["suicide"],2],
        [["better","dead"],6],
        [["bullied"],1],
        [["feel","trapped"],4],
        [["anger"],1],
        [["angry"],1],
        [["no","reason","live"],8],
        [["want","dead"],2],
        [["wish","dead"],2],
        [["feel","empty"],3],
        [["feel","worthless"],3],
        [["end","life"],5],
        [["want","escape"],1],
        [["miss","so","much"],3],
        [["feel","lonely"],3]
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