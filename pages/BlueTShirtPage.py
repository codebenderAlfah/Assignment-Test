class BlueTShirtsPage():
    def __init__(self, driver):
        self.driver = driver

        self.add_to_cart_Button_x_path = "//button[@class='exclusive']"
        self.proceed_to_checkout_button_x_path = "//a[@class='btn btn-default button button-medium']"

    def click_add_to_cart(self):
        self.driver.find_element_by_xpath(self.add_to_cart_Button_x_path).click()

    def click_proceed_to_checkout(self):
        self.driver.find_element_by_xpath(self.proceed_to_checkout_button_x_path).click()