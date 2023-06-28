from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

chrome_driver_path = "/Users/ethanwilliams/Development/chromedriver_mac_arm64/chromedriver"
driver = webdriver.Chrome(options=chrome_options)
# driver.get("https://www.python.org/")

# driver_container = {}

# date = driver.find_elements(By.CLASS_NAME,"menu li time")
# event = driver.find_elements(By.CLASS_NAME,"event-widget li a")

# for idx, item in enumerate(event):
#     # driver_container[item.text] = date[idx].text
#     driver_container[idx] = {
#         "time": date[idx].text,
#         "event": item.text,
#     }

# print(driver_container)

driver.get("https://orteil.dashnet.org/experiments/cookie/")

items = driver.find_elements(By.CLASS_NAME, "grayed")
item_ids = [item.get_attribute("id") for item in items]
print(item_ids)



timeout = time.time() + 5
five_min = time.time() + (60*5)

while True:
  driver.find_element(By.ID, "cookie").click()
  if time.time() > timeout:

    prices = driver.find_elements(By.CSS_SELECTOR, "#store b")
    cookie_count = int(driver.find_element(By.ID, "money").text.replace(",", ""))
    item_prices = []

    print(prices)
    for price in prices:
      if price.text != "":
        price = int(price.text.split("- ")[1].split("\n")[0].replace(",", ""))
        item_prices.append(price)
    print(item_prices)
    cookie_upgrades = {}

    for idx, price in enumerate(item_prices):
      cookie_upgrades[price] = idx

    print(cookie_upgrades.items())
    affordable_upgrades = {}

    for cost, idx in cookie_upgrades.items():
      if int(cookie_count) > cost:
        affordable_upgrades[cost] = idx

    print(affordable_upgrades)

    highest_affordable_upgrade = max(affordable_upgrades)
    print(highest_affordable_upgrade)
    to_purchase_id = affordable_upgrades[highest_affordable_upgrade]
    print(to_purchase_id)
    print(item_ids[to_purchase_id])

    driver.find_element(By.ID, f"{item_ids[to_purchase_id]}").click()

    timeout = time.time() + 5

  if time.time() > five_min:
    cookie_per_s = driver.find_element(By.ID, "cps").text
    print(cookie_per_s)
    break


# driver.quit()

