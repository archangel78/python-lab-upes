import requests
import re

class InvalidAccountError(Exception):
    def __init__(self, account):
        super().__init__(account+" is not a valid github account")

account = input("Enter github account username: ")

try:
    req = requests.get("https://www.github.com/"+account)
    if(req.status_code==404):
        raise InvalidAccountError(account)
    else:
        title = (re.search("<title>(.*)</title>",req.text)).group(1)
        name = (re.search("\((.*)\)",title)).group(1)
        print("Name of the user is: "+name)

except InvalidAccountError:
    print("The account provided is not a valid github account")  