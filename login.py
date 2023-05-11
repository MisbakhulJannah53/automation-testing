from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Connect to Chrome using Chrome Driver
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://app.jubelio.com/login")
# assert "Python" in driver.title
elem = driver.find_element(By.NAME, "email")
elem.clear()
elem.send_keys("qa.rakamin.jubelio@gmail.com")

elem = driver.find_element(By.NAME, "password")
elem.clear()
elem.send_keys("Jubelio123!")
elem.send_keys(Keys.RETURN)
sleep(5)
# assert "No results found." not in driver.page_source
driver.close()