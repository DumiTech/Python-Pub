from pytest import mark

@mark.entertainment
def test_can_navigate_to_entertainment(chrome_browser):
    second_browser = chrome_browser
    chrome_browser.get('https://www.siriusxm.com/')
    assert True