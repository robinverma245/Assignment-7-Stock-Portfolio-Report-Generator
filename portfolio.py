"""Stock portfolio reading and performance calculations."""

import csv

import requests


def read_portfolio(source):
    """Read stock holdings from a CSV file."""
    holdings = []

    with open(source, "r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            holdings.append({
                "symbol": row["symbol"],
                "units": int(row["units"]),
                "cost": float(row["cost"]),
            })

    return holdings


def get_stock_price(symbol, api_key):
    """Retrieve the latest stock price."""
    url = "https://www.alphavantage.co/query"

    params = {
        "function": "GLOBAL_QUOTE",
        "symbol": symbol,
        "apikey": api_key,
    }

    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()
    data = response.json()

    quote = data.get("Global Quote", {})
    price = quote.get("05. price")

    if price is None:
        return None

    return float(price)


def calculate_performance(units, cost, latest_price):
    """Calculate portfolio performance metrics."""
    book_value = units * cost
    market_value = units * latest_price
    gain_loss = market_value - book_value
    change = gain_loss / book_value if book_value else 0

    return {
        "book_value": book_value,
        "market_value": market_value,
        "gain_loss": gain_loss,
        "change": change,
    }