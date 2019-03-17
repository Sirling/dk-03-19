import re

hidden_email = 'b.s**********s@temabit.com'

def hidden_email_verification(email):

    match = re.match('[\w._+-]{0,3}[*]+[\w._+-]{1}@[\w._+-]+\.[\w]{1,11}', email)
    if match is not None:
        print('Success!\n', match[0])
    else:
        print("Epic fail :)")

hidden_email_verification(hidden_email)