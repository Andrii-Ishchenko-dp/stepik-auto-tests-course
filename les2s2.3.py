from selenium import webdriver
import os
import time

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    name=browser.find_element_by_css_selector ("[name=firstname]")
    name.send_keys("Ваня")
    laname=browser.find_element_by_css_selector ("[name=lastname]")
    laname.send_keys("Ivanov")
    maile=browser.find_element_by_css_selector ("[name=email]")
    maile.send_keys("asd.com")

    element=browser.find_element_by_css_selector ("#file")
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'new.txt')           # добавляем к этому пути имя файла
    element.send_keys(file_path)

    submit = browser.find_element_by_css_selector ("[type=submit]")  # ищем кнопку
    submit.click()

finally:
    time.sleep(10)                                                    # ставим выполнене команды на паузу 10 секунд
    browser.quit()


