from selenium import webdriver
import time
import math
def mat(x):
    return str(math.log(abs(12*math.sin(x))))

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    but=browser.find_element_by_css_selector ("button")
    but.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    num=browser.find_element_by_css_selector ("#input_value")
    x=int(num.text)

    ans=browser.find_element_by_css_selector ("#answer")
    ans.send_keys(mat(x))

    submit = browser.find_element_by_css_selector ("[type=submit]")  # ищем кнопку
    submit.click()

finally:
    time.sleep(10)                                                    # ставим выполнене команды на паузу 10 секунд
    browser.quit()
