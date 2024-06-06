import os


class Config:
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:password@localhost/calendar_db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    HOLIDAY_API_KEY = os.environ.get("HOLIDAY_API_KEY")
    SECRET_KEY = os.environ.get("SECRET_KEY", "your_secret_key")
