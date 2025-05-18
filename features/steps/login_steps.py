from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helpers import wait_and_type, wait_and_click, assert_css_property

@given('I open the login page')
def step_open_login(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
    #https://www.saucedemo.com/cart.html
    context.wait = WebDriverWait(context.driver, 10)


@when('I enter valid credentials')
def step_enter_credentials(context):
    wait_and_type(context.driver, (By.XPATH, "//input[@name='username']"), 'Admin')
    wait_and_type(context.driver, (By.XPATH, "//input[@name='password']"), 'admin123')

@then('the login label should have correct CSS properties')
def step_validate_css(context):
    selector = 'label.oxd-label'
    expected_props = {
        'font-family': 'Nunito',
        'font-weight': '600',
        'font-size': '12px',
        'padding-top': '0px',
        'padding-left': '0px'
    }
    assert_css_property(context.driver, selector, expected_props)

@then('I click the login button')
def step_click_login(context):
    wait_and_click(context.driver, (By.XPATH, "//button[@type='submit']"))

@then('I should see the dashboard page')
def step_verify_dashboard(context):
    dashboard_header = context.wait.until(
        EC.visibility_of_element_located((By.XPATH, "//h6[text()='Dashboard']"))
    )
    assert dashboard_header.is_displayed(), 'Dashboard header not visible'
    context.driver.quit()