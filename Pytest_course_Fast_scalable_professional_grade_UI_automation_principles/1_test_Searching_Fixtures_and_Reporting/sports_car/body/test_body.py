from pytest import mark

@mark.body
class BodyTests:
    @mark.door
    def test_can_navigate_to_body_page(self, chrome_browser):
        second_browser = chrome_browser
        chrome_browser.get('http://www.motortrend.com/')
        assert True
    
    @mark.smoke
    def test_bumper(self):
        assert True