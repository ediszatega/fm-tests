from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

def test_correct_search(driver, wait):
    
    search_text = "AMD"
    
    driver.get("https://www.doper.ba/")
    driver.maximize_window()

    search_field = (By.XPATH, '//input[@name="s"]')
    wait_search_field = wait.until(EC.element_to_be_clickable(search_field))
    wait_search_field.click()
    wait_search_field.clear()
    wait_search_field.send_keys(search_text)
    btn_search_element = (By.XPATH,'//form[@class="searchform search-layout-advanced"]/div/span/button')
    wait_search_button = wait.until(EC.element_to_be_clickable(btn_search_element))
    wait_search_button.click()
    load_search = By.XPATH,'//body[contains(@class, "archive search search-results")]'
    wait.until(EC.presence_of_element_located(load_search))
    
    item_searched= driver.find_elements(By.XPATH, "//div[@class='product-inner']//div[2]//a//h3[contains(text(), '%s')]" % search_text)
    
    assert len(item_searched) == 0
