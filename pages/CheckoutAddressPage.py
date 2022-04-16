class CheckoutAddressPage():
    def __init__(self, driver):
        self.driver = driver

        self.address_checkout_button_x_path = "//button[@class='button btn btn-default button-medium']"

    def click_address_checkout_button(self):
        self.driver.find_element_by_xpath(self.address_checkout_button_x_path).click()