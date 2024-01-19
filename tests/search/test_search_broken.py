from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def test_search_broken(driver, wait):
    search_text = '/()/()/()&)("!%#&/!#"%/"$'
    not_found_text = 'Nisu pronađeni proizvodi koji odgovaraju vašem odabiru.'

    search_field = (By.NAME, 's')
    wait_search_field = wait.until(EC.element_to_be_clickable(search_field))
    wait_search_field.click()
    wait_search_field.clear()
    wait_search_field.send_keys(search_text)
    
    wait.until(EC.element_to_be_clickable(wait_search_field)).submit()
        
    load_search = (By.CLASS_NAME,'nothing-found-message')
    wait.until(EC.presence_of_element_located(load_search))
    load_search_text = driver.find_element(*load_search).find_element(By.TAG_NAME, 'p').text
    
    assert load_search_text == not_found_text
