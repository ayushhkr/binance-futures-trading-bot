def validate_symbol(symbol: str):
    if not symbol or not isinstance(symbol, str):
        raise ValueError("Symbol must be a non-empty string")


def validate_side(side: str):
    if side not in ["BUY", "SELL"]:
        raise ValueError("Side must be either BUY or SELL")


def validate_order_type(order_type: str):
    if order_type not in ["MARKET", "LIMIT"]:
        raise ValueError("Order type must be MARKET or LIMIT")


def validate_quantity(quantity: float):
    if quantity <= 0:
        raise ValueError("Quantity must be greater than 0")


def validate_price(price, order_type):
    if order_type == "LIMIT":
        if price is None:
            raise ValueError("Price is required for LIMIT orders")
        if float(price) <= 0:
            raise ValueError("Price must be greater than 0")