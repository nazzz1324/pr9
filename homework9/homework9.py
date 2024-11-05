import re

def split_email(email):
    #regular = r'^(?P<username>[^@]+)@(?P<domain>.+)$'
    regular = r'^(?P<username>[a-zA-Z][a-zA-Z0-9._%+-]*)@(?P<domain>[a-zA-Z][a-zA-Z0-9.-]+.[a-zA-Z]{2,})$'
    match = re.match(regular, email)

    if match:
        username = match.group('username')
        domain = match.group('domain')
        return username, domain
    else:
        return None, None

email = input("Введите email: ")
username, domain = split_email(email)

if username and domain:
    print(f"username: {username}, domain: {domain}")
else:
    print("Некорректный email")
