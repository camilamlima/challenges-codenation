import re

REGEX = r"^([a-z0-9-._]+)@([a-z0-9]+)(\.[a-z]{1,3})+$"

def valid_email(email):
    check = re.match(REGEX, email)
    if check:
        return True
    else:
        return False

def filter_email(emails):
    
    return list(filter(valid_email, emails))