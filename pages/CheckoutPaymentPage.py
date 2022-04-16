class CheckoutPaymentPage():
    def __init__(self, driver):
        self.driver = driver

        self.pay_by_cheque_link_x_path = "//a[@class='cheque']"


    def click_pay_by_check(self):
        self.driver.find_element_by_xpath(self.pay_by_cheque_link_x_path).click()