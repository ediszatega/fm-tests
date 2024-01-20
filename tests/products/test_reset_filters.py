from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

def test_reset_filters(driver, wait):
    bottom_label_close_element = (By.CSS_SELECTOR, ".woocommerce-store-notice__dismiss-link")
    wait_bottom_label_close_element = wait.until(EC.element_to_be_clickable(bottom_label_close_element))
    wait_bottom_label_close_element.click()

    nav_laptopi_element = (By.XPATH, "//*[text()='Laptopi']")
    wait_laptopi_nav = wait.until(EC.element_to_be_clickable(nav_laptopi_element))
    wait_laptopi_nav.click()

    cb_filter = (By.XPATH, "//span[text()='Ryzen 5 5500U']")
    driver.execute_script("arguments[0].scrollIntoView(true);", wait.until(EC.presence_of_element_located(cb_filter)))
    wait_cb_filter = wait.until(EC.element_to_be_clickable(cb_filter))
    wait_cb_filter.click()
    wait.until(EC.staleness_of(wait_cb_filter))
    
    btn_reset = (By.XPATH, "//*[text()='Reset']")
    driver.execute_script("arguments[0].scrollIntoView(true);", wait.until(EC.presence_of_element_located(btn_reset)))
    wait_btn_reset = wait.until(EC.element_to_be_clickable(btn_reset))
    wait_btn_reset.click()
    time.sleep(5)

    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "product-inner")))
    
    assert element                          