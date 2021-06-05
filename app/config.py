class Config:
    pass

class ProdConfig(Config):
    pass

class DevConfig (Config):
    DEBUG = True


config_options = {
    'develpoment': DevConfig,
    'production': ProdConfig
}