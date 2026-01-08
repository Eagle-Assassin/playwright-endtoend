#my_account_page.py
#========================
#This class represents the 'My Account' page of the application
#It follows the Page Object Model (POM) pattern to separate
#the page locators and actions from the actual test cases

from playwright.sync_api import Page,expect
from pages.logout_page import LogoutPage

class MyAccountPage:
    """Page Object Model Class for the My Account Page"""

    def __init__(self,page:Page):
        """
        Construct to initialize the palywright Page instance
        and define all locators present on the MY Account Page.
        """

        self.page=page

        #Locators
        self.msg_heading=page.locator("h2:has-text('My Account')")
        self.lnk_logout= page.locator("text='Logout'").nth(1)

    #Page Validation Methods
    def get_my_account_page_heading(self):
        """
        Return the locator for the 'My Account' page heading
        Can be used in test assertionsto verify page visibility

        """
        try:
            return(self.msg_heading)

        except Exception as e:
            print(f"Error returning My Account page heading: {e}")
            return None
        
    def click_logout(self) ->LogoutPage:
        """ 
        Clicks on the 'Logout' link to logout to the user
        Returns as instance of the LogoutPage class
        to allow chained navigation in tests
        
        Example:
            logout_page=my_account_page.click_logout()
        
        """

        try:
            self.lnk_logout.click()
            return LogoutPage(self.page)
        except Exception as e:
            print(f"Unable to click Logout link: {e}")
            raise e
    
    #======== Page Title Verifications ======
    def get_page_title(self)->str:
        """
        Returns the title of the current page
        
        Example:
            assert my_account_page.get_page_title()=="My Account"""

        try:
            return self.page.title()
        except Exception as e:
            print(f"Error retrieving page title: {e}")
            return ""