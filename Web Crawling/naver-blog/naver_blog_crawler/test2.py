from bs4 import BeautifulSoup
import requests
import time
import pandas as pd


def get_url(keyword):
    headers = {'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.146 Safari/537.36'
}

    url = f'https://section.blog.naver.com/Search/Post.naver?pageNo=1&rangeType=ALL&orderBy=sim&keyword={keyword}'

    data = requests.get(url, headers=headers)
    html = BeautifulSoup(data.text, "html.parser")

    print(html)



get_url("NLP")