from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

def test_product_sorting(driver, wait):
    bottom_label_close_element = (By.CSS_SELECTOR, ".woocommerce-store-notice__dismiss-link")
    wait_bottom_label_close_element = wait.until(EC.element_to_be_clickable(bottom_label_close_element))
    wait_bottom_label_close_element.click()

    nav_racunari_element = (By.XPATH, "//*[text()='Računari']")
    wait_racunari_nav = wait.until(EC.element_to_be_clickable(nav_racunari_element))
    wait_racunari_nav.click()

    select_sort_by = (By.CLASS_NAME, 'orderby')
    wait_select = wait.until(EC.element_to_be_clickable(select_sort_by))
    select = Select(wait_select)

    select.select_by_value('price-desc')
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.orderby option[selected="selected"]')))

    max_price_input = (By.ID, "292710-max-price")
    wait_max_price_input = wait.until(EC.presence_of_element_located(max_price_input))
    max_price = wait_max_price_input.get_attribute("value")

    first_product_price = (By.TAG_NAME, 'bdi')
    wait_first_product_price = wait.until(EC.presence_of_element_located(first_product_price))
    price = wait_first_product_price.text.split('.')[0]

    assert int(max_price) == int(price)
