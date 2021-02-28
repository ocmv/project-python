class Config:
	SECRET_KEY = 'A487poi9'

class DevelopmentConfig(Config):
	DEBUG = True
	SQLALCHEMY_DATABASE_URI = 'mysql://root:@localhost:3306/project-python'
	SQLALCHEMY_TRACK_MODIFICATIONS = False
config = {
	'development': DevelopmentConfig,
	'default': DevelopmentConfig
}