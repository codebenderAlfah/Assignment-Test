class CasualDressesPage():
    def __init__(self, driver, actions):
        self.driver = driver
        self.actions = actions

        self.dresses_bar_x_path = "(//*[@class='sf-with-ul'])[4]"
        self.casual_dresses_bar_x_path = "(//a[@title='Casual Dresses'])[2]"
        self.dresses = driver.find_element_by_xpath(self.dresses_bar_x_path)
        self.casual_dresses = driver.find_element_by_xpath(self.casual_dresses_bar_x_path)

    def click_casualdresses(self):
        self.actions.move_to_element(self.dresses).move_to_element(self.casual_dresses).click().perform()