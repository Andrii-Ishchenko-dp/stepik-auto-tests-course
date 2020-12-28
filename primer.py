from selenium import webdriver          # вызываем селениум для работы
import time                             # импортируем время, чтобы использовать time.sleep(n) для остановки работы программы на n секунд
import math                             # импортирует блок с формулами, которые можно использовать в написании кода
def sum(x, y):                          # пример создания функции, чтобы потом использовать для нахождения результата
    return str(x + y)                   # пример создания функции, чтобы потом использовать для нахождения результата
def mat(x):
    return str(math.log(abs(12*math.sin(x))))


try:                                                       #блок в котором мы указываем прямую ссылку на тестируемую страницу
    link = "http://suninjuly.github.io/selects1.html"      #блок в котором мы указываем прямую ссылку на тестируемую страницу
    browser = webdriver.Chrome()                           #блок в котором мы указываем прямую ссылку на тестируемую страницу
    # говорим WebDriver искать каждый элемент в течение 5 секунд
    browser.implicitly_wait(5)
    browser.get(link)

Если надо настроить ожидание, то применяем:
# добавляем сверху это
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    button = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "id"), "значение")) # даём браузеру команду ждать 12 секунд, пока значение элимента id не станит равно значению


Перевод фотмата в число + нахождение текста:
    num1=browser.find_element_by_css_selector ("#num1")      #num1 - переменная, в которую мы присваеваем объект, найденный по сss селектору, в данном случае по id = num1
    x=int(num1.text)                                         # х - переменная, которй присваиваем численное значение текста найденного по селектору выше. Команда  int(n) преобразовывает информацию в число. Команда .text выуживает из объекта только текст.
    num2=browser.find_element_by_css_selector ("#num2")
    y=int(num2.text)

Написание значения в поле:
    input1 = browser.find_element_by_css_selector ("#answer") #поиск поля для записи
    input1.send_keys(y)                                       # написание в поле значения y

Присваиваем элементу значение атрибута:
    x_element = browser.find_element_by_css_selector ("#treasure") # находим элемент по css селектору
    x = x_element.get_attribute("valuex")                          # присваиваем х значение атрибута valuex элемента выше

Работа со списками:
    from selenium.webdriver.support.ui import Select          # вызываем блок select, для того, чтобы в списке выбрать нужное значение
    select = Select(browser.find_element_by_css_selector ("#dropdown")) # находим список
    select.select_by_value(sum(x, y))                              # в списке делаем поиск по значению sum(x, y)

Нажимаем на кнопку:
    submit = browser.find_element_by_css_selector ("[type=submit]")  # ищем кнопку
    submit.click()                 # нажимаем на кнопку, такой же командой можно выбирать значения радиобатонн и чекбокса

Пролистываение страницы до объекта:
    rad = browser.find_element_by_css_selector("#robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", rad) #эта строка с помощью скрипта проматывает строницу до нужной кнопки
    rad.click()

Загрузка файла в объект(в той же дерриктории что и скрипт):
    element=browser.find_element_by_css_selector ("#file")
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'new.txt')           # добавляем к этому пути имя файла
    element.send_keys(file_path)

    Открывающиеся окна, которые требуют подтверждение:

    confirm = browser.switch_to.alert                          #обнаруживаем открывшееся окно, которое ждёт подтверждения действия
    confirm.accept()                                           #нажимаем на Ок в открывшемся окне

    alert = browser.switch_to.alert
    alert_text = alert.text                                    #получаем текст с окна

    confirm = browser.switch_to.alert                          # окно с выбором принятия или отмены
    confirm.accept()                                           # принимаем

    prompt = browser.switch_to.alert                           # окно с написанием своего ответа
    prompt.send_keys("My answer")                              # записываем ответ
    prompt.accept()

Переход на соседнюю вкладку:
    new_window = browser.window_handles[1]                    #создаём переменную и присваиваем ей значение 1. Счёт идёт с 0. Текущая вкладка =0
    browser.switch_to.window(new_window)                      # даём команду браузеру перейти во вкладку с таким названием




finally:
    time.sleep(10)                                                    # ставим выполнене команды на паузу 10 секунд
    browser.quit()                                                    # закрываем браузер

