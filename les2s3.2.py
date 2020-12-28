from selenium import webdriver
import time
import math
def mat(x):
    return str(math.log(abs(12*math.sin(x))))

try:                                                       #блок в котором мы указываем прямую ссылку на тестируемую страницу
    link = "http://suninjuly.github.io/alert_accept.html"      #блок в котором мы указываем прямую ссылку на тестируемую страницу
    browser = webdriver.Chrome()                           #блок в котором мы указываем прямую ссылку на тестируемую страницу
    browser.get(link)

    start=browser.find_element_by_css_selector ("button")
    start.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    per=browser.find_element_by_css_selector ("#input_value")
    x=int(per.text)

    ans=browser.find_element_by_css_selector ("#answer")
    ans.send_keys(mat(x))

    sab=browser.find_element_by_css_selector ("[type=submit]")
    sab.click()

finally:
    time.sleep(10)                                                    # ставим выполнене команды на паузу 10 секунд
    browser.quit()
