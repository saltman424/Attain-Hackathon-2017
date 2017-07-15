import UserClassifier as uc


threshold_score = 10


def is_suspicious(status):
    if is_suspicious_tweet(status):
        return uc.is_suspicious(status.user)
    else:
        return False


def is_suspicious_tweet(status):
    return buzzword_score(status.text) >= threshold_score


def buzzword_score(text):
    # List of words or phrases that indicate a suspicious tweet
    #  (List is in disjunctive normal form)
    buzzwords = [
        [["kill myself"],1],
        [["hurt"],1],
        [["hate"],1],
        [["pain"],1],
        [["depress"],1], # handles depressed or depression, or other variants
        [["make", "pay"],1],
        [["suicide"],1],
        [["better","dead"],1],
        [["bullied"],1],
        [["feel","trapped"],1],
        [["anger"],1],
        [["angry"],1],
        [["no","reason","live"],1],
        [["want","dead"],1],
        [["wish","dead"],1],
        [["feel","empty"],1],
        [["feel","worthless"],1],
        [["end","life"],1],
        [["want","escape"],1],
        [["miss","so","much"],1]
    ]
    for series in buzzwords:
        suspicious = True
        for buzzword in series:
            if buzzword not in text:
                suspicious = False
        if suspicious:
            output = "Suspicious words: "
            for word in series:
                output += word + " "
            print(output)
            return True
    return False