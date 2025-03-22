
"""
This is a brief description of what the script does.
"""

# Import statements
import pytest , time
from playwright.sync_api import sync_playwright, expect , Page


# Test Functions
def test_one(context):
    page = context.new_page()
    page.set_viewport_size({"width": 1920, "height": 1600})  # Adjust to your screen resolution
    page.goto("https://circula-qa-challenge.vercel.app/users/sign_up")
    page.get_by_role("button",name = "Deny All").click()
    page.locator(r"#textfield-\:Rqikmm\:").fill("test@circula.com")
    page.locator(r"#textfield-\:R3aikmm\:").fill("testtest1")
    page.evaluate("document.querySelector('div.ItvoJ').click()")
    page.get_by_role("button", name = "Try for free").click()
    page.locator(r"#textfield-\:r0\:").fill("test")
    page.locator(r"#textfield-\:r1\:").fill("test")
    page.locator(r"#textfield-\:r2\:").fill("123456")
    page.get_by_role("button", name = "Next step").click()


    time.sleep(3)






    # page.locator("label").filter(has_text="I'm happy to get occasional").click()
    # page.locator("label").filter(has_text="I agree to the").click()
    # page.locator("label").filter(has_text="I agree to the").click()
    # page.locator("label").filter(has_text="I agree to the").click()

    # page.locator(".sc-b0a11073-0.fYVNCA").nth(0).set_checked(True)
    # checkbox = page.locator('input[name="acceptTos"]')
   

    time.sleep(5)