from selenium import webdriver
 
chromedriver = webdriver.Chrome(executable_path=r'C:\Users\techies\Desktop\CodingProjects\Selenium\Drivers')
 
# options = webdriver.ChromeOptions()
# options.add_argument('headless')
# options.add_argument('window-size=1200x600') # optional
 
browser = webdriver.Chrome(executable_path=chromedriver)
 
browser.get('https://www.duckduckgo.com')
 
browser.save_screenshot(executable_path=r'C:\Users\techies\Desktop\CodingProjects\Random Sh_t\test_2_screenshot.png')
 
browser.quit()