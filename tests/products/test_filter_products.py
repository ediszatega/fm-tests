from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def test_filter_products(driver, wait):
    bottom_label_close_element = (By.CSS_SELECTOR, ".woocommerce-store-notice__dismiss-link")
    wait_bottom_label_close_element = wait.until(EC.element_to_be_clickable(bottom_label_close_element))
    wait_bottom_label_close_element.click()

    nav_laptopi_element = (By.XPATH, "//*[text()='Laptopi']")
    wait_laptopi_nav = wait.until(EC.element_to_be_clickable(nav_laptopi_element))
    wait_laptopi_nav.click()

    product_element_locator = (By.XPATH, "//span[text()='Ryzen 5 5500U']")
    wait_product = wait.until(EC.element_to_be_clickable(product_element_locator))
    product_element = driver.find_element(*product_element_locator)
    product_element.click()
    product_element_text = product_element.text

    product_title_element_locator = (By.XPATH, "//h3[text()='Laptop HP 255 G8 7J034AA R5 5500U 256GB SSD 8GB DDR4 15,6”']")
    wait_product_title = wait.until(EC.presence_of_element_located(product_title_element_locator))
    product_title_text = wait_product_title.text

    assert product_element_text[6:] in product_title_text