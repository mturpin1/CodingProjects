from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# instantiate a chrome options object so you can set the size and headless preference
chrome_options = Options()
chrome_options.add_argument('--disable-extensions')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--headless')

driver = webdriver.Chrome(options=chrome_options, executable_path=r'C:\Users\techies\Desktop\CodingProjects\Selenium\Drivers\chromedriver.exe')

driver.get("https://www.google.com")
lucky_button = driver.find_element_by_css_selector("[name=btnI]")
lucky_button.click()

# capture the screen
driver.get_screenshot_as_file("capture.png")

driver.quit()