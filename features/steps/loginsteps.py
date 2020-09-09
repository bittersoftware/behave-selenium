from behave import *
from selenium import webdriver

@given(u'I launch Chrome Browser')
def launch_browser(context):
    context.driver = webdriver.Chrome()

@when(u'I open OrangeHRM Home Page')
def open_homepage(context):
    context.driver.get('https://opensource-demo.orangehrmlive.com/')


@when(u'Enter user name "{user}" and password "{password}"')
def enter_login_credentials(context, user, password):
    context.driver.find_element_by_id("txtUsername").send_keys(user)
    context.driver.find_element_by_id("txtPassword").send_keys(password)
    

@when(u'Click Login button')
def step_impl(context):
    context.driver.find_element_by_id("btnLogin").click()

@then(u'User must successfully login to the Dashboard page')
def step_impl(context):
    try:
        dashboard_text = context.driver.find_element_by_xpath("//h1[contains(text(),'Dashboard')]").text
    except:
        assert False,"Test Failed."
    else:
        if dashboard_text == "Dashboard":
            assert True,"Test Passed. Valid Credentials"
    context.driver.close()

@then(u'User must successfully login to the Dashboard page if credentials are "{valid}"')
def check_if_in_dashboard(context, valid):
    try:
        dashboard_text = context.driver.find_element_by_xpath("//h1[contains(text(),'Dashboard')]").text
    except:
        if valid == "False":
            assert True,"Test Passed. Invalid Credentials"
        else:
            assert False,"Test Failed. Invalid Credentials"
    else:
        if dashboard_text == "Dashboard":
            if valid == "True":
                assert True,"Test Passed. Valid Credentials"
            else:
                assert False,"Test Failed. Valid Credentials"    
    context.driver.close()