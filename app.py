from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options


chrome_options = Options()
chrome_options.add_argument("--window-size=1920,1080")

driver_path = '/home/nawodya_Dark/Third_party/chrome_Driver/chromedriver'

driver = webdriver.Chrome(executable_path=driver_path, chrome_options=chrome_options)

driver.get('https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0')


singnin_btn = driver.find_element_by_link_text('Sign in')
singnin_btn.click()

time.sleep(1)

user_name = driver.find_element_by_name('session_key')
user_name.send_keys('nawodyahckr@gmail.com')

password = driver.find_element_by_name('session_password')
password.send_keys('PASSWORD')
time.sleep(2)

singnin = driver.find_element_by_xpath('//*[@id="organic-div"]/form/div[3]/button')
singnin.click()

time.sleep(3)
easy_apply_btn = driver.find_element_by_class_name('jobs-apply-button')
easy_apply_btn.click()

time.sleep(4)
next_btn = driver.find_element_by_css_selector('footer button')
next_btn.click()

time.sleep(1)
next_btn = driver.find_element_by_css_selector('footer button')
next_btn.click()
