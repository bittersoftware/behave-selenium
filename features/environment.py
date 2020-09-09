# -- FILE: features/environment.py
from behave import fixture, use_fixture
from selenium import webdriver

@fixture
def selenium_driver_chrome(context):
    # -- HINT: @behave.fixture is similar to @contextlib.contextmanager
    context.driver = webdriver.Chrome()
    context.driver.get('https://opensource-demo.orangehrmlive.com/')
    yield context.driver
    # -- CLEANUP-FIXTURE PART:
    context.driver.quit()

def before_scenario(context, scenario):
    if "setup_scenario" in scenario.tags:
        use_fixture(selenium_driver_chrome, context)
        # -- HINT: CLEANUP-FIXTURE is performed after after_all() hook is called.

def after_scenario(context, scenario):
    if "teardown_scenario" in scenario.tags:
        context.driver.close()