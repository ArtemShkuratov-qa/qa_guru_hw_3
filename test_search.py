from selene import browser, be, have

def test_search():
    browser.open('https://duckduckgo.com/')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('html').should(have.text('Не нашли то, что искали?'))
    browser.element('[id="react-layout"]').should(have.text('yashaka/selene: User-oriented Web UI browser tests in Python'))

def test_search_without_results():
    browser.open('https://duckduckgo.com/')
    browser.element('[name="q"]').should(be.blank).type('----').press_enter()
    browser.element('[id="react-layout"]').should(have.text('По запросу ---- результаты не найдены.'))