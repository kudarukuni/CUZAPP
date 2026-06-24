"""
WhatsApp Chatbot using Meta Cloud API
Main Flask application
"""

from flask import Flask, request, jsonify
import json
import logging
from config import Config
from whatsapp_client import WhatsAppClient
from bot_logic import ChatBot

# Initialize Flask app
app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize clients
whatsapp_client = WhatsAppClient()
chatbot = ChatBot()

# Validate configuration on startup
try:
    Config.validate()
except ValueError as e:
    logger.error(f"Configuration error: {e}")
    raise


@app.route("/webhook", methods=["POST"])
def handle_webhook():
    """
    Handle incoming webhooks from Meta Cloud API
    Processes incoming messages and sends responses
    """
    try:
        body = request.get_json()
        logger.info(f"Received webhook: {json.dumps(body, indent=2)}")
        
        # Check if this is a message event
        if body.get("object") == "whatsapp_business_account":
            changes = body.get("entry", [{}])[0].get("changes", [])
            
            for change in changes:
                value = change.get("value", {})
                messages = value.get("messages", [])
                
                for message in messages:
                    # Mark message as read
                    whatsapp_client.mark_message_as_read(message["id"])
                    
                    # Get sender phone number
                    sender_phone = message.get("from")
                    
                    # Get message text
                    message_text = message.get("text", {}).get("body", "")
                    
                    if message_text:
                        logger.info(f"Message from {sender_phone}: {message_text}")
                        
                        # Generate bot response
                        bot_response = chatbot.get_response(message_text)
                        
                        # Send response
                        response = whatsapp_client.send_message(sender_phone, bot_response)
                        logger.info(f"Response sent: {response}")
        
        return jsonify({"status": "success"}), 200
    
    except Exception as e:
        logger.error(f"Error handling webhook: {str(e)}", exc_info=True)
        return jsonify({"status": "error", "message": str(e)}), 500


@app.route("/webhook", methods=["GET"])
def verify_webhook():
    """
    Verify webhook endpoint for Meta Cloud API
    Called by Meta to verify the webhook URL is valid
    """
    try:
        verify_token = request.args.get("hub.verify_token")
        challenge = request.args.get("hub.challenge")
        
        # Verify the token
        if verify_token == Config.VERIFY_TOKEN:
            logger.info("Webhook verified successfully")
            return challenge, 200
        else:
            logger.warning(f"Invalid verify token: {verify_token}")
            return "Invalid verify token", 403
    
    except Exception as e:
        logger.error(f"Error verifying webhook: {str(e)}")
        return "Error verifying webhook", 500


@app.route("/health", methods=["GET"])
def health_check():
    """Health check endpoint"""
    return jsonify({"status": "healthy"}), 200


@app.route("/", methods=["GET"])
def home():
    """Home endpoint"""
    return jsonify({
        "status": "running",
        "message": "WhatsApp Chatbot is running",
        "endpoints": {
            "webhook": "/webhook",
            "health": "/health"
        }
    }), 200


@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return jsonify({"error": "Endpoint not found"}), 404


@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    logger.error(f"Internal server error: {error}")
    return jsonify({"error": "Internal server error"}), 500


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=Config.PORT,
        debug=Config.DEBUG
    )
