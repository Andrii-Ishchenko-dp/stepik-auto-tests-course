from selenium import webdriver
import time
import math
def sum(x, y):
    return str(x + y)


try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    num1=browser.find_element_by_css_selector ("#num1")
    x=int(num1.text)
    num2=browser.find_element_by_css_selector ("#num2")
    y=int(num2.text)



    from selenium.webdriver.support.ui import Select
    select = Select(browser.find_element_by_css_selector ("#dropdown"))
    select.select_by_value(sum(x, y))

    submit = browser.find_element_by_css_selector ("[type=submit]")
    submit.click()

finally:
    time.sleep(10)
    browser.quit()
