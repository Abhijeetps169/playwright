import os

class Config:
    BASE_URL = os.getenv("BASE_URL")
    API_URL = os.getenv("API_URL")
    BROWSER = os.getenv("BROWSER", "chromium")