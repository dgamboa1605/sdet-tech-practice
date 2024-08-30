from behave import given, when, then
from core.pages.login_page import LoginPage
from config.config import Config
import allure

@given('I am on the login page')
@allure.step("Go to Login Page")
def step_given_i_am_on_the_homepage(context):
    context.page = context.browser.new_page()
    context.login_page = LoginPage(context.page)
    context.login_page.navigate(Config.BASE_URL)

@when('I login with valid credentials')
@allure.step("Logging with valid credentials")
def step_when_i_log_in_with_valid_credentials(context):
    context.login_page.login(Config.USERNAME, Config.PASSWORD)

@when('I login with invalid credentials')
@allure.step("Logging with invalid credentialsd")
def step_when_i_log_in_with_invalid_credentials(context):
    context.login_page.login("user1", "userpass")

@then('I should see the inventory page')
@allure.step("Check if the page is as expected")
def step_then_i_should_see_the_inventory_page(context):
    assert context.page.url == Config.BASE_URL + "/inventory.html"

@then('I should see an error message "{expected_title}"')
@allure.step("Check if the error message is displayed")
def step_then_i_should_see_error_message(context, expected_title):
    actual_title = context.login_page.get_error_message()
    assert  expected_title in actual_title, f"Expected title '{expected_title}', but got '{actual_title}'"
