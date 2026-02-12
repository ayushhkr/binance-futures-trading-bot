import argparse
from bot.orders import OrderService


def main():
    parser = argparse.ArgumentParser(description="Binance Futures Testnet Trading Bot")

    parser.add_argument("--symbol", required=True, help="Trading symbol (e.g., BTCUSDT)")
    parser.add_argument("--side", required=True, help="BUY or SELL")
    parser.add_argument("--type", required=True, help="MARKET, LIMIT, or STOP_MARKET")
    parser.add_argument("--quantity", required=True, type=float, help="Order quantity")
    parser.add_argument("--price", type=float, help="Price (required for LIMIT orders)")

    args = parser.parse_args()

    service = OrderService()

    try:
        response = service.create_order(
            symbol=args.symbol,
            side=args.side.upper(),
            order_type=args.type.upper(),
            quantity=args.quantity,
            price=args.price,
        )


        
        print("\n===== ORDER RESPONSE =====")
        print(f"Symbol: {response.get('symbol')}")
        print(f"Order ID: {response.get('orderId')}")
        print(f"Status: {response.get('status')}")
        print(f"Side: {response.get('side')}")
        print(f"Type: {response.get('type')}")
        print(f"Original Qty: {response.get('origQty')}")
        print(f"Executed Qty: {response.get('executedQty')}")
        print(f"Avg Price: {response.get('avgPrice')}")
        print("==========================\n")

    except Exception as e:
        print(f"Error: {str(e)}")


if __name__ == "__main__":
    main()