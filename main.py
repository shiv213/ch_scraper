import requests
import urllib.request
import time
from bs4 import BeautifulSoup

with requests.Session() as s:
    url = 'https://www.coursehero.com/login/'
    response = s.get(url)
    print(response.content)
