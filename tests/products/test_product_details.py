from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def test_product_details(driver, wait):
    driver.get("https://www.doper.ba/")
    driver.maximize_window()
    
    nav_laptopi_element = (By.XPATH,'//header[@class="searchform search-layout-advanced"]/div/span/button')
    wait_laptopi_nav = wait.until(EC.element_to_be_clickable(nav_laptopi_element))
    wait_laptopi_nav.click()