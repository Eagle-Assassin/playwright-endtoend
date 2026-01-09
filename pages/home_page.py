from playwright.sync_api import Page

class HomePage:
    def __init__(self,page:Page):
        self.page=page

        #Locators
        self.lnk_myaccount=page.locator("a[title='My Account'] span[class='hidden-xs hidden-sm hidden-md']")
        self.lnk_register=page.get_by_role("link", name="Register")
        # self.lnk_register=page.locator("a has-text('Register')")
        self.lnk_login=page.locator("a[href='https://tutorialsninja.com/demo/index.php?route=account/login']")
        self.txt_searchbox=page.locator("input[placeholder='Search']")
        self.btn_search=page.locator("#search button[type='button']")

    #Action Method
    #Each Method represents a user interaction on the page

    def get_home_page_title(self)->str:
        """Return the title of the Home page."""
        title =self.page.title()
        return title
    
    def click_my_account(self):
        """Click on the 'My Account' link"""
        try:
            self.lnk_myaccount.click()
        except Exception as e:
            print(f"Exception while clicking 'My Account' : {e}")
            raise
    
    def click_register(self):
        """Click on the 'Register' link under My Account"""
        try:
            self.lnk_register.click()
        except Exception as e:
            print(f"Exception while clicking 'Register' link under My Account : {e}")
            raise

    def click_login(self):
        """Click on the 'Login' link under My Account"""
        try:
            self.lnk_login.click()
        except Exception as e:
            print(f"Exception while clicking 'Login' link under My Account : {e}")
            raise

    def enter_product_name(self,product_name:str):
        """Enter the product name into the search input box"""
        try:
            self.txt_searchbox.fill(product_name)
        except Exception as e:
            print(f"Exception while entering the product name into the search input box : {e}")
            raise

    def click_search(self):
        """click on th search button to initiate the product search"""
        try:
            self.btn_search.click()
        except Exception as e:
            print(f"Exception while clicking 'seach' Button {e}")
            raise
