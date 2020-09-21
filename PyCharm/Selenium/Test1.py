from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")

driver = webdriver.Chrome(options=chrome_options, executable_path=r'C:\Users\techies\Desktop\CodingProjects\Selenium\Drivers\chromedriver.exe')
driver.get("https://www.google.com")
lucky_button = driver.find_element_by_css_selector("[name=btnI]")
lucky_button.click()

driver.get_screenshot_as_file(r"C:\Users\techies\Desktop\CodingProjects\Random Sh_t\capture.png")