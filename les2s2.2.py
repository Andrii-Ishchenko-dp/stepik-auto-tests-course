from selenium import webdriver
import time
import math
def mat(x):
    return str(math.log(abs(12*math.sin(x))))

try:                                                       #блок в котором мы указываем прямую ссылку на тестируемую страницу
    link = "http://suninjuly.github.io/execute_script.html"      #блок в котором мы указываем прямую ссылку на тестируемую страницу
    browser = webdriver.Chrome()                           #блок в котором мы указываем прямую ссылку на тестируемую страницу
    browser.get(link)

    num1=browser.find_element_by_css_selector ("#input_value")
    x=int(num1.text)
    y=mat(x)

    answer=browser.find_element_by_css_selector ("#answer")
    answer.send_keys(y)

    chek= browser.find_element_by_css_selector ("#robotCheckbox")
    chek.click()

    rad = browser.find_element_by_css_selector("#robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", rad)
    rad.click()

    sab = browser.find_element_by_css_selector("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", sab)
    sab.click()

finally:
    time.sleep(10)                                                    # ставим выполнене команды на паузу 10 секунд
    browser.quit()


