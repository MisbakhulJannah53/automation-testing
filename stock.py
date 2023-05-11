from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains


# Connect to Chrome using Chrome Driver
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
actionChains = ActionChains(driver)

driver.get("https://app.jubelio.com/login")
# assert "Python" in driver.title
elem = driver.find_element(By.NAME, "email")
elem.clear()
elem.send_keys("qa.rakamin.jubelio@gmail.com")

elem = driver.find_element(By.NAME, "password")
elem.clear()
elem.send_keys("Jubelio123!")
elem.send_keys(Keys.RETURN)
sleep(3)

elem = driver.find_element(By.XPATH, "//*[@id='wrapper']/nav/div/div/ul/li[2]/a").click()
sleep(0.5)
elem = driver.find_element(By.XPATH, "//*[@id='wrapper']/nav/div/div/ul/li[2]/ul/li[2]/a").click()
sleep(1)
elem = driver.find_element(By.XPATH, "//*[@id='page-wrapper']/div[3]/div/div/div/div[2]/div/div/div/div/div/div[1]/div[2]/div/button[2]").click()
sleep(0.5)
elem = driver.find_element(By.NAME, "note")
elem.send_keys("Stock baju wanita dengan type long dress")
sleep(0.5)
elem = driver.find_element(By.XPATH, "//*[@id='page-wrapper']/div[3]/div/div/div/div[2]/div/div/div/div/div[1]/div/div[1]/div[2]/div[3]/div/div/div/div/span/a/i")
if elem:
    elem.click()

elem = driver.find_element(By.XPATH, "//*[@id='page-wrapper']/div[3]/div/div/div/div[2]/div/div/div/div/div[1]/div/div[1]/div[2]/div[3]/div/div")
elem.click()
sleep(0.1)
elem = driver.find_element(By.XPATH, "//*[@id='page-wrapper']/div[3]/div/div/div/div[2]/div/div/div/div/div[1]/div/div[1]/div[2]/div[3]/div/div/div[2]/div[2]/div[3]")
elem.click()
sleep(0.5)

elem = driver.find_element(By.XPATH, "//*[@id='page-wrapper']/div[3]/div/div/div/div[2]/div/div/div/div/div[1]/div/div[2]/div/div/div[2]/div/div[2]/div/div/div[2]/div/div/div[2]/div/div/div[1]/div")
actionChains.double_click(elem).perform()
sleep(1)
elem = driver.find_element(By.XPATH, "//*[@id='page-top']/div[6]/div/div/div[2]/div[2]/div[3]")
elem.click()
sleep(0.1)
elem = driver.find_element(By.XPATH, "//*[@id='page-wrapper']/div[3]/div/div/div/div[2]/div/div/div/div/div[3]/div/button")
# elem.click()
driver.execute_script("arguments[0].click();", elem)
sleep(5)
# driver.implicitly_wait(1)
# assert "No results found." not in driver.page_source
driver.close()
# //*[@id="wrapper"]/nav/div/div/ul/li[2]/a