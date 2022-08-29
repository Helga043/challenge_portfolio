from selenium.webdriver.common.by import By

from pages.base_page import BasePage

class AddPlayer(BasePage):
    player_name_xpath = "//input[@name = 'name']"
    player_surname_xpath = "//input[@name = 'surname']"
    player_age_xpath = "//input[@name = 'age']"
    choose_leg_xpath = "//*[@id='mui-component-select-leg']"
    left_leg_xpath = "//li[@data-value='left']"
    right_leg_xpath = "//li[@data-value='right']"
    player_position_xpath = "//input[@name='mainPosition']"
    submit_button_xpath = "//button[@type='submit']/span[1]"
    add_player_header_xpath = "//span[contains(@class, 'MuiTypography-h5')]"
    main_page_button_xpath = "//div/ul[1]/div[1]/div[2]/span"

    def type_player_name(self, name):
        self.field_send_keys(self.player_name_xpath, name)

    def type_player_surname(self, surname):
        self.field_send_keys(self.player_surname_xpath, surname)

    def select_player_age(self, age):
        self.field_send_keys(self.player_age_xpath, age)

    def choose_leg(self, leg):
        self.click_on_the_element(self.choose_leg_xpath)
        if leg == "right":
            self.click_on_the_element(self.right_leg_xpath)
        else:
            self.click_on_the_element(self.left_leg_xpath)

    def type_to_main_position(self, position):
        self.field_send_keys(self.player_position_xpath, position)

    def click_submit_button(self):
        self.click_on_the_element(self.submit_button_xpath)

    def click_main_page_button(self):
        self.click_on_the_element(self.main_page_button_xpath)

