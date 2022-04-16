class IndexPage():

    def __init__(self, driver):
        self.driver = driver

        self.signin_button_class_name = "login"

    def click_signin(self):
        self.driver.find_element_by_class_name(self.signin_button_class_name).click()