import re

email = 'b.shvets@temabit.com'


def hide_email(string):

    if string.__contains__('@'):
        match = re.split('[@]', string)
        name = match[0]
        pattern = name[3:-1]
        replacement = '*'*len(pattern)
        if len(name) >= 5:
            name = re.sub(pattern, replacement, name)
            print(name + '@' + match[1])
        else:
            print("Email name is too short.")
    else:
        print("Given string is not an email.")


hide_email(email)
