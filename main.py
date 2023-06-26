from selenium import webdriver
from selenium.webdriver.chrome.options import Options


chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

chrome_driver_path = "/Users/ethanwilliams/Development/chromedriver_mac_arm64/chromedriver"
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.amazon.com/")
# driver.quit()
