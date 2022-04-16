import time
from selenium import webdriver
from selenium.webdriver import ActionChains

from pages.BlueTShirtPage import BlueTShirtsPage
from pages.CasualDressAddToCart import CasualDressAddToCart
from pages.CasualDressesPage import CasualDressesPage
from pages.CheckoutAddressPage import CheckoutAddressPage
from pages.CheckoutPaymentPage import CheckoutPaymentPage
from pages.CheckoutShippingPage import CheckoutShippingPage
from pages.CheckoutSummaryPage import CheckoutSummaryPage
from pages.ConfirmOrderPage import ConfirmOrderPage
from pages.IndexPage import IndexPage
from pages.LoginPage import LoginPage
from pages.LogoutPage import LogoutPage
from pages.Shirts import Shirts
from pages.TShirtsPage import TShirtsPage

user1_email = "smithjhon@outlook.com"
user1_password = "abc123"

driver = webdriver.Chrome("F:/try/webdriver/chromedriver.exe")
actions = ActionChains(driver)

driver.implicitly_wait(10)
driver.maximize_window()

driver.get('http://automationpractice.com/index.php')

index = IndexPage(driver)
index.click_signin()

login = LoginPage(driver)
login.enter_email(user1_email)
login.enter_password(user1_password)
login.click_login()

casual_dress = CasualDressesPage(driver, actions)
casual_dress.click_casualdresses()

casual_dress_cart = CasualDressAddToCart(driver, actions)
casual_dress_cart.click_add_to_cart()
casual_dress_cart.click_continue_shopping()

shirts = Shirts(driver)
shirts.click_shirts()

tshirt = TShirtsPage(driver, actions)
tshirt.click_filter_blue()
tshirt.click_and_select_blue_tshirt()

bluetshirt = BlueTShirtsPage(driver)
bluetshirt.click_add_to_cart()
bluetshirt.click_proceed_to_checkout()

checkout_summary = CheckoutSummaryPage(driver)
checkout_summary.click_summary_checkout_button()

checkout_address = CheckoutAddressPage(driver)
checkout_address.click_address_checkout_button()

checkout_shipping = CheckoutShippingPage(driver)
checkout_shipping.click_agree_terms_button()
checkout_shipping.click_shipping_checkout_button()

checkout_payment = CheckoutPaymentPage(driver)
checkout_payment.click_pay_by_check()

confirm_order = ConfirmOrderPage(driver)
confirm_order.click_confirm_button()

logout = LogoutPage(driver)
logout.click_signout()

time.sleep(5)
driver.quit()
