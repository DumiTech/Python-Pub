class Config:
    def __init__(self, env):
        
        self.base_url = {
            'dev': 'https://mydev-env.com',
            'qa': 'https://myqa-env.com',
            'staging': 'https://mystaging-env.com',
            'production': 'https://myproduction-end.com'
        }[env]
        
        self.app_port = {
            'dev': 809,
            'qa': 808,
            'staging': '800',
            'production': '8080'
        }[env]