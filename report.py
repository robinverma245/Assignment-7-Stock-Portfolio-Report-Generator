"""Generate stock portfolio reports."""

from portfolio import get_stock_price, calculate_performance


def generate_report(holdings, api_key):
    """Generate a report for all portfolio holdings."""
    report = []

    for holding in holdings:
        symbol = holding["symbol"]
        units = holding["units"]
        cost = holding["cost"]

        latest_price = get_stock_price(symbol, api_key)

        performance = calculate_performance(
            units, cost, latest_price
        )

        report.append({
            "symbol": symbol,
            "units": units,
            "cost": cost,
            "latest_price": latest_price,
            **performance,
        })

    return report
