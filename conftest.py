import pytest , time
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="module")
def browser():
    with sync_playwright() as p:
        browser = p.firefox.launch(headless=False)
        yield browser
        browser.close()

@pytest.fixture
def context(browser):
    context = browser.new_context(viewport=None)
    yield context
    context.close()