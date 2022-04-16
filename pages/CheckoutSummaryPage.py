class CheckoutSummaryPage():
    def __init__(self, driver):
        self.driver = driver

        self.summary_checkout_button_x_path = "//a[@class='button btn btn-default standard-checkout button-medium']"

    def click_summary_checkout_button(self):
        self.driver.find_element_by_xpath("//a[@class='button btn btn-default standard-checkout button-medium']").click()