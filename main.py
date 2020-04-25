import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import json


def stringify(obj: dict) -> dict:
    """turn every value in the dictionary to a string"""
    for k, v in obj.items():
        if isinstance(v, dict):
            # if value is a dictionary, stringifiy recursively
            stringify(v)
            continue
        if not isinstance(v, str):
            if isinstance(v, bool):
                # False/True -> false/true
                obj[k] = str(v).lower()
            else:
                obj[k] = str(v)
    return obj


headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36'
}

login_data = {
    'email': 'importanthacked@gmail.com',
    'password': 'testing123',
    'submit': 'true',
    'remember_me': '1'
}

with requests.Session() as s:
    url = 'https://www.coursehero.com/login/'
    response = s.get(url, headers=headers)
    # print(response.content)
    # soup = BeautifulSoup(response.content, 'html5lib')
    with open('cookies.json') as f:
        cookie_list: list = json.load(f)
        # create the cookie jar from the first cookie
        cookie_jar = requests.utils.cookiejar_from_dict(stringify(cookie_list[0]))
        # append the rest of the cookies
        for cookie in cookie_list[1:]:
            requests.utils.add_dict_to_cookiejar(cookie_jar, stringify(cookie))
        s.cookies = cookie_jar
    response = s.post('https://www.coursehero.com/ajax/login.php', data=login_data, headers=headers, cookies=cookie_jar)
    print(response.text)
