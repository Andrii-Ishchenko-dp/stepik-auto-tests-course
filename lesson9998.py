        input2 = browser.find_element_by_css_selector (".form-control.second")
        input2.send_keys("Petrov")
        input4 = browser.find_element_by_css_selector ("[class="second_block" class="form-control.first"]")
        input4.send_keys("+3333")
        input5 = browser.find_element_by_css_selector ("[class="second_block" class="form-control.second"]")
        input5.send_keys("Petrova 34")
