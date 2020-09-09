from behave import *
from selenium import webdriver

@given(u'launch chrome webrowser')
def launch_browser(context):
    context.driver = webdriver.Chrome()

@when(u'open OrangeHRM homepage')
def open_homepage(context):
    context.driver.get('https://opensource-demo.orangehrmlive.com/')

@then(u'verify that logo is present in the page')
def check_logo(context):
    status = context.driver.find_element_by_xpath("//*[@id='divLogo']/img").is_displayed()
    assert status is True

@then(u'close browser')
def close_browser(context):
    context.driver.close()