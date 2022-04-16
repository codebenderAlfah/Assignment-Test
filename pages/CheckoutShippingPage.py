class CheckoutShippingPage():
    def __init__(self, driver):
        self.driver = driver

        self.terms_agree_button_x_path = "//input[@id='cgv']"
        self.shipping_checkout_button_x_path = "//button[@class='button btn btn-default standard-checkout button-medium']"

    def click_agree_terms_button(self):
        self.driver.find_element_by_xpath(self.terms_agree_button_x_path).click()

    def click_shipping_checkout_button(self):
        self.driver.find_element_by_xpath(self.shipping_checkout_button_x_path).click()