from selenium import webdriver
from behave import*
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@when('Enter usernaem "{user}" and password "{pwd}"')
def credintial(context,user,pwd):
    wait = WebDriverWait(context.driver, 20)

    username = wait.until( EC.visibility_of_element_located((By.XPATH, "//input[@name='username']")))
    
    username.clear()
    username.send_keys(user)

    password = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@name='password']")))


    password.clear()
    password.send_keys(pwd)   

@when('click on login button')
def loginbutton(context):
   
    context.driver.find_element(By.XPATH,"//button[normalize-space()='Login']").click()
    


@then('user must successfully login to the Dasboard Page')
def step_impl(context):
    context.driver.implicitly_wait(10)
    text=context.driver.find_element(By.XPATH,"//a[@class='oxd-main-menu-item active']").text
    assert text=="Dashboard"

   
