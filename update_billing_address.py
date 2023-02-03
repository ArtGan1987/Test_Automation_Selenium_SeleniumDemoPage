
import random
import pytest
from pages.billing_addresse_page import BillingAddressPage
from pages.my_account_page import MyAccountPage
from time import sleep


@pytest.mark.usefixtures("setup")
class TestUpdateBillingAddress:

    def test_update_billing_address(self):
        email = str(random.randint(0, 10000)) + "test@gmail.com"
        my_account_page = MyAccountPage(self.driver)
        my_account_page.open_page()
        my_account_page.create_account(email, "Test!@#123")
        billing_address_page = BillingAddressPage(self.driver)
        billing_address_page.open_edit_billing_address()
        billing_address_page.set_personal_data("Artur", "Gandor")
        billing_address_page.set_country("Poland")
        billing_address_page.set_address("Kwiatowa 1", "23-123", "Warszawa")
        billing_address_page.set_phone_number("070772072")
        billing_address_page.save_address()

        msg = "Address changed successfully."
        assert msg in billing_address_page.get_message_text()



