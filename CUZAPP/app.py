"""
Main entry point for the WhatsApp chatbot application
"""

import os
from app import create_app

# Create Flask app
app = create_app()

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    debug = os.getenv('FLASK_DEBUG', False)
    
    print("🤖 WhatsApp Chatbot starting...")
    print(f"Running on http://localhost:{port}")
    print("Make sure your Twilio webhook URL is configured correctly in the Twilio console.")
    
    app.run(
        host='0.0.0.0',
        port=port,
        debug=debug
    )
