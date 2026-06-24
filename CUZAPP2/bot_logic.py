"""
Bot logic for handling WhatsApp messages and generating responses
"""

class ChatBot:
    """Simple chatbot logic for WhatsApp"""
    
    def __init__(self):
        self.intents = {
            "greet": {
                "keywords": ["hello", "hi", "hey", "good morning", "good evening"],
                "response": "Hello! 👋 Welcome to our chatbot. How can I help you today?"
            },
            "help": {
                "keywords": ["help", "support", "assist", "what can you do"],
                "response": "I can help you with:\n1. General information\n2. Product details\n3. Support requests\n\nWhat would you like to know?"
            },
            "thanks": {
                "keywords": ["thank", "thanks", "appreciate", "thank you"],
                "response": "You're welcome! 😊 Is there anything else I can help you with?"
            },
            "goodbye": {
                "keywords": ["bye", "goodbye", "see you", "farewell"],
                "response": "Goodbye! 👋 Thanks for chatting with us. Have a great day!"
            }
        }
    
    def get_response(self, user_message: str) -> str:
        """
        Generate a response based on user message
        
        Args:
            user_message: The message from the user
            
        Returns:
            Response message
        """
        user_message_lower = user_message.lower().strip()
        
        # Check for matching intents
        for intent, data in self.intents.items():
            for keyword in data["keywords"]:
                if keyword in user_message_lower:
                    return data["response"]
        
        # Default response if no intent matches
        return self._get_default_response(user_message)
    
    def _get_default_response(self, user_message: str) -> str:
        """
        Generate a default response when no intent is matched
        
        Args:
            user_message: The message from the user
            
        Returns:
            Default response message
        """
        return (
            f"Thank you for your message: '{user_message}'\n\n"
            "I'm still learning and don't have a specific response for this. "
            "Type 'help' to see what I can assist you with."
        )
    
    def add_intent(self, intent_name: str, keywords: list, response: str):
        """
        Add a new intent to the bot
        
        Args:
            intent_name: Name of the intent
            keywords: List of keywords that trigger this intent
            response: Response message for this intent
        """
        self.intents[intent_name] = {
            "keywords": keywords,
            "response": response
        }
