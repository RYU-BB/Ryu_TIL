import chromedriver_autoinstaller
from selenium import webdriver

CHROME_VER = chromedriver_autoinstaller.get_chrome_version().split('.')[0]
BASE_DRIVER_PATH = f'./{CHROME_VER}/chromedriver.exe'
content_list = []

try:
    driver = webdriver.Chrome(f"{BASE_DRIVER_PATH}")
except:
    chromedriver_autoinstaller.install(True)
    driver = webdriver.Chrome(f"{BASE_DRIVER_PATH}")


driver.get("https://blog.naver.com/skyat23/222429861092")
driver.implicitly_wait(3)

driver.switch_to.frame('mainFrame')

test = driver.find_element_by_css_selector('em#commentCount')
print(test.text)
test.click()
test_comment = driver.find_elements_by_css_selector('span.u_cbox_contents')
for comment in test_comment:
    print(comment.text)

if not test:
    print("true")
else:
    print("false")