# WhatsApp Chatbot Project - Development Instructions

This project is a WhatsApp chatbot built with Python, Flask, and Twilio.

## Project Overview

- **Type**: Python Flask Application
- **Purpose**: WhatsApp chatbot with Twilio integration
- **Main Features**: Message handling, conversation tracking, extensible chatbot logic

## Development Checklist

- [x] Project structure created
- [x] Core modules implemented (Flask app, chatbot, routes)
- [x] Twilio integration configured
- [x] Environment configuration setup
- [ ] Dependencies installed
- [ ] Application tested
- [ ] Twilio webhook configured

## Quick Start

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure Environment**:
   - Copy `.env.example` to `.env`
   - Add your Twilio credentials

3. **Run the Application**:
   ```bash
   python app.py
   ```

4. **Setup Webhooks**:
   - Use ngrok: `ngrok http 5000`
   - Configure webhook in Twilio console

## File Structure

```
app/
  ├── __init__.py       - Flask app factory
  ├── config.py         - Configuration
  ├── chatbot.py        - Chatbot logic
  └── routes.py         - API endpoints
app.py                  - Entry point
requirements.txt        - Dependencies
.env.example           - Configuration template
README.md              - Full documentation
```

## Key Endpoints

- `POST /webhook` - Receive WhatsApp messages
- `POST /send-message` - Send manual messages
- `GET /health` - Health check
- `GET /conversations/<number>` - Get conversation history

## Next Steps

1. Install all dependencies
2. Set up your `.env` file with Twilio credentials
3. Test locally with ngrok
4. Configure Twilio webhook
5. Deploy to production
