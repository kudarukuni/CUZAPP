# WhatsApp Chatbot using Meta Cloud API

A Python-based WhatsApp chatbot built with Flask and Meta's Cloud API. This chatbot can receive messages, process them, and send intelligent responses.

## Features

- ✅ Receive messages from WhatsApp users
- ✅ Send text messages
- ✅ Send template messages
- ✅ Send interactive button messages
- ✅ Mark messages as read
- ✅ Extensible bot logic
- ✅ Webhook verification
- ✅ Error handling and logging

## Prerequisites

- Python 3.8+
- Meta Business Account
- WhatsApp Business Account
- Active access to Meta Cloud API
- Ngrok or similar tool for local testing (optional)

## Setup

### 1. Clone/Create the Project

```bash
cd CUZAPP2
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate the virtual environment:
- **Windows:**
  ```bash
  venv\Scripts\activate
  ```
- **macOS/Linux:**
  ```bash
  source venv/bin/activate
  ```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file based on `.env.example`:

```bash
cp .env.example .env
```

Edit `.env` and add your Meta Cloud API credentials:

```env
ACCESS_TOKEN=your_access_token_here
PHONE_NUMBER_ID=your_phone_number_id_here
BUSINESS_ACCOUNT_ID=your_business_account_id_here
VERIFY_TOKEN=your_verify_token_here
PORT=5000
DEBUG=True
```

### How to Get Your Credentials

1. **Access Token**: 
   - Go to [Meta App Dashboard](https://developers.facebook.com)
   - Select your app
   - Go to Settings > Basic
   - Create a system user and generate a token

2. **Phone Number ID**:
   - In Meta App Dashboard, go to WhatsApp > Getting Started
   - Find your phone number ID

3. **Business Account ID**:
   - In Meta App Dashboard settings, find your Business Account ID

4. **Verify Token**:
   - Create any secure random string (e.g., "my_verify_token_123")

## Running the Application

### Local Development

```bash
python app.py
```

The server will start on `http://localhost:5000`

### With Gunicorn (Production)

```bash
gunicorn -w 4 -b 0.0.0.0:5000 app.py
```

## Testing the Webhook Locally

To test locally, use **ngrok** to expose your local server:

```bash
ngrok http 5000
```

This will provide a public URL like: `https://xxxx-xx-xxx-xxx-xx.ngrok.io`

### Configure Webhook in Meta Dashboard

1. Go to [Meta App Dashboard](https://developers.facebook.com)
2. Select your app
3. Go to WhatsApp > Configuration
4. Set webhook URL to: `https://your-ngrok-url/webhook`
5. Set verify token to match your `.env` VERIFY_TOKEN
6. Subscribe to `messages` webhook

## API Endpoints

### POST /webhook
Receives incoming messages from WhatsApp

**Response:**
```json
{
  "status": "success"
}
```

### GET /webhook
Verifies the webhook endpoint

**Parameters:**
- `hub.verify_token` - Token to verify
- `hub.challenge` - Challenge string from Meta

### GET /health
Health check endpoint

**Response:**
```json
{
  "status": "healthy"
}
```

### GET /
Home endpoint

**Response:**
```json
{
  "status": "running",
  "message": "WhatsApp Chatbot is running",
  "endpoints": {...}
}
```

## Extending the Bot Logic

### Adding New Intents

Edit `bot_logic.py` and add new intents to the `intents` dictionary:

```python
chatbot.add_intent(
    intent_name="custom_intent",
    keywords=["keyword1", "keyword2"],
    response="Your response here"
)
```

### Using WhatsApp Client Methods

```python
from whatsapp_client import WhatsAppClient

client = WhatsAppClient()

# Send text message
client.send_message("1234567890", "Hello!")

# Send button message
buttons = [
    {"id": "1", "title": "Option 1"},
    {"id": "2", "title": "Option 2"}
]
client.send_button_message("1234567890", "Choose an option:", buttons)

# Send template message
client.send_template_message("1234567890", "template_name", parameters=["param1", "param2"])
```

## Project Structure

```
CUZAPP2/
├── app.py                 # Main Flask application
├── config.py             # Configuration management
├── whatsapp_client.py    # Meta Cloud API client
├── bot_logic.py          # Chatbot logic
├── requirements.txt      # Python dependencies
├── .env.example          # Example environment variables
├── README.md             # This file
└── .github/
    └── copilot-instructions.md  # Copilot instructions
```

## Error Handling

The application includes comprehensive error handling:
- Configuration validation on startup
- Webhook verification
- Message processing with error logging
- 404 and 500 error handlers

## Logging

Logs are written to console with INFO level by default. To adjust logging level, modify `app.py`:

```python
logging.basicConfig(level=logging.DEBUG)  # For more verbose logging
```

## Troubleshooting

### "Missing configuration" Error
- Ensure all required variables are set in `.env`
- Restart the application after updating `.env`

### "Invalid verify token" Error
- Verify that `VERIFY_TOKEN` in `.env` matches the webhook verify token in Meta Dashboard
- Check for whitespace or typos

### Messages Not Being Received
- Ensure webhook URL is correctly configured in Meta Dashboard
- Verify webhook is subscribed to `messages` event
- Check that phone number is properly formatted (country code + number, no +)

### 401 Unauthorized
- Check that `ACCESS_TOKEN` is valid and not expired
- Regenerate token if needed in Meta App Dashboard

## Security Notes

⚠️ **Important:**
- Never commit `.env` file with real credentials
- Keep your verify token and access token secure
- Rotate access tokens regularly
- Use environment variables for all sensitive data

## Next Steps

1. Integrate with a database to store conversation history
2. Add AI/ML capabilities for smarter responses
3. Implement NLP for better intent detection
4. Add support for media messages (images, documents)
5. Create admin dashboard for bot management

## Resources

- [Meta Cloud API Documentation](https://developers.facebook.com/docs/whatsapp/cloud-api)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [WhatsApp Business Platform](https://www.whatsapp.com/business)

## License

MIT License

## Support

For issues or questions, refer to the Meta Cloud API documentation or the project's README.
