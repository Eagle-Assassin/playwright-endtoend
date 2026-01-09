"""
Test Case: User Login Functionality

===========================================
Test Steps
===========================================

Test Case 1: Verify Login with Invalid Credentials
--------------------------------------------------
1. Open the application in the browser.
2. Navigate to the "My Account" menu on the Home page.
3. Click on the "Login" link.
4. Enter an invalid email address and password.
5. Click on the "Login" button.
6. Verify that an error message appears indicating invalid credentials.

Expected Result:
----------------
An error message should be displayed, and the user should not be logged in.


Test Case 2: Verify Login with Valid Credentials
------------------------------------------------
1. Open the application in the browser.
2. Navigate to the "My Account" menu on the Home page.
3. Click on the "Login" link.
4. Enter a valid email address and password.
5. Click on the "Login" button.
6. Verify that the "My Account" page is displayed after successful login.

Expected Result:
----------------
The "My Account" page should appear, confirming a successful login.
"""

from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.my_account_page import MyAccountPage
from playwright.sync_api import Page,expect
from config import Config
import time



def test_invalid_user_login(page):
    hompage=HomePage(page)
    loginpage =LoginPage(page)

    hompage.click_my_account()
    hompage.click_login()

    loginpage.set_email(Config.invalid_email)
    loginpage.set_password(Config.invalid_password)

    loginpage.click_login()

    # error= 

    expect(loginpage.get_login_error()).to_be_visible(timeout=3000)

def test_valid_user_login(page):
    hompage=HomePage(page)
    loginpage =LoginPage(page)

    hompage.click_my_account()
    hompage.click_login()

    loginpage.set_email(Config.email)
    loginpage.set_password(Config.password)

    loginpage.click_login()

    time.sleep(2)

    myaccount=MyAccountPage(page)

    page_heading= myaccount.get_my_account_page_heading()

    expect(page_heading).to_be_visible(timeout=300)