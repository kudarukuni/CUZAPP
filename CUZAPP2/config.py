import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Configuration for WhatsApp Chatbot"""
    
    # Meta Cloud API Configuration
    ACCESS_TOKEN = os.getenv("ACCESS_TOKEN", "")
    PHONE_NUMBER_ID = os.getenv("PHONE_NUMBER_ID", "")
    BUSINESS_ACCOUNT_ID = os.getenv("BUSINESS_ACCOUNT_ID", "")
    VERIFY_TOKEN = os.getenv("VERIFY_TOKEN", "")
    
    # WhatsApp API URL
    WHATSAPP_API_URL = "https://graph.instagram.com/v18.0"
    
    # Server Configuration
    PORT = int(os.getenv("PORT", 5000))
    DEBUG = os.getenv("DEBUG", "True") == "True"
    
    @staticmethod
    def validate():
        """Validate that all required configuration is present"""
        required = ["ACCESS_TOKEN", "PHONE_NUMBER_ID", "VERIFY_TOKEN"]
        missing = [key for key in required if not getattr(Config, key)]
        if missing:
            raise ValueError(f"Missing configuration: {', '.join(missing)}")
