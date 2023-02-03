from selenium.webdriver.support.select import Select

from locators import locators


class BillingAddressPage:

    def __init__(self, driver):
        self.driver = driver
        # billing account page elements
        self.addresses_link = locators.BillingAddressLocators.addresses_link
        self.first_name_input = locators.BillingAddressLocators.first_name_input
        self.last_name_input = locators.BillingAddressLocators.last_name_input
        self.edit_link = locators.BillingAddressLocators.edit_link
        self.country_select = locators.BillingAddressLocators.country_select
        self.address_input = locators.BillingAddressLocators.address_input
        self.postcode_input = locators.BillingAddressLocators.postcode_input
        self.city_input = locators.BillingAddressLocators.city_input
        self.phone_input = locators.BillingAddressLocators.phone_input
        self.save_address_button = locators.BillingAddressLocators.save_address_button
        self.message_div = locators.BillingAddressLocators.message_div

    def open_edit_billing_address(self):
        self.driver.find_element(*self.addresses_link).click()
        self.driver.find_element(*self.edit_link).click()

    def set_personal_data(self, first_name, last_name):
        self.driver.find_element(*self.first_name_input).send_keys(first_name)
        self.driver.find_element(*self.last_name_input).send_keys(last_name)

    def set_country(self, country):
        select = Select(self.driver.find_element(*self.country_select))
        select.select_by_visible_text(country)

    def set_address(self, street, postcode, city):
        self.driver.find_element(*self.address_input).send_keys(street)
        self.driver.find_element(*self.postcode_input).send_keys(postcode)
        self.driver.find_element(*self.city_input).send_keys(city)

    def set_phone_number(self, number):
        self.driver.find_element(*self.phone_input).send_keys(number)

    def save_address(self):
        self.driver.find_element(*self.save_address_button).click()

    def get_message_text(self):
        return self.driver.find_element(*self.message_div).text
