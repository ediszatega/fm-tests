from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

def test_add_to_cart(driver, wait):
    bottom_label_close_element = (By.CSS_SELECTOR, ".woocommerce-store-notice__dismiss-link")
    wait_bottom_label_close_element = wait.until(EC.element_to_be_clickable(bottom_label_close_element))
    wait_bottom_label_close_element.click()
    
    nav_racunari_element = (By.XPATH, "//*[text()='Računari']")
    wait_racunari_nav = wait.until(EC.element_to_be_clickable(nav_racunari_element))
    wait_racunari_nav.click()

    btn_add_to_cart = (By.CLASS_NAME, 'add-links-wrap')
    wait_btn_add = wait.until(EC.element_to_be_clickable(btn_add_to_cart))
    wait_btn_add.click()

    wait.until(lambda driver: int(driver.find_element(By.CLASS_NAME, 'cart-items').text) > 0)

    cart_value = (By.CLASS_NAME, 'cart-items')
    wait_cart_value = wait.until(EC.presence_of_element_located(cart_value))
    cart_value_str = wait_cart_value.text

    assert int(cart_value_str) > 0
