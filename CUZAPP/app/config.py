import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Base configuration"""
    TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
    TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
    TWILIO_PHONE_NUMBER = os.getenv('TWILIO_PHONE_NUMBER')
    FLASK_ENV = os.getenv('FLASK_ENV', 'development')
    FLASK_DEBUG = os.getenv('FLASK_DEBUG', False)
    PORT = int(os.getenv('PORT', 5000))
    WEBHOOK_URL = os.getenv('WEBHOOK_URL', 'http://localhost:5000/webhook')

    @staticmethod
    def validate():
        """Validate that all required config variables are set"""
        required_vars = ['TWILIO_ACCOUNT_SID', 'TWILIO_AUTH_TOKEN', 'TWILIO_PHONE_NUMBER']
        for var in required_vars:
            if not getattr(Config, var):
                raise ValueError(f"Missing required environment variable: {var}")
