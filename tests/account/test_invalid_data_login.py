from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def test_invalid_data_login(driver, wait):
    username_text = "testmail@test.com"
    password_text = "password123"
    invalid_login_message = "Nepoznata adresa e-pošte. Ponovno provjerite ili pokušajte svojim korisničkim imenom."

    bottom_label_close_element = (By.CSS_SELECTOR, ".woocommerce-store-notice__dismiss-link")
    wait_bottom_label_close_element = wait.until(EC.element_to_be_clickable(bottom_label_close_element))
    wait_bottom_label_close_element.click()

    menu_mojracun_element = (By.XPATH, "//*[text()='Moj račun']")
    wait_mojracun = wait.until(EC.element_to_be_clickable(menu_mojracun_element))
    wait_mojracun.click()

    input_username = (By.ID, "username")
    wait_input_username = wait.until(EC.element_to_be_clickable(input_username))
    wait_input_username.click()
    wait_input_username.clear()
    wait_input_username.send_keys(username_text)

    input_password = (By.ID, "password")
    wait_input_password = wait.until(EC.element_to_be_clickable(input_password))
    wait_input_password.click()
    wait_input_password.clear()
    wait_input_password.send_keys(password_text)

    btn_prijava = (By.XPATH, "//button[text()='Prijava']")
    wait_btn_prijava = wait.until(EC.element_to_be_clickable(btn_prijava))
    wait_btn_prijava.click()

    invalid_login_element = (By.CSS_SELECTOR, ".wc-block-components-notice-banner__content")
    wait_invalid_login_element = wait.until(EC.presence_of_element_located(invalid_login_element))

    
    assert invalid_login_message in wait_invalid_login_element.text