from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

@given(u'User was login ("{email}" and "{password}") and the user on the dahboard page')
def launchBrowserAndLogin(context,email,password):
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    context.driver = webdriver.Chrome(options=chrome_options)
    context.actionChains = ActionChains(context.driver)
    context.driver.get("https://app.jubelio.com/login")

    context.elem = context.driver.find_element(By.NAME, "email")
    context.elem.clear()
    context.elem.send_keys(email)

    context.elem = context.driver.find_element(By.NAME, "password")
    context.elem.clear()
    context.elem.send_keys(password)

    context.elem.send_keys(Keys.RETURN)
    sleep(3)

@when(u'I click product item and the list from dropdown menu will be shown')
def step_impl(context):
    context.elem = context.driver.find_element(By.XPATH, "//*[@id='wrapper']/nav/div/div/ul/li[2]/a").click()
    sleep(0.5)

@when(u'I click persediaan menu then persediaan page will shown')
def step_impl(context):
    context.elem = context.driver.find_element(By.XPATH, "//*[@id='wrapper']/nav/div/div/ul/li[2]/ul/li[2]/a").click()
    sleep(1)

@when(u'I click inventory adjusment button')
def step_impl(context):
    context.elem = context.driver.find_element(By.XPATH, "//*[@id='page-wrapper']/div[3]/div/div/div/div[2]/div/div/div/div/div/div[1]/div[2]/div/button[2]").click()
    sleep(0.5)

@when(u'i fill the description')
def step_impl(context):
    context.elem = context.driver.find_element(By.NAME, "note")
    context.elem.send_keys("Stock baju wanita dengan type long dress")
    sleep(0.5)

@when(u'i select the location')
def step_impl(context):
    context.elem = context.driver.find_element(By.XPATH, "//*[@id='page-wrapper']/div[3]/div/div/div/div[2]/div/div/div/div/div[1]/div/div[1]/div[2]/div[3]/div/div/div/div/span/a/i")
    if context.elem:
        context.elem.click()
    sleep(1)

    context.elem = context.driver.find_element(By.XPATH, "//*[@id='page-wrapper']/div[3]/div/div/div/div[2]/div/div/div/div/div[1]/div/div[1]/div[2]/div[3]/div/div")
    context.elem.click()
    sleep(0.1)
    context.elem = context.driver.find_element(By.XPATH, "//*[@id='page-wrapper']/div[3]/div/div/div/div[2]/div/div/div/div/div[1]/div/div[1]/div[2]/div[3]/div/div/div[2]/div[2]/div[3]")
    context.elem.click()
    sleep(0.5)

@when(u'i select the name of product that i want to manage the stock')
def step_impl(context):
    context.elem = context.driver.find_element(By.XPATH, "//*[@id='page-wrapper']/div[3]/div/div/div/div[2]/div/div/div/div/div[1]/div/div[2]/div/div/div[2]/div/div[2]/div/div/div[2]/div/div/div[2]/div/div/div[1]/div")
    context.actionChains.double_click(context.elem).perform()
    sleep(1)
    context.elem = context.driver.find_element(By.XPATH, "//*[@id='page-top']/div[6]/div/div/div[2]/div[2]/div[3]")
    context.elem.click()
    sleep(0.1)
    context.elem = context.driver.find_element(By.XPATH, "//*[@id='page-wrapper']/div[3]/div/div/div/div[2]/div/div/div/div/div[3]/div/button")

@when(u'i click save button')
def step_impl(context):
    context.driver.execute_script("arguments[0].click();", context.elem)
    sleep(5)

@then(u'the stock of product success to manage')
def step_impl(context):
    context.driver.close()