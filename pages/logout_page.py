#logout_page.py
#====================
#This class represents the "Logout Page" of the application
#It allows the Page Object Model (POM) design pattern
#to separate page locators and actions from the test logic

from playwright.sync_api import Page
from pages.home_page import Homepage #Adjust this import path as per your project structure

class LogoutPage:
    def __init__(self,page:Page):
        """
        Constructor  that initializes the Playwright Page instance
        and defines all locators used on the Logout Page
        """

        self.page=page

        #Locators
        self.btn_continue =page.locator('.btn.btn-primary')

    #Action Method
    def click_continue(self):
        """Docstring for __init__
        
        :param self: Description
        :param page: Description
        :type page: Page
        Click the 'Continue button after logging out.
        This typically redirects the user back to the Home Page."""

        try:
            self.btn_continue.click()
        except Exception as e:
            print(f"Exception while clicking 'continue button: {e}")
    
    def get_continue_button(self):
        """
        Return the continue button locator.
        Useful for checking its visiblility or state in test assertions

        Example:
                expect(logout_page.get_continue_button()).to_be_visible()
        """

        try:
            return self.btn_continue
        except Exception as e:
            print(f"Exception while fetchinf 'Continue' button locator:{e}")
            return None
