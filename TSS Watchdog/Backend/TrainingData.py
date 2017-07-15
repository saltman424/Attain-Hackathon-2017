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


def getNNData():
    sets_of_inputs = []
    sets_of_outputs = []
    for user in get_users():
        sets_of_inputs.append(getNNInputsFrom(user))
        sets_of_outputs.append([1])

def getNNInputsFrom(user):
    inputs = []
    inputs.append(1 if hasattr(user,"default_profile_image") and user.default_profile_image else 0)
    inputs.append(1 if hasattr(user,"profile_background_tile") and user.profile_background_tile else 0)
    inputs.append(1 if hasattr(user,"verified") and user.verified else 0)
    inputs.append(1 if hasattr(user,"default_profile_image") and user.default_profile_image else 0)
    inputs.append(1 if hasattr(user,"protected") and user.protected else 0)
    inputs.append(1 if hasattr(user,"has_extended_profile") and user.has_extended_profile else 0)
    inputs.append(1 if hasattr(user,"contributors_enabled") and user.contributors_enabled else 0)
    inputs.append(int(user.statuses_count) if hasattr(user,"statuses_count") else 0)
    inputs.append(int(user.favourites_count) if hasattr(user,"favourites_count") else 0)
    inputs.append(int(user.followers_count) if hasattr(user,"followers_count") else 0)
    inputs.append(int(user.friends_count) if hasattr(user,"friends_count") else 0)
    inputs.append(int(user.listed_count) if hasattr(user,"listed_count") else 0)
    inputs.append(int(user.profile_sidebar_border_color, 16) if hasattr(user,"profile_sidebar_border_color") else 0)
    inputs.append(int(user.profile_link_color, 16) if hasattr(user,"profile_link_color") else 0)
    inputs.append(int(user.profile_text_color, 16) if hasattr(user,"profile_text_color") else 0)
    inputs.append(int(user.profile_side_bar_fill_color, 16) if hasattr(user,"profile_side_bar_fill_color") else 0)
    inputs.append(int(user.profile_background_color, 16) if hasattr(user,"profile_background_color") else 0)