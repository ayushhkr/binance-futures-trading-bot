Binance Futures Testnet Trading Bot
Overview

This project is a simplified trading bot built in Python that places MARKET and LIMIT orders on Binance Futures Testnet (USDT-M).

The application follows a modular structure with:

API client layer

Order logic layer

Input validation

CLI interface

Structured logging

Exception handling

Features

Place MARKET orders

Place LIMIT orders

Support BUY and SELL

CLI-based user input

Input validation

Logging of API requests and responses

Error handling

Project Structure
trading_bot/
│
├── bot/
│ ├── client.py
│ ├── orders.py
│ ├── validators.py
│ ├── logging_config.py
│
├── cli.py
├── requirements.txt
├── README.md
Setup Instructions

1. Create Binance Futures Testnet Account

Generate API credentials from Binance Futures Testnet.

2. Create .env file in project root
   API_KEY=your_api_key
   API_SECRET=your_secret_key
3. Create virtual environment

Windows:

python -m venv venv
venv\Scripts\activate 4. Install dependencies
pip install -r requirements.txt
Usage
Place MARKET Order
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.002
Place LIMIT Order
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.002 --price 90000
Logging

All API requests, responses, and errors are logged to:

trading.log
Assumptions

USDT-M Futures only

Default leverage and margin mode

Binance minimum notional rules apply
