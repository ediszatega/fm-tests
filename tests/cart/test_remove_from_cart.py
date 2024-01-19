from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def test_remove_from_cart(driver, wait):
    empty_cart_text = "No products added to the cart"
    
    nav_laptopi_element = (By.XPATH, "//*[text()='Laptopi']")
    wait_laptopi_nav = wait.until(EC.element_to_be_clickable(nav_laptopi_element))
    wait_laptopi_nav.click()
    
    btn_add_to_cart = (By.XPATH, "//*[text()='Dodaj u košaricu']")
    wait_btn_add_to_cart = wait.until(EC.element_to_be_clickable(btn_add_to_cart))
    wait_btn_add_to_cart.click() 
    
    btn_view_cart = (By.CSS_SELECTOR, '#woocommerce_widget_cart-3 > div > div > p.woocommerce-mini-cart__buttons.buttons > a:nth-child(1)')
    wait_btn_view_cart = wait.until(EC.element_to_be_clickable(btn_view_cart))
    wait_btn_view_cart.click()

    btn_remove_from_cart = (By.CSS_SELECTOR, ".remove.remove-product.position-absolute")
    wait_btn_remove_from_cart = wait.until(EC.element_to_be_clickable(btn_remove_from_cart))
    wait_btn_remove_from_cart.click()

    empty_cart_text_element = (By.XPATH, f"//*[text()='{empty_cart_text}']")
    wait_empty_cart_text = wait.until(EC.presence_of_element_located(empty_cart_text_element))

    
    assert empty_cart_text in wait_empty_cart_text.text
