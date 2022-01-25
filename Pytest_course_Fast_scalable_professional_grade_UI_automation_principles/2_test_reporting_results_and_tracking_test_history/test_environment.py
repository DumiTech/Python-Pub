from pytest import mark

@mark.skip(reason="broken by deploy hash_xyz")
def test_environment_is_qa(app_config):
    base_url = app_config.base_url
    port = app_config.app_port 
    assert base_url == 'https://myqa-env.com'
    assert port == 808

@mark.xfail(reason="This feature should have been deprecated")
def test_environment_is_dev(app_config):
    base_url = app_config.base_url
    port = app_config.app_port 
    assert base_url == 'https://mydev-env.com'
    assert port == 809

def test_environment_is_staging(app_config):
    base_url = app_config.base_url
    port = app_config.app_port
    assert base_url == "https://mystaging-env.com"
    assert port == "800"

@mark.skip    
def test_environment_is_production(app_config):
    base_url = app_config.base_url
    port = app_config.app_port
    assert base_url == "https://myproduction-end.com"
    assert port == "8080"
    
def test_this_should_always_pass():
    assert true
    
@mark.skip(reason="Broken, fixing next sprint")
def test_this_needs_work():
    assert False