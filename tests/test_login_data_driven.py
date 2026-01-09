from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.my_account_page import MyAccountPage
from playwright.sync_api import Page,expect
from config import Config
import time
import pytest


#load / read the data from the files
from utilities.data_reader_util import read_csv_data, read_excel_data,read_json_data

for i in range(3):
    if i==0:
        data=read_csv_data("testdata/logindata.csv")
    elif i==2:
        data=read_json_data("testdata/logindata.json")
    else:
        data=read_excel_data("testdata/logindata.xlsx")

@pytest.mark.parametrize("testname,email,password,expected",data)
def test_login_data_driven(page,testname,email,password,expected):
    
    hompage=HomePage(page)
    loginpage =LoginPage(page)

    hompage.click_my_account()
    hompage.click_login()

    loginpage.set_email(email)
    loginpage.set_password(password)

    loginpage.click_login()

    time.sleep(2)

    myaccount=MyAccountPage(page)

    

    page_heading= myaccount.get_my_account_page_heading()

    if expected=="success":
        expect(page_heading).to_be_visible(timeout=3000)
    else:
         expect(loginpage.get_login_error()).to_be_visible(timeout=3000)

        