from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

@given(u'I am on the login page')
def launchBrowser(context):
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    context.driver = webdriver.Chrome(options=chrome_options)
    context.driver.get("https://app.jubelio.com/login")

@when(u'I enter my correct email and password ("{email}" and "{password}")')
def inputCredentials(context,email,password):
    context.elem = context.driver.find_element(By.NAME, "email")
    context.elem.clear()
    context.elem.send_keys(email)

    context.elem = context.driver.find_element(By.NAME, "password")
    context.elem.clear()
    context.elem.send_keys(password)

@when(u'I click on the login button')
def step_impl(context):
    context.elem.send_keys(Keys.RETURN)

@then(u'I should be redirected to the dashboard')
def step_impl(context):
    sleep(3)
    context.driver.close()
