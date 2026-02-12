from bot.client import BinanceClient
from bot.validators import (
    validate_symbol,
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price,
)


class OrderService:
    def __init__(self):
        self.client = BinanceClient()

    def create_order(self, symbol, side, order_type, quantity, price=None):
        """
        Validates input and places order via BinanceClient.
        """

        # Validation
        validate_symbol(symbol)
        validate_side(side)
        validate_order_type(order_type)
        validate_quantity(float(quantity))
        validate_price(price, order_type)

        # Place order
        response = self.client.place_order(
            symbol=symbol,
            side=side,
            order_type=order_type,
            quantity=quantity,
            price=price,
        )

        return response