""" from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def test_invalid_data_login(driver, wait):
    email_text = "testmail@test.com"

    bottom_label_close_element = (By.CSS_SELECTOR, ".woocommerce-store-notice__dismiss-link")
    wait_bottom_label_close_element = wait.until(EC.element_to_be_clickable(bottom_label_close_element))
    wait_bottom_label_close_element.click()

    menu_mojracun_element = (By.XPATH, "//*[text()='Moj račun']")
    wait_mojracun = wait.until(EC.element_to_be_clickable(menu_mojracun_element))
    wait_mojracun.click()

    input_email = (By.ID, "reg_email")
    wait_input_email = wait.until(EC.element_to_be_clickable(input_email))
    wait_input_email.click()
    wait_input_email.clear()
    wait_input_email.send_keys(email_text)

    btn_prijava = (By.XPATH, "//button[text()='Registracija']")
    wait_btn_prijava = wait.until(EC.element_to_be_clickable(btn_prijava))
    wait_btn_prijava.click()

    invalid_login_element = (By.CSS_SELECTOR, ".wc-block-components-notice-banner__content")
    wait_invalid_login_element = wait.until(EC.presence_of_element_located(invalid_login_element))

    
    assert invalid_login_message in wait_invalid_login_element.text """