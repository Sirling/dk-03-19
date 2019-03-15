import re

list_of_emails = {'back@gmail.com', 'thun.311@gmail.com', 'back321@gmail.com', '123back@gmail.com', 'backagmail.com',
                  '12.back@gmail.com', 'back@gmail.com132', 'back@gmail.com', 'back@gmail123.com', 'backgmailcom'}


def verification(list_input):

    result_list = list()
    for x in list_input:
        if isinstance(x, str):
            match = re.search(r'[\w._+-]+@[\w._+-]+\.[\w]{1,11}', x)
            if match is not None:
                result_list.append(match[0])
    return result_list


print(verification(list_of_emails))
