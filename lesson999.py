from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_css_selector (".first_block .form-control.first")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_css_selector (".first_block .form-control.second")
    input2.send_keys("Petrov")
    input4 = browser.find_element_by_css_selector (".first_block .form-control.third")
    input4.send_keys("a@gmail.com")
    input3 = browser.find_element_by_css_selector (".second_block .form-control.first")
    input3.send_keys("+3335")
    input5 = browser.find_element_by_css_selector (".second_block .form-control.second")
    input5.send_keys("petrova 34")
    time.sleep(5)
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text
    print(welcome_text)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
