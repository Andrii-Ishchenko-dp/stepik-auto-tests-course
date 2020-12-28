from selenium import webdriver
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_css_selector ("#input_value")
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element_by_css_selector ("#answer")
    input1.send_keys(y)
    option1 = browser.find_element_by_css_selector ("[type=checkbox]")
    option1.click()

    input2 = browser.find_element_by_css_selector ("#robotsRule")
    input2.click()

    submit = browser.find_element_by_css_selector ("[type=submit]")
    submit.click()

finally:

    time.sleep(10)
    browser.quit()








