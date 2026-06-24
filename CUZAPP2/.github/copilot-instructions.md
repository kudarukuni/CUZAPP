# WhatsApp Chatbot Project - Copilot Instructions

This is a WhatsApp chatbot project built with Meta Cloud API and Python.

## Project Overview
- **Type**: Python Web Application (Flask)
- **Purpose**: WhatsApp chatbot using Meta's Cloud API
- **Framework**: Flask
- **Key Components**: 
  - WhatsApp API client
  - Webhook server
  - Chatbot logic engine
  - Configuration management

## Setup Completed
- ✅ Project structure created
- ✅ Dependencies configured (requirements.txt)
- ✅ Configuration management (config.py)
- ✅ WhatsApp API client (whatsapp_client.py)
- ✅ Bot logic engine (bot_logic.py)
- ✅ Flask application (app.py)
- ✅ Documentation (README.md)

## To Get Started

1. **Activate Virtual Environment** (if not already active):
   ```bash
   venv\Scripts\activate  # Windows
   # or
   source venv/bin/activate  # macOS/Linux
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Credentials**:
   - Copy `.env.example` to `.env`
   - Add your Meta Cloud API credentials
   - See README.md for how to get credentials

4. **Run the Application**:
   ```bash
   python app.py
   ```

5. **For Local Testing** (use ngrok):
   ```bash
   ngrok http 5000
   ```
   Then configure webhook URL in Meta Dashboard

## Key Files
- `app.py` - Main Flask application with webhook handlers
- `whatsapp_client.py` - Meta Cloud API client for sending messages
- `bot_logic.py` - Chatbot response logic
- `config.py` - Configuration management
- `.env` - Environment variables (create from .env.example)

## Common Tasks
- **Add new bot intents**: Edit `bot_logic.py` and add to `intents` dictionary
- **Change response logic**: Modify `ChatBot.get_response()` in `bot_logic.py`
- **Extend API methods**: Add methods to `WhatsAppClient` class
- **Update configuration**: Edit `.env` file

## API Endpoints
- `POST /webhook` - Receive messages from WhatsApp
- `GET /webhook` - Verify webhook with Meta
- `GET /health` - Health check
- `GET /` - Home endpoint

## Troubleshooting
See README.md for detailed troubleshooting guide and error solutions.
