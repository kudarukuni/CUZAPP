"""
Chatbot logic and response generation
"""

class WhatsAppChatbot:
    """Main chatbot class for handling user messages and generating responses"""
    
    def __init__(self):
        self.conversation_history = {}
    
    def process_message(self, sender: str, message: str) -> str:
        """
        Process incoming message and generate response
        
        Args:
            sender: WhatsApp phone number of sender
            message: Incoming message text
            
        Returns:
            Response message to send back
        """
        # Initialize conversation history for new users
        if sender not in self.conversation_history:
            self.conversation_history[sender] = []
        
        # Store the incoming message
        self.conversation_history[sender].append({
            'type': 'user',
            'text': message
        })
        
        # Generate response based on message content
        response = self.generate_response(message.lower().strip(), sender)
        
        # Store the bot response
        self.conversation_history[sender].append({
            'type': 'bot',
            'text': response
        })
        
        return response
    
    def generate_response(self, message: str, sender: str) -> str:
        """
        Generate response based on user message
        
        Args:
            message: Processed incoming message
            sender: User's phone number
            
        Returns:
            Response message
        """
        # Example greeting responses
        greetings = ['hello', 'hi', 'hey', 'hola', 'bonjour']
        if any(greeting in message for greeting in greetings):
            return "👋 Hello! Welcome to our WhatsApp chatbot. How can I help you today?"
        
        # Help command
        if message in ['help', 'menu', 'options']:
            return (
                "📋 *Available Commands:*\n"
                "1. 'hello' - Greeting\n"
                "2. 'time' - Current time\n"
                "3. 'help' - Show this menu\n"
                "4. 'info' - About us\n"
                "5. Any question - I'll try to help!\n\n"
                "What would you like to do?"
            )
        
        # Info command
        if message in ['info', 'about']:
            return (
                "ℹ️ *About Us*\n"
                "This is a WhatsApp chatbot powered by Twilio and Python.\n"
                "We're here to assist you 24/7!\n\n"
                "Type 'help' to see available commands."
            )
        
        # Time command
        if message in ['time', 'current time', 'what time']:
            from datetime import datetime
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            return f"🕐 Current time: {current_time}"
        
        # Default response
        return (
            "I understand you said: \"" + message + "\"\n\n"
            "I'm still learning! 🤖 You can try:\n"
            "• 'hello' - Say hi\n"
            "• 'help' - View commands\n"
            "• 'info' - Learn about me\n\n"
            "How else can I assist you?"
        )
    
    def get_conversation_history(self, sender: str) -> list:
        """Get conversation history for a user"""
        return self.conversation_history.get(sender, [])
    
    def clear_history(self, sender: str = None) -> None:
        """Clear conversation history"""
        if sender:
            self.conversation_history.pop(sender, None)
        else:
            self.conversation_history.clear()
