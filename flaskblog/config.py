import os

class Config:
	SECRET_KEY = '8c4dc18e4cb337da30eb8ee734d8499c'
	SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
	MAIL_SERVER = 'smtp.googlemail.com'
	MAIL_PORT = 587
	MAIL_USE_TLS = True
	MAIL_USERNAME = os.environ.get('EMAIL_ID')
	MAIL_PASSWORD = os.environ.get('PASS')