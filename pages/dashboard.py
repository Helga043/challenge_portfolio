import time
from pages.base_page import BasePage



class Dashboard(BasePage):
    scouts_panel_xpath = "//*[@id='__next']/div[1]/header/div/h6"
    main_page_menu_xpath = "//*[text()='Main page']"
    players_menu_xpath = "//*[contains(@class, 'jss29 jss31')]/span"
    language_menu_xpath = "//ul[2]/div[1]/div[2]/span"
    sign_out_menu_xpath = "//*[text()='Sign out']"
    players_count_block_xpath = "//div[2]/div[1]/div"
    matches_count_block_xpath = "//div[2]/div[2]/div"
    reports_count_block_xpath = "//div[2]/div[3]/div"
    events_count_block_xpath = "//div[2]/div[4]/div"
    dev_team_contact_button_xpath = "//*[contains(@class, 'MuiCardActions-root MuiCardActions-spacing')]/a"
    add_player_button_xpath = "//*[text()='Add player']"

    expected_title = "Scouts panel"
    dashboard_url = 'https://scouts-test.futbolkolektyw.pl/'

    def title_of_page(self):
        self.wait_for_element_to_be_clickable(self.add_player_button_xpath)
        assert self.get_page_title(self.dashboard_url) == self.expected_title

    def click_on_add_player_button(self):
        self.click_on_the_element(self.add_player_button_xpath)

    def check_sign_out_button(self):
        self.wait_for_element_to_be_clickable(self.sign_out_menu_xpath)

    def click_on_the_sign_out_button(self):
        self.click_on_the_element(self.sign_out_menu_xpath)

    def click_on_language_button(self):
        self.click_on_the_element(self.language_menu_xpath)


