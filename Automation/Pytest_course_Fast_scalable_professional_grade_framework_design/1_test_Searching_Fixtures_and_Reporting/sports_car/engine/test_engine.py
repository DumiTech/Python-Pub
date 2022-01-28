from pytest import mark



@mark.smoke
@mark.engine
@mark.ui
def test_can_navigate_to_engine_page(chrome_browser):
    second_browser = chrome_browser
    chrome_browser.get('http://www.artofmanliness.com/articles/how-a-cars-engine-works/')
    assert True
