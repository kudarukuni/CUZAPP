import requests
import json
from config import Config
from typing import Dict, List, Optional

class WhatsAppClient:
    """Client for interacting with Meta Cloud WhatsApp API"""
    
    def __init__(self):
        self.api_url = Config.WHATSAPP_API_URL
        self.phone_number_id = Config.PHONE_NUMBER_ID
        self.access_token = Config.ACCESS_TOKEN
        self.headers = {
            "Authorization": f"Bearer {self.access_token}",
            "Content-Type": "application/json"
        }
    
    def send_message(self, recipient_phone: str, message_text: str) -> Dict:
        """
        Send a text message to a WhatsApp user
        
        Args:
            recipient_phone: Recipient's phone number (with country code, no +)
            message_text: Message text to send
            
        Returns:
            API response as dictionary
        """
        url = f"{self.api_url}/{self.phone_number_id}/messages"
        
        payload = {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": recipient_phone,
            "type": "text",
            "text": {
                "preview_url": False,
                "body": message_text
            }
        }
        
        response = requests.post(url, json=payload, headers=self.headers)
        return response.json()
    
    def send_template_message(self, recipient_phone: str, template_name: str, 
                             language: str = "en_US", parameters: Optional[List] = None) -> Dict:
        """
        Send a template message to a WhatsApp user
        
        Args:
            recipient_phone: Recipient's phone number
            template_name: Name of the template
            language: Language code (default: en_US)
            parameters: List of parameter values for template
            
        Returns:
            API response as dictionary
        """
        url = f"{self.api_url}/{self.phone_number_id}/messages"
        
        payload = {
            "messaging_product": "whatsapp",
            "to": recipient_phone,
            "type": "template",
            "template": {
                "name": template_name,
                "language": {
                    "code": language
                }
            }
        }
        
        if parameters:
            payload["template"]["components"] = [
                {
                    "type": "body",
                    "parameters": [{"type": "text", "text": param} for param in parameters]
                }
            ]
        
        response = requests.post(url, json=payload, headers=self.headers)
        return response.json()
    
    def send_button_message(self, recipient_phone: str, message_body: str, 
                           buttons: List[Dict]) -> Dict:
        """
        Send an interactive button message
        
        Args:
            recipient_phone: Recipient's phone number
            message_body: Message body text
            buttons: List of button dictionaries with 'id' and 'title'
            
        Returns:
            API response as dictionary
        """
        url = f"{self.api_url}/{self.phone_number_id}/messages"
        
        payload = {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": recipient_phone,
            "type": "interactive",
            "interactive": {
                "type": "button",
                "body": {
                    "text": message_body
                },
                "action": {
                    "buttons": [
                        {
                            "type": "reply",
                            "reply": {
                                "id": btn["id"],
                                "title": btn["title"]
                            }
                        } for btn in buttons[:3]  # Max 3 buttons
                    ]
                }
            }
        }
        
        response = requests.post(url, json=payload, headers=self.headers)
        return response.json()
    
    def mark_message_as_read(self, message_id: str) -> Dict:
        """
        Mark a received message as read
        
        Args:
            message_id: ID of the message to mark as read
            
        Returns:
            API response as dictionary
        """
        url = f"{self.api_url}/{self.phone_number_id}/messages"
        
        payload = {
            "messaging_product": "whatsapp",
            "status": "read",
            "message_id": message_id
        }
        
        response = requests.post(url, json=payload, headers=self.headers)
        return response.json()
