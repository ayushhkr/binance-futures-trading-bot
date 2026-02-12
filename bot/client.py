import os
from dotenv import load_dotenv
from binance.client import Client
from bot.logging_config import setup_logger

load_dotenv()
logger = setup_logger()


class BinanceClient:
    def __init__(self):
        self.api_key = os.getenv("API_KEY")
        self.api_secret = os.getenv("API_SECRET")

        if not self.api_key or not self.api_secret:
            raise ValueError("API_KEY and API_SECRET must be set in .env file")

        # Official Binance Futures Testnet
        self.client = Client(
            self.api_key,
            self.api_secret,
            testnet=True
        )

    def place_order(self, symbol, side, order_type, quantity, price=None):
        """
        Place order on Binance Futures Testnet.
        Supports MARKET, LIMIT, and STOP_MARKET orders.
        """

        try:
            logger.info(
                f"Placing order | Symbol: {symbol}, Side: {side}, "
                f"Type: {order_type}, Qty: {quantity}, Price: {price}"
            )

            # MARKET ORDER
            if order_type == "MARKET":
                response = self.client.futures_create_order(
                    symbol=symbol,
                    side=side,
                    type="MARKET",
                    quantity=quantity,
                )

            # LIMIT ORDER
            elif order_type == "LIMIT":
                if price is None:
                    raise ValueError("Price is required for LIMIT orders")

                response = self.client.futures_create_order(
                    symbol=symbol,
                    side=side,
                    type="LIMIT",
                    quantity=quantity,
                    price=price,
                    timeInForce="GTC",
                )

            # STOP_MARKET ORDER
            elif order_type == "STOP_MARKET":
                if price is None:
                    raise ValueError("Stop price is required for STOP_MARKET orders")

                response = self.client.futures_create_order(
                    symbol=symbol,
                    side=side,
                    type="STOP_MARKET",
                    stopPrice=price,
                    quantity=quantity,
                    workingType="CONTRACT_PRICE",
                    reduceOnly=False,
                    
                )

            else:
                raise ValueError("Invalid order type")

            logger.info(f"Order response: {response}")
            return response

        except Exception as e:
            logger.exception(f"Error placing order: {str(e)}")
            raise