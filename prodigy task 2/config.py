import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'mysql://root:nksql8899@localhost:3306/prodigy_db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_POOL_SIZE = int(os.getenv('POOL_SIZE', 5))
    SQLALCHEMY_MAX_OVERFLOW = int(os.getenv('MAX_OVERFLOW', 10))
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev') 