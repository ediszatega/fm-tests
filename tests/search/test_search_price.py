from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

def test_product_details(driver, wait):
    min_price = "699"
    max_price = "799"
    price_range = range(int(min_price), int(max_price) + 1)
    
    nav_laptopi_element = (By.XPATH, "//*[text()='Laptopi']")
    wait_laptopi_nav = wait.until(EC.element_to_be_clickable(nav_laptopi_element))
    wait_laptopi_nav.click()
    
    input_min_price = (By.NAME, "minPrice")
    wait_min_price = wait.until(EC.element_to_be_clickable(input_min_price))
    wait_min_price.click()
    min_price_len = len(wait_min_price.get_attribute("value"))
    for _ in range(min_price_len):
        wait_min_price.send_keys(Keys.BACKSPACE)
    wait_min_price.send_keys(min_price)
    wait_min_price.send_keys(Keys.TAB)
    wait.until(EC.staleness_of(wait_min_price))
    
    input_max_price = (By.NAME, "maxPrice")
    wait_max_price = wait.until(EC.element_to_be_clickable(input_max_price))
    wait_max_price.click()
    max_price_len = len(wait_max_price.get_attribute("value"))
    for _ in range(max_price_len):
        wait_max_price.send_keys(Keys.BACKSPACE)
    wait_max_price.send_keys(max_price)
    wait_max_price.send_keys(Keys.TAB)
    wait.until(EC.staleness_of(wait_max_price))
    
    
    
    price_span_elemenets = driver.find_elements(By.CSS_SELECTOR, '.woocommerce-Price-amount.amount')

    for price_span in price_span_elemenets:
        text_element = price_span.find_element(By.TAG_NAME, 'bdi')
        price = int(text_element.text.split('.')[0])
        assert price in price_range   
        