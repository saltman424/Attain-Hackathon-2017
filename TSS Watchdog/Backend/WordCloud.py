import re

import TwitterConnectionAPI as tca


class WordCloud:
    total_count = 0
    min_length = 3

    def __init__(self, text=None):
        self.word_counts = dict()
        if text is not None:
            self.add_words_from(text)

    def add_words_from(self, text):
        for word in re.sub("[^\w]", " ", text).split():
            self.add(word)

    def add(self, word, count=1):
        if self.valid_word(word):
            word = word.lower()
            if word not in self.word_counts:
                self.word_counts[word] = 0
            self.word_counts[word] += count
            self.total_count += count

    def similarity_to(self, other):
        similarity = 1.0
        for word in self.word_counts.keys():
            our_frequency = self.word_counts[word] / self.total_count
            their_frequency = (0 if other.total_count == 0 or word not in other.word_counts else other.word_counts[word] / other.total_count)
            similarity -= abs(our_frequency - their_frequency)
        print(similarity)
        return similarity

    def load(self, file_name):
        load_file = open(file_name, "r", encoding="utf-8")
        self.word_counts, self.total_count = json_string_to_word_counts_and_total(load_file.read())
        return self

    def save_as(self, file_name):
        save_file = open(file_name, "w", encoding="utf-8")
        save_file.write(word_counts_to_json_string(self.word_counts))

    def reduce_noise(self):
        min_frequency = 0.01
        orig_total_count = self.total_count
        print(str(orig_total_count) + " // " + str(1 / min_frequency))
        if orig_total_count > 0:
            for word in list(self.word_counts.keys()):
                if self.valid_word(word) or self.word_counts[word] / orig_total_count < min_frequency:
                    self.total_count -= self.word_counts.pop(word, 0)

    def valid_word(self, word):
        return len(word) > self.min_length

    def train_on_twitter_user(self, user, cleanup_afterwards=False):
        if not tca.is_connected():
            tca.connect()
        tweets = tca.get_tweets_from(user)
        for tweet in tweets:
            self.add_words_from(tweet.text)
        if cleanup_afterwards:
            self.reduce_noise()



def word_counts_to_json_string(word_counts):
    json_string = "{\n"
    is_first_word = True
    for word in word_counts.keys():
        if is_first_word:
            is_first_word = False
        else:
            json_string += ",\n"
        json_string += "\t\"" + word + "\": " + str(word_counts[word])
    json_string += "\n}"
    return json_string


def json_string_to_word_counts_and_total(json_string):
    total_count = 0
    word_counts = dict()
    word = ""
    count_string = ""
    reading_word = False
    reading_number = False
    for char in json_string:
        if char == '"':
            if reading_word:
                reading_word = False
            else:
                reading_word = True
        elif char == ':':
            reading_number = True
        elif char == ',':
            reading_number = False
            count = int(count_string)
            word_counts[word] = count
            total_count += count
            word = ""
            count_string = ""
        elif reading_word:
            word += char
        elif reading_number and char.isdigit():
            count_string += char
    return word_counts, total_count