#login_page.py

#This class represents the "Login Page" of the  Apllication
#It is designed using the Page Object Model (POM) Pattern
#Which helps to kep locators and actions separate from the test logic

from playwright.sync_api import Page

class LoginPage:
    def __init__(self,page:Page):
        """Constructor that initialises th eplaywright page instance
           abd defines all locators used on the Logi Page"""
        
        self.page=page

        #Locators
        #Using CSS selectors to locate elemets on the Login page
        self.txt_email_address=page.locator("#input-email")
        self.txt_password=page.locator("#input-password")
        self.btn_login=page.locator("input[value='Login']")
        self.txt_error_message=page.locator(".alert.alert-danger.alert-dismissible")


    #=======Action Methods========
    def set_email(self,email:str):
        "Enter the email address in the Email field"
        try:
            self.txt_email_address.fill(email)
        except Exception as E:
            print(f"Exception while entering email: {E}")
    
    def set_password(self,password:str):
        "Enter the email address in the password field"
        try:
            self.txt_email_address.fill(password)
        except Exception as E:
            print(f"Exception while entering password: {E}")
    
    def click_login(self,email:str,password:str):
        """perform the complete login operation
        1. Enter email
        2. Enter password
        3. Click the Login button
        """
        self.set_email(email)
        self.set_password(password)
        self.click_login()

    def get_login_error(self):
        """
        Return the error message element if login fails
        Example use:
                error_text=login_page.get_login_error().inner_text()
        """

        try:
            return self.txt_error_message
        except Exception as e:
            print(f"Exception while fetching login error message: {e}")
            return None
