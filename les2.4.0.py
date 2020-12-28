from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time                             # импортируем время, чтобы использовать time.sleep(n) для остановки работы программы на n секунд
import math
def mat(x):
    return str(math.log(abs(12*math.sin(x))))

try:                                                       #блок в котором мы указываем прямую ссылку на тестируемую страницу
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    button = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100"))

    submit=browser.find_element_by_css_selector ("#book")
    submit.click()

    num=browser.find_element_by_css_selector ("#input_value")
    x=int(num.text)

    ans=browser.find_element_by_css_selector ("#answer")
    ans.send_keys(mat(x))

    sub=browser.find_element_by_css_selector ("#solve")
    sub.click()

finally:
    time.sleep(10)                                                    # ставим выполнене команды на паузу 10 секунд
    browser.quit()
