from selenium import webdriver
from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#from behave.api.pending_step import StepNotImplementedError
@given('launch chrome browser')
def launchbrowser(context):
    context.driver=webdriver.Chrome()

@when('open orange hrm homepage')
def openhomepage(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

   
@then('verify that the logo present on Page')
def veryfylogo(context):
    wait = WebDriverWait(context.driver, 10)
    logo = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='orangehrm-login-branding']//img")))
    
    status = logo.is_displayed()
    assert status is True

@then('close browser')
def closebrowser(context):
    context.driver.close()
