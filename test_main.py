"""
Includes automated tests for some of the main checks from task 1.
Using dummy creds and signing up process is set up as a fixture in conftest.py to save time.
Automated cases: TC01, TC02, TC04, TC05, TC06, TC07, TC09, TC12, TC14, TC25
Dependencies: playwright
Author: Bhavana Murugan
Date: March 23, 2025
"""

from playwright.sync_api import sync_playwright , expect


def test_one(info_page): 
    """
    - TC01, TC02, TC04, TC14
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
    - TC05, TC06
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
    - TC07, TC09, TC12
    """ 
    
    page = info_page
    page = info_page
    dropdown = page.locator('xpath=/html/body/div[1]/div/div/main/div/form/div[3]/div[1]/label/div[2]/input')
    dropdown.click()
    dropdown.fill("Sweden")
    page.keyboard.press("ArrowDown")
    page.wait_for_timeout(200)
    page.keyboard.press("Enter")
    page.locator('input[name="hdyhau"]').click()
    page.locator('text=DATEV').click()
    page.get_by_role("button",name = "Create an account").click()
    page.go_back()
