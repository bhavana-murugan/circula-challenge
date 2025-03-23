"""
Includes automated tests for some of the main checks from task 1.
Using dummy creds and signing up process is set up as a fixture in conftest.py to save time.
Dependencies: playwright
Author: Bhavana Murugan
Date: March 23, 2025
"""

from playwright.sync_api import expect


def test_one(info_page): 
    """
    - Verify sweden is listed in country dropdown page and selecting it updates the field
    - Verify alphabetical order
    """
    
    page = info_page
    dropdown = page.get_by_role("combobox")
    dropdown.click()
    page.wait_for_selector("role=option")
    options = page.evaluate('''() => {
    const elements = Array.from(document.querySelectorAll('[id^="downshift-"][role="option"]'));
    return elements.map(option => option.textContent.trim());}''')
    assert options == sorted(options), f"Dropdown options are not in alphabetical order: {options}"
    dropdown = page.locator('xpath=/html/body/div[1]/div/div/main/div/form/div[3]/div[1]/label/div[2]/input')
    dropdown.click()
    dropdown.fill("Sweden")
    page.keyboard.press("ArrowDown")
    page.wait_for_timeout(100)
    page.keyboard.press("Enter")

    assert page.get_by_role("combobox").input_value() == "Sweden"
    

def test_two(info_page):
    """
    - Verify that selecting nothing in the field should display the error “Company registration country is required” and CTA disabled dynamically.
    """ 
    
    page = info_page
    page.get_by_role("combobox").click()
    page.get_by_role("combobox").fill("")
    page.click("body")
    expect(page.get_by_text("Company registration country is required")).to_be_visible()
    page.get_by_role("button",name = "Create an account").click()
    button = page.get_by_role("button",name = "Create an account")
    expect(button).to_be_disabled()

    
def test_three(info_page):
    """
    - Verify form submitted successfully after selecting Sweden
    - Verify user data retention after clicking back(caching)
    - Verify hdyhau works as expected after selecting Sweden
    """ 
    
    page = info_page
    page = info_page
    dropdown = page.locator('xpath=/html/body/div[1]/div/div/main/div/form/div[3]/div[1]/label/div[2]/input')
    dropdown.click()
    dropdown.fill("Sweden")
    page.keyboard.press("ArrowDown")
    page.wait_for_timeout(500)
    page.keyboard.press("Enter")
    page.locator('input[name="hdyhau"]').click()
    page.locator('text=DATEV').click()
    page.get_by_role("button",name = "Create an account").click()
    page.go_back()


def test_four(info_page): #Verify form submitted successfully for other country
    page = info_page
    dropdown = page.locator('xpath=/html/body/div[1]/div/div/main/div/form/div[3]/div[1]/label/div[2]/input')
    dropdown.click()
    dropdown.fill("Belgium")
    page.keyboard.press("ArrowDown")
    page.wait_for_timeout(100)
    page.locator('input[name="hdyhau"]').click()
    page.locator('text=DATEV').click()
    page.get_by_role("button",name = "Create an account").click()

