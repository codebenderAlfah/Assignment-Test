class Shirts():
    def __init__(self, driver):
        self.driver = driver

        self.shirts_button_x_path = "(//a[@title='T-shirts'])[2]"

    def click_shirts(self):
        self.driver.find_element_by_xpath(self.shirts_button_x_path).click()