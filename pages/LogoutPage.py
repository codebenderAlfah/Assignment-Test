class LogoutPage():
    def __init__(self, driver):
        self.driver = driver

        self.signout_button_class_name = "logout"

    def click_signout(self):
        self.driver.find_element_by_class_name(self.signout_button_class_name).click()