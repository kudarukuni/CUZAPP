# WhatsApp Chatbot with Python and Twilio

A modern WhatsApp chatbot application built with Python, Flask, and Twilio that enables automated conversational interactions through WhatsApp.

## 🚀 Features

- **WhatsApp Integration**: Seamless integration with Twilio's WhatsApp Business API
- **Flask Server**: RESTful API endpoints for webhook handling
- **Conversational AI**: Dynamic chatbot responses with conversation history tracking
- **Easy Configuration**: Environment-based configuration management
- **Command-based Responses**: Pre-built commands (hello, help, time, info)
- **Extensible Architecture**: Easily add custom responses and AI integrations
- **Health Monitoring**: Built-in health check endpoint

## 📋 Prerequisites

- Python 3.8 or higher
- Twilio Account with WhatsApp sandbox or Business Account
- pip (Python package manager)
- ngrok (for local testing) or a public server

## 🔧 Setup Instructions

### 1. Clone or Download the Project

```bash
cd c:\Users\WVA\Desktop\CUZAPP
```

### 2. Create Virtual Environment

```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Copy `.env.example` to `.env` and fill in your Twilio credentials:

```bash
cp .env.example .env
```

Edit `.env` with your credentials:

```env
TWILIO_ACCOUNT_SID=ACxxxxxxxxxxxxxxxxxxxx
TWILIO_AUTH_TOKEN=your_auth_token_here
TWILIO_PHONE_NUMBER=whatsapp:+1234567890
FLASK_ENV=development
FLASK_DEBUG=True
PORT=5000
WEBHOOK_URL=http://localhost:5000/webhook
```

### 5. Get Your Twilio Credentials

1. Go to [Twilio Console](https://console.twilio.com)
2. Navigate to **Account Info** to get `ACCOUNT_SID` and `AUTH_TOKEN`
3. Go to **Messaging → Services** and create or select a WhatsApp service
4. Get your WhatsApp sandbox number or business number

## 🏃 Running the Application

### Development Mode

```bash
python app.py
```

The server will start on `http://localhost:5000`

### Using ngrok for Local Testing

To test with Twilio webhooks locally:

```bash
# In a new terminal
ngrok http 5000
```

This will give you a public URL like `https://xxxx-xx-xxx-xx.ngrok.io`

### 5. Configure Twilio Webhook

1. Go to [Twilio Console](https://console.twilio.com)
2. Navigate to **Messaging → Services → Your Service**
3. Go to **Integration**
4. Set the webhook URL to: `https://your-ngrok-url.ngrok.io/webhook` (or your production URL)
5. Select **Webhooks** as the integration type

## 📡 API Endpoints

### Webhook (POST)
Receives messages from Twilio

```
POST /webhook
```

**Request:**
- Automatically handled by Twilio

**Response:**
- TwiML response with chatbot message

### Send Message (POST)
Send a manual message to a WhatsApp user

```
POST /send-message
Content-Type: application/json

{
  "to": "+1234567890",
  "message": "Hello from the chatbot!"
}
```

### Get Conversation History (GET)
Retrieve conversation history with a user

```
GET /conversations/<phone_number>
```

**Response:**
```json
{
  "phone_number": "whatsapp:+1234567890",
  "conversation": [
    {"type": "user", "text": "hello"},
    {"type": "bot", "text": "Hello! How can I help?"}
  ]
}
```

### Health Check (GET)
Check if the service is running

```
GET /health
```

**Response:**
```json
{
  "status": "healthy",
  "service": "WhatsApp Chatbot"
}
```

## 🎯 Testing

### 1. Manual Testing with Twilio

1. Save your Twilio phone number's contact as "Twilio" in WhatsApp
2. Send a message to it
3. You should receive an automated response from the chatbot

### 2. Test Commands

Try these commands:
- `hello` - Greeting
- `help` - Show available commands
- `info` - About the chatbot
- `time` - Current time
- Any text - Generic response

## 🤖 Customizing the Chatbot

Edit the `app/chatbot.py` file to add custom responses:

```python
def generate_response(self, message: str, sender: str) -> str:
    if "custom" in message:
        return "Custom response here!"
    # ... rest of the logic
```

### Adding AI Integration

To integrate with an AI service like OpenAI:

```bash
pip install openai
```

Then modify `generate_response()` to use the AI API:

```python
import openai

def generate_response(self, message: str, sender: str) -> str:
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": message}]
    )
    return response.choices[0].message.content
```

## 📦 Project Structure

```
CUZAPP/
├── app/
│   ├── __init__.py          # Flask app factory
│   ├── config.py            # Configuration management
│   ├── chatbot.py           # Chatbot logic
│   └── routes.py            # API endpoints
├── app.py                   # Main entry point
├── requirements.txt         # Python dependencies
├── .env.example             # Environment variables template
├── .env                     # Environment variables (local only)
└── README.md               # This file
```

## 🔐 Security Notes

- Never commit `.env` files containing real credentials
- Use environment variables for all sensitive data
- Validate all incoming messages
- Implement rate limiting for production
- Use HTTPS in production
- Keep dependencies updated

## 🚀 Deployment

### Heroku

```bash
# Login to Heroku
heroku login

# Create a new Heroku app
heroku create your-app-name

# Add Procfile
echo "web: python app.py" > Procfile

# Deploy
git push heroku main
```

### AWS, DigitalOcean, Google Cloud

See the cloud provider's documentation for Python Flask deployment.

## 🐛 Troubleshooting

### "Missing required environment variable"
- Make sure `.env` file exists and has all required variables
- Check that variables are in the correct format

### "Webhook not connecting"
- Verify your ngrok URL is correct
- Check Twilio webhook configuration
- Ensure Flask app is running

### "Messages not sending"
- Verify Twilio credentials are correct
- Check WhatsApp number format
- Review Twilio logs for errors

## 📚 Resources

- [Twilio Documentation](https://www.twilio.com/docs)
- [Twilio WhatsApp API](https://www.twilio.com/docs/whatsapp)
- [Flask Documentation](https://flask.palletsprojects.com)
- [Python-dotenv](https://github.com/theskumar/python-dotenv)

## 📝 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Feel free to fork this project and submit pull requests for any improvements!

## 📧 Support

For issues and questions:
- Check the troubleshooting section
- Review Twilio logs
- Check Flask app logs for detailed errors

---

**Happy Chatting! 🚀**
