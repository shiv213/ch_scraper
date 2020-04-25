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
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'no-cache',
    'content-length': '583',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'cookie': 'root_session_id=elfabj7oumm5mk15voov9r1ei3; G_ENABLED_IDPS=google; __zlcmid=x9iyNB2ak03n5F; visid_incap_987752=IC/xCAsARvaxwzOm17kd32F0al4AAAAAQUIPAAAAAADfN8RsKEYE3iccX8LPcPry; device_view=full; incap_ses_210_987752=trCLATvp/Dxbqv4h+BHqApVBo14AAAAAEm0p6gIbrFeOhUJxvDOFJw==; has_called_TBM=1; nlbi_987752=9ApJH9au9E7AkJV/5Tz1lQAAAABNfu4ijJpDvFBwgOEtkPFw; growth_restrict_views_v5=%7B%2204%2020%22%3A%7B%221i7bau%22%3A1%7D%7D; recently_viewed_docs=41116349; has_seen_mcq=yes; qualaroo_doc_visited=true; qualaroo_register_visited=false; covid19_bucket_student=0; full_name=Shiv Trivedi; email=shiv.v.trivedi@gmail.com; qualaroo_loggedin=true; incap_ses_1213_987752=x3pLadARkSOW/haLF3LVEHBJo14AAAAAQqo+N5jGv7strrE8eU8a1g==; incap_ses_469_987752=HXWIQ2Pe/VtQ8FLgOzqCBkhMo14AAAAARPk6gutXufcYrag01ccIDg==; PHPSESSID=15tvnk0lc00m3i89cftooqlkk2; incap_ses_223_987752=kUD9Io7VXlJjNL8zVkEYA9Wbo14AAAAAPzUQ9Jes9BFxcfn4yZ4WyA==; incap_ses_119_987752=3NKeBVZMoyvuZTtMDcemAdabo14AAAAAtKUIWIuboY0IUGbH8VJCmA==; incap_ses_889_987752=WkmSaA9z2gL2cDfl/11WDNabo14AAAAAiHGjErW6aPBA0c7pvdxZHA==; __cfduid=d2d1fd3c12e48444dbdfc6cb51ea24f291587780570',
    'dnt': '1',
    'origin': 'https://www.coursehero.com',
    'pragma': 'no-cache',
    'referer': 'https://www.coursehero.com/login/?ref=login',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest'
}

headers1 = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36'
}

headers3 = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'no-cache',
    'cookie': 'PHPSESSID=q59sf515eeukglf1nhk4vmksl6; device_view=full; root_session_id=q59sf515eeukglf1nhk4vmksl6; nlbi_987752=VANdB5AL8TnJnDFy5Tz1lQAAAADikuTEKfzwHKd9XP5MrC6D; visid_incap_987752=q1NAT3UiQI61ZrqcRoROSUKdo14AAAAAQUIPAAAAAADr5TOyLdpjicwiOxI6BEj+; incap_ses_1178_987752=1+0jBtFCfg81CUyRYBlZEEKdo14AAAAA4uEaK2Ez0RrNG37V9S901g==; incap_ses_168_987752=qH5wSttoE0ctg+USP9tUAkOdo14AAAAAYpLGiD0HmgnAx8YqEYyRIQ==; incap_ses_481_987752=yDwXCXevOGlZeCN7ztusBkOdo14AAAAAJiQVFDaeHgu7GWWcVewmuA==; has_called_TBM=1; incap_ses_985_987752=o7F8YO57nA2lj0kTXW2rDVOdo14AAAAAdiEpFxkzgq6jiZzCdglGiA==; G_ENABLED_IDPS=google; userID=100000801725775; ch_logged_in=1; userEmail=importanthacked%40gmail.com; supportEmail=importanthacked%40gmail.com; has_successfully_logged_in_the_past=1; remember_me=100000801725775%7C%7CdEIBt9mdUOyihdLzRgacMnUVh3P2iNSw; has_seen_payment_page=true; show_qualaroo_survey=true; incap_ses_119_987752=PE1UEmwC7WhAf0VMDcemAZKio14AAAAAhitQgnWtBTe3VFXwyB39rw==; __cfduid=d1c599596b3ffd3dfd35238ffe5bb294f1587782291; incap_ses_889_987752=6r+5fylP7TZZlkDl/11WDJKio14AAAAAufJLodtYkKi/XSNT98HNsg==; incap_ses_223_987752=5Yd0EzhKBBFeD8czVkEYA/qmo14AAAAAF1y4UAm0OEbrJVWjy5xhbg==',
    'dnt': '1',
    'pragma': 'no-cache',
    'referer': 'https://www.coursehero.com/home/',
    'sec-fetch-dest': 'ocument',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
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
    response = s.get(url, headers=headers1)
    # print(response.text)
    # soup = BeautifulSoup(response.content, 'html5lib')
    with open('cookies.json') as f:
        cookie_list: list = json.load(f)
        # create the cookie jar from the first cookie
        cookie_jar = requests.utils.cookiejar_from_dict(stringify(cookie_list[0]))
        # append the rest of the cookies
        for cookie in cookie_list[1:]:
            requests.utils.add_dict_to_cookiejar(cookie_jar, stringify(cookie))
        s.cookies = cookie_jar
    response = s.post('https://www.coursehero.com/ajax/login.php', data=login_data, headers=headers1, cookies=cookie_jar)
    print(response.text)
    with open('cookies2.json') as f:
        cookie_list: list = json.load(f)
        # create the cookie jar from the first cookie
        cookie_jar = requests.utils.cookiejar_from_dict(stringify(cookie_list[0]))
        # append the rest of the cookies
        for cookie in cookie_list[1:]:
            requests.utils.add_dict_to_cookiejar(cookie_jar, stringify(cookie))
        s.cookies = cookie_jar
    response = s.get('https://www.coursehero.com/home/', headers=headers3, cookies=cookie_jar)
    print(response.text)
