def user_to_string(user):
    output = "["
    vals = 0
    if user.name is not None:
        output += "name = '" + user.name + "'"
        vals += 1
    if user.screen_name is not None:
        if vals > 0:
            output += ", "
        output += " screen_name = '" + user.screen_name + "', profile_url = https://twitter.com/" + user.screen_name
        vals += 1
    if user.url is not None:
        if vals > 0:
            output += ", "
        output += " url = " + user.url + ""
        vals += 1
    output += "]"
    return output
