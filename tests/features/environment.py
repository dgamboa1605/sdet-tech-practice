from playwright.sync_api import sync_playwright
import allure

def before_all(context):
    context.playwright = sync_playwright().start()
    context.browser = context.playwright.chromium.launch(headless=True, args=['--start-maximized'])

def after_all(context):
    context.browser.close()
    context.playwright.stop()

def after_step(context, step):
    if step.status == "failed":
        allure.attach(
            context.page.screenshot(),
            name="screenshot",
            attachment_type=allure.attachment_type.PNG
        )
