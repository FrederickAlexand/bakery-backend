import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://postgres:geWWxhGWtocSFRlbDcQPHbJlwzGvjWgK@autorack.proxy.rlwy.net:11990/railway')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'supersecretkey'
