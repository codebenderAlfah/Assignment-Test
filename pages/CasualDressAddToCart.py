class CasualDressAddToCart():
    def __init__(self, driver, actions):
        self.driver = driver
        self.actions = actions

        self.item1_dress_x_path = "//*[@class='ajax_block_product col-xs-12 col-sm-6 col-md-4 first-in-line last-line first-item-of-tablet-line first-item-of-mobile-line last-mobile-line']"
        self.add_to_cart_button_x_path = "//*[@class='button ajax_add_to_cart_button btn btn-default']"
        self.continue_shopping_button_x_path = "//*[@class='continue btn btn-default button exclusive-medium']"

        self.item1 = driver.find_element_by_xpath(self.item1_dress_x_path)
        self.add_to_cart_button = driver.find_element_by_xpath(self.add_to_cart_button_x_path)
        self.continue_shopping_button = driver.find_element_by_xpath(self.continue_shopping_button_x_path)

    def click_add_to_cart(self):
        self.actions.move_to_element(self.item1).move_to_element(self.add_to_cart_button).click().perform()

    def click_continue_shopping(self):
        self.continue_shopping_button.click()