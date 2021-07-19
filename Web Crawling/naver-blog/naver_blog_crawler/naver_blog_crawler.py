import chromedriver_autoinstaller
from selenium import webdriver
import time
import re

import pandas as pd

from multiprocessing import Pool

CHROME_VER = chromedriver_autoinstaller.get_chrome_version().split('.')[0]
BASE_DRIVER_PATH = f'./{CHROME_VER}/chromedriver.exe'

options = webdriver.ChromeOptions()
options.add_argument('headless')

URL_LIST = list()
TITLE_LIST = list()
CONTENT_LIST = list()
COMMENT_LISt = list()

try:
    driver = webdriver.Chrome(f"{BASE_DRIVER_PATH}", chrome_options=options)
except:
    chromedriver_autoinstaller.install(True)
    driver = webdriver.Chrome(f"{BASE_DRIVER_PATH}", chrome_options=options)


def get_num(text):
    result = re.sub('[^0-9]', '', text)

    return result


def get_url(keyword):
    url_list = []
    url = f'https://section.blog.naver.com/Search/Post.naver?pageNo=1&rangeType=ALL&orderBy=sim&keyword={keyword}'

    driver.get(url)
    driver.implicitly_wait(2)

    blog_no = driver.find_element_by_xpath('//*[@id="content"]/section/div[1]/div[2]/span/span/em')
    max_page_no = int(get_num(blog_no.text)) // 7

    for page in range(1, max_page_no):
        url = f"https://section.blog.naver.com/Search/Post.naver?pageNo={page}" \
              f"&rangeType=ALL&orderBy=sim&keyword={keyword}"
        driver.get(url)
        driver.implicitly_wait(2)

        for blog_no in range(1, 8):
            titles = driver.find_element_by_xpath(f'/html/body/ui-view/div/main/div/div/section/div[2]/div[{blog_no}]'
                                                  f'/div/div[1]/div[1]/a[1]')
            blog_url = titles.get_attribute('href')
            url_list.append(blog_url)

    print(f"총 {len(url_list)}개의 url 수집 완료")

    return url_list


def get_content(link):
    driver.get(link)
    driver.implicitly_wait(2)

    try:
        driver.switch_to.frame('mainFrame')
        overlays = ".se-fs-.se-ff-"
        title = driver.find_element_by_css_selector(overlays)
        title_text = title.text

        overlays = ".se-component.se-text.se-l-default"
        content = driver.find_element_by_css_selector(overlays)
        content_text = content.text

        comment_info = driver.find_element_by_css_selector('em#commentCount')
        comment_count = comment_info.text

        comment_list = ""
        if not comment_count:
            pass
        else:
            comment_info.click()
            comments = driver.find_elements_by_css_selector('span.u_cbox_contents')
            for comment in comments:
                comment_list += comment.text

        print(f"{link} 데이터 수집 완료")

        return [link, title_text, content_text, comment_list]
    except:
        print(f"에러 발생{link}")


def to_csv():
    blog_text_df = pd.DataFrame({
        'url' : URL_LIST,
        'title' : TITLE_LIST,
        'content' : CONTENT_LIST,
        'comment' : COMMENT_LISt
    })

    blog_text_df.to_csv(
        f'naver_blog_data{len(blog_text_df)}.csv',
        header=True,
        index=True,
        encoding='utf-8-sig'
    )


if __name__ == '__main__':
    start_time = time.time()
    pool = Pool(processes=2)

    for blog_info in pool.map(get_content, get_url('NLP')):
        if not blog_info:
            pass
        else:
            URL_LIST.append(blog_info[0])
            TITLE_LIST.append(blog_info[1])
            CONTENT_LIST.append(blog_info[2])
            COMMENT_LISt.append(blog_info[3])

    print("--- %s seconds ---" % (time.time() - start_time))
    to_csv()
    print("finish!!")
