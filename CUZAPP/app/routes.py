"""
Flask routes for WhatsApp webhook
"""

from flask import Blueprint, request, jsonify
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse
from app.config import Config
from app.chatbot import WhatsAppChatbot

# Initialize blueprint
api_bp = Blueprint('api', __name__)

# Initialize Twilio client
twilio_client = Client(Config.TWILIO_ACCOUNT_SID, Config.TWILIO_AUTH_TOKEN)

# Initialize chatbot
chatbot = WhatsAppChatbot()


@api_bp.route('/webhook', methods=['POST'])
def webhook():
    """
    Webhook endpoint to receive messages from Twilio
    """
    try:
        # Get incoming message details
        sender = request.values.get('From', '')
        message_body = request.values.get('Body', '').strip()
        message_sid = request.values.get('MessageSid', '')
        
        print(f"Received message from {sender}: {message_body}")
        
        # Process message through chatbot
        bot_response = chatbot.process_message(sender, message_body)
        
        # Create Twilio response
        twiml_response = MessagingResponse()
        twiml_response.message(bot_response)
        
        # Send response back through Twilio
        send_whatsapp_message(sender, bot_response)
        
        return str(twiml_response), 200
    
    except Exception as e:
        print(f"Error processing webhook: {str(e)}")
        return jsonify({'error': str(e)}), 500


@api_bp.route('/webhook', methods=['GET'])
def webhook_get():
    """
    GET endpoint for Twilio webhook verification
    """
    return jsonify({'status': 'ok'}), 200


@api_bp.route('/send-message', methods=['POST'])
def send_message():
    """
    Manual endpoint to send a message to a WhatsApp user
    """
    try:
        data = request.get_json()
        to_number = data.get('to')
        message_text = data.get('message')
        
        if not to_number or not message_text:
            return jsonify({'error': 'Missing "to" or "message" field'}), 400
        
        # Ensure to_number is in WhatsApp format
        if not to_number.startswith('whatsapp:'):
            to_number = f'whatsapp:{to_number}'
        
        send_whatsapp_message(to_number, message_text)
        
        return jsonify({
            'status': 'success',
            'message': 'Message sent successfully',
            'to': to_number
        }), 200
    
    except Exception as e:
        print(f"Error sending message: {str(e)}")
        return jsonify({'error': str(e)}), 500


@api_bp.route('/health', methods=['GET'])
def health():
    """
    Health check endpoint
    """
    return jsonify({'status': 'healthy', 'service': 'WhatsApp Chatbot'}), 200


@api_bp.route('/conversations/<phone_number>', methods=['GET'])
def get_conversation(phone_number):
    """
    Get conversation history for a specific phone number
    """
    try:
        # Format phone number
        if not phone_number.startswith('whatsapp:'):
            phone_number = f'whatsapp:{phone_number}'
        
        history = chatbot.get_conversation_history(phone_number)
        
        return jsonify({
            'phone_number': phone_number,
            'conversation': history
        }), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500


def send_whatsapp_message(to_number: str, message_text: str) -> str:
    """
    Send a WhatsApp message using Twilio
    
    Args:
        to_number: Recipient's WhatsApp number (format: whatsapp:+1234567890)
        message_text: Message content
        
    Returns:
        Message SID
    """
    try:
        message = twilio_client.messages.create(
            body=message_text,
            from_=Config.TWILIO_PHONE_NUMBER,
            to=to_number
        )
        print(f"Message sent with SID: {message.sid}")
        return message.sid
    
    except Exception as e:
        print(f"Failed to send WhatsApp message: {str(e)}")
        raise
