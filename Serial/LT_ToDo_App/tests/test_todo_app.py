from time import sleep

from selenium.webdriver.common.by import By


def test_lambdatest_todo_app(py):
    py.visit('https://lambdatest.github.io/sample-todo-app/')
    py.maximize_window()
    # py.get uses the CSS Selector, hence we find the CSS Selector of the WebElement using Inspect Tool
    # More information about py.get at https://elsnoman.gitbook.io/pylenium/pylenium-commands/get
    element_1 = py.get("ul.list-unstyled > li:nth-of-type(1) > [type='checkbox']")
    element_1.click()

    # Get the instance of the current WebDriver and use the WebDriver commands like they are used in any test
    # automation framework (e.g. PyTest) More information about webdriver at
    # https://elsnoman.gitbook.io/pylenium/pylenium-commands/webdriver
    py.webdriver.find_element(By.NAME, "li2").click()

    title = "Sample page - lambdatest.com"
    assert title == py.title()

    sample_text = "Happy Testing at LambdaTest"

    # Locate the DOM element using the CSS Selector
    elem_text_box = py.get("[ng-model='sampleList.sampletodoText']")
    elem_text_box.type(sample_text)

    # The submit method will submit the data but we submit the data by pressing the Add Button
    # elem_text_box.submit()
    # sleep(5)

    # Note - find (https://elsnoman.gitbook.io/pylenium/pylenium-commands/find)
    # Note - findx (https://elsnoman.gitbook.io/pylenium/pylenium-commands/find_xpath)

    elem_add_button = py.get(".btn")
    elem_add_button.click()
    sleep(5)

    assert py.contains('Happy Testing at LambdaTest')
    print("Test of Sample ToDo app complete")
