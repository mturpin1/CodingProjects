from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time 

driver = webdriver.Chrome(executable_path=r'C:\Users\techies\Desktop\CodingProjects\Selenium\Drivers\chromedriver.exe')

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--windows-size=1920x1080')

driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=driver)

driver.get('https://discord.com/login')

driver.find_element_by_name('email').send_keys('mjturp2@gmail.com')
driver.find_element_by_name('password').send_keys('//NoMmAROTsee1928//')
driver.find_element_by_name('password').send_keys(Keys.ENTER)

time.sleep(10)

driver.save_screenshot(r'C:\Users\techies\Desktop\CodingProjects\Random Sh_t\test_1_screenshot.png')

time.sleep(5)

driver.quit()