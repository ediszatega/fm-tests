from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def test_navigating_from_footer(driver, wait):
    payment_type = "4. Virmansko plaćanje"

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
 
    nacin_placanja_link = (By.XPATH, "//span[text()='Načini plaćanja']")
    wait_nacin_placanja_link = wait.until(EC.element_to_be_clickable(nacin_placanja_link))
    wait_nacin_placanja_link.click()

    nacin_placanja_page_text = (By.XPATH, "//span[text()='4. Virmansko plaćanje']")
    wait_nacin_placanja_page_text  = wait.until(EC.presence_of_element_located(nacin_placanja_page_text))
    payment_type_text = wait_nacin_placanja_page_text.text

    assert payment_type_text == payment_type