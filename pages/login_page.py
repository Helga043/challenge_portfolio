from pages.base_page import BasePage


class LoginPage(BasePage):
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//*[@id='password']"
    sign_in_button_xpath = "//*[@type='submit']/span[1]"
    login_url = 'https://scouts-test.futbolkolektyw.pl/en'
    expected_title = "Scouts panel - sign in"
    title_of_box_xpath = "//*[@id='__next']/form/div/div[1]/h5"
    header_of_box = "Scouts Panel"

    error_message_xpath = "//span[contains(@class, 'MuiTypography-root')]"
    message_invalid_login_data = "Invalid Login or Password"
    message_empty_password = "Fill the password field"

    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)

    def type_in_password(self, password):
        self.field_send_keys(self.password_field_xpath, password)

    def click_on_the_sign_in_button(self):
        self.click_on_the_element(self.sign_in_button_xpath)

    def title_of_page(self):
        assert self.get_page_title(self.login_url) == self.expected_title

    def check_title_of_header(self):
        self.assert_element_text(self.driver, self.title_of_box_xpath, self.header_of_box)

    def type_all_for_log_in(self, email, password):
        self.type_in_email(email)
        self.type_in_password(password)
        self.click_on_the_sign_in_button()

    def log_in_with_invalid_data_message(self):
        self.assert_element_text(self.driver, self.error_message_xpath, self.message_invalid_login_data)

    def empty_password_message(self):
        self.assert_element_text(self.driver, self.error_message_xpath, self.message_empty_password)







