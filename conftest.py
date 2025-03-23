"""
Includes all necessary fixtures
Dependencies: playwright, faker, pytest
Author: Bhavana Murugan
Date: March 23, 2025
"""

import pytest
from playwright.sync_api import sync_playwright
from faker import Faker

@pytest.fixture(scope="function", params=["firefox", "webkit", "chromium"])
def browser(request):
    browser_type = request.param  # Get the browser type from the parameter
    with sync_playwright() as p:
        browser = getattr(p, browser_type).launch(headless=True)
        # browser = getattr(p, browser_type).launch()
        yield browser
        browser.close()


@pytest.fixture(scope="function")
def context(browser):
    context = browser.new_context(viewport=None)
    yield context
    context.close()

@pytest.fixture(scope="function")
def info_page(context):
    fake = Faker()
    page = context.new_page()
    page.goto("https://circula-qa-challenge.vercel.app/users/sign_up")
    page.get_by_role("button",name = "Deny All").click()

    email = f"{fake.user_name()}@circula.com"
    password = fake.password(length=10, special_chars=False, digits=True,
                             upper_case=True, lower_case=True)
    first_name = fake.first_name()
    last_name = fake.last_name()
    company_name = fake.company()
    phone_number = fake.numerify(text="##########")
    
    page.locator(r"#textfield-\:Rqikmm\:").fill(email)
    page.locator(r"#textfield-\:R3aikmm\:").fill(password)
    page.evaluate("document.querySelector('div.ItvoJ').click()")
    page.get_by_role("button", name = "Try for free").click()
    page.get_by_label("First Name").fill(first_name)
    page.get_by_label("Last Name").fill(last_name)
    page.get_by_label("Phone Number").fill(phone_number)
    page.get_by_role("button", name = "Next step").click()
    page.get_by_label("Company name").fill(company_name)

    yield page


    page.close()

