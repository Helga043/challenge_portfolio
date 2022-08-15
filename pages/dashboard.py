from pages.base_page import BasePage


class Dashboard(BasePage):
    scouts_panel_xpath = "//*[@id='__next']/div[1]/header/div/h6"
    main_page_menu_xpath = "//*[text()='Main page']"
    players_menu_xpath = "//*[contains(@class, 'jss29 jss31')]/span"
    language_menu_xpath = "//*[@id='__next']/div[1]/div/div/div/ul[2]/div[1]/div[2]/span"
    sign_out_menu_xpath = "//*[text()='Sign out']"
    players_count_block_xpath = "//*[@id='__next']/div[1]/main/div[2]/div[1]/div"
    matches_count_block_xpath = "//*[@id='__next']/div[1]/main/div[2]/div[2]/div"
    reports_count_block_xpath = "//*[@id='__next']/div[1]/main/div[2]/div[3]/div"
    events_count_block_xpath = "//*[@id='__next']/div[1]/main/div[2]/div[4]/div"
    dev_team_contact_button_xpath = "//*[contains(@class, 'MuiCardActions-root MuiCardActions-spacing')]/a"
    add_player_button_xpath = "//*[text()='Add player']"




