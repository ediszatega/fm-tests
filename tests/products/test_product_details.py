from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def test_product_details(driver, wait):
    bottom_label_close_element = (By.CSS_SELECTOR, ".woocommerce-store-notice__dismiss-link")
    wait_bottom_label_close_element = wait.until(EC.element_to_be_clickable(bottom_label_close_element))
    wait_bottom_label_close_element.click()

    nav_laptopi_element = (By.XPATH, "//*[text()='Laptopi']")
    wait_laptopi_nav = wait.until(EC.element_to_be_clickable(nav_laptopi_element))
    wait_laptopi_nav.click()
    
    product_element = (By.CLASS_NAME, 'woocommerce-loop-product__title')
    wait_product = wait.until(EC.element_to_be_clickable(product_element))
    product_name = wait_product.text
    wait_product.click()
    
    product_details_element = (By.CSS_SELECTOR, '.product_title.entry-title.show-product-nav')
    wait_product_details = wait.until(EC.presence_of_element_located(product_details_element))
    product_details_name = wait_product_details.text

    assert product_name == product_details_name    