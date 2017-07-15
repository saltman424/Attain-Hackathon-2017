import time

import TweetScanner as ts
import TweetProcessor as tp
import TrainingData as trainer


normal = 1
training = 2

run_type = training




# Actual execution:

if run_type == normal:
    api = ts.start()
    while ts.running():
        time.sleep(60)
elif run_type == training:
    users_to_train_on = trainer.get_users()
    for user in users_to_train_on:
        tp.train_basis_wordcloud_on(user)