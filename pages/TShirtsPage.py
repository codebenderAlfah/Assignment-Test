class TShirtsPage():
    def __init__(self, driver, actions):
        self.driver = driver
        self.actions = actions

        self.blue_filter_x_path = "(//*[@class='layered_color'])[2]"
        self.item2_x_path = "//*[@class='ajax_block_product col-xs-12 col-sm-6 col-md-4 first-in-line last-line first-item-of-tablet-line first-item-of-mobile-line last-mobile-line']"
        self.blue_color_x_path = "//a[@id='color_2']"

        self.item2 = driver.find_element_by_xpath(self.item2_x_path)
        self.blue_color = driver.find_element_by_xpath(self.blue_color_x_path)

    def click_filter_blue(self):
        self.driver.find_element_by_xpath(self.blue_filter_x_path).click()

    def click_and_select_blue_tshirt(self):
        self.actions.move_to_element(self.item2).move_to_element(self.blue_color).click().perform()