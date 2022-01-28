from pytest import mark


@mark.skip
@mark.parametrize('phone_brand', [
        ('Samsung', 'HTC'),
        ('Tesla'),
        ('Iphone')
    ]
)
def test_phone_turns_on(phone_brand):
    print(f'{phone_brand} turns on as expected')
    
def test_browser_can_navigate_to_training_ground(browser):
    browser.get('https://techstepacademy.com/training-ground')
    