import TwitterConnectionAPI as tca

training_users_identifiers = [
    "freddy_e",
    "introverted_dad",
    "goingunder248",
    "brokensoul_12",
    "BeyondBrokenDep"
]

def get_users():
    epochs = 10

    if not tca.is_connected():
        tca.connect()
    original = list(map(lambda identifier: tca.api.get_user(identifier), training_users_identifiers))
    users = original
    for i in range(epochs - 1):
        users.extend(original)
    return users