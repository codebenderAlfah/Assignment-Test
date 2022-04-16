class ConfirmOrderPage():
    def __init__(self, driver):
        self.driver = driver

        self.confirm_button_x_path = "//button[@class='button btn btn-default button-medium']"

    def click_confirm_button(self):
        self.driver.find_element_by_xpath(self.confirm_button_x_path).click()