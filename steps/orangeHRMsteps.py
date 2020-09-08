from behave import *
from selenium import webdriver

@given(u'launch chrome webrowser')
def launch_browser(context):
    raise NotImplementedError(u'STEP: Given launch chrome webrowser')

@when(u'open OrangeHRM homepage')
def open_homepage(context):
    raise NotImplementedError(u'STEP: When open OrangeHRM homepage')

@then(u'verify that logo is present in the page')
def check_logo(context):
    raise NotImplementedError(u'STEP: Then verify that logo is present in the page')

@then(u'close browser')
def close_browser(context):
    raise NotImplementedError(u'STEP: Then close browser')