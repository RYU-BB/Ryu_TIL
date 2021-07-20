import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from tqdm import tqdm
import time
import re

import pandas as pd

from multiprocessing import Pool

CHROME_VER = chromedriver_autoinstaller.get_chrome_version().split('.')[0]
BASE_DRIVER_PATH = f'./{CHROME_VER}/chromedriver.exe'

for _ in range(3):
    options = Options()
    options.add_argument('headless')
    # options.add_argument("--proxy-server=socks5://127.0.0.1:9150")
    options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/91.0.4472.124 Safari/537.36")
    options.add_argument(
        "app-version=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/91.0.4472.124 Safari/537.36")

CHECK_POINT = 560
CRAWLING_FLAG = True

URL_LIST = list()
TITLE_LIST = list()
CONTENT_LIST = list()
COMMENT_LISt = list()
FAIL_URL_LIST = list()

try:
    driver = webdriver.Chrome(f"{BASE_DRIVER_PATH}", chrome_options=options)
except:
    chromedriver_autoinstaller.install(True)
    driver = webdriver.Chrome(f"{BASE_DRIVER_PATH}", chrome_options=options)


def get_num(text):
    result = re.sub('[^0-9]', '', text)

    return result


def get_url(keyword):
    global CHECK_POINT, CRAWLING_FLAG

    url_list = []
    max_page_no = 572

    for page in range(1, max_page_no):
        url = f"https://section.blog.naver.com/Search/Post.naver?pageNo={page}" \
              f"&rangeType=ALL&orderBy=sim&keyword={keyword}"
        driver.get(url)
        driver.implicitly_wait(2)

        for blog_no in range(1, 8):
            try:
                titles = driver.find_element_by_xpath(f'/html/body/ui-view/div/main/div/div/section/div[2]/div[{blog_no}]'
                                                      f'/div/div[1]/div[1]/a[1]')
                blog_url = titles.get_attribute('href')
                url_list.append(blog_url)
            except:
                print("url 수집 중 에러발생")
                time.sleep(2)

        if not page % 10:
            print(f'url{page}개 수집완료')

    print(f"총 {len(url_list)}개의 url 수집 완료")

    return url_list


def get_content(link):
    driver.get(link)
    driver.implicitly_wait(2)
    error_count = 0
    try:
        driver.switch_to.frame('mainFrame')
        overlays = ".se-fs-.se-ff-"
        title = driver.find_element_by_css_selector(overlays)
        title_text = title.text

        overlays = ".se-component.se-text.se-l-default"
        content = driver.find_element_by_css_selector(overlays)
        content_text = content.text

        # comment_info = driver.find_element_by_css_selector('em#commentCount')
        # comment_count = comment_info.text
        #
        # comment_list = ""
        # if not comment_count:
        #     pass
        # else:
        #     comment_info.click()
        #     comments = driver.find_elements_by_css_selector('span.u_cbox_contents')
        #     for comment in comments:
        #         comment_list += comment.text

        print(f"{link} 데이터 수집 완료")

        return [link, title_text, content_text]
    except:
        error_count += 1
        FAIL_URL_LIST.append(link)
        print(f"에러 발생{link}")


def to_csv(keyword):
    blog_text_df = pd.DataFrame({
        'url': URL_LIST,
        'title': TITLE_LIST,
        'content': CONTENT_LIST,
    })

    blog_fail_df = pd.DataFrame({
        'fail_url': FAIL_URL_LIST
    })

    blog_text_df.to_csv(
        f'naver_blog_data{CHECK_POINT - 1}page_{keyword}.csv',
        header=True,
        index=True,
        encoding='utf-8-sig'
    )

    blog_fail_df.to_csv(
        f"naver_blog_fail_url{CHECK_POINT - 1}page_{keyword}.csv",
        header=True,
        index=True,
        encoding='utf-8-sig'
    )


if __name__ == '__main__':
    pool = Pool(processes=6)

    keyword_list = [
        '리뷰',
        '후기',
        '맛집',
        '연애',
        '결혼',
        '관광지',
        '코로나',
        '날씨',
        '꽃',
        '명소',
        '다이어트',
        '학교',
        '자격증',
        '라인',
        '학교',
        '주사',
        '성형',
        '교정',
        '여드름',
        '제주',
        '키보드',
        '마우스',
        '카페',
        '아이폰',
        '일상',
        '내돈내산',
        '웹툰',
        '리그오브레전드',
        '배그',
        '헤드셋',
        '로아',
        '서든어택',
        'NLP',
        '딥러닝',
        '이미지처리',
        '챗봇',
        '페르소나',
        '교감',
        '고양이',
        '멍멍이',
        '진돗개',
        '인공지능',
        '로꼬',
        '쇼미더머니',
        '릴보이',
        'aomg',
        '산이',
        '비와이',
        '마우스패드',
        '비트코인',
        '그래픽카드'
    ]
    for keyword in keyword_list:
        print(f'{keyword}키워드 크롤링 시작')
        for blog_info in tqdm(pool.map(get_content, get_url(keyword)), desc=f'{keyword}_crawling'):
            if not blog_info:
                pass
            else:
                URL_LIST.append(blog_info[0])
                TITLE_LIST.append(blog_info[1])
                CONTENT_LIST.append(blog_info[2])
                # COMMENT_LISt.append(blog_info[3])
        to_csv(keyword)

        if not CRAWLING_FLAG:
            break

        URL_LIST = []
        TITLE_LIST = []
        CONTENT_LIST = []
        FAIL_URL_LIST = []
            
        print(f'{keyword}키워드 크롤링 끝')
        CHECK_POINT = 1
        # COMMENT_LISt = []

