"""Portfolio reading and processing functions."""

import csv


def read_portfolio(source):
    """Read stock holdings from a CSV file."""
    holdings = []

    with open(source, encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            holdings.append({
                "symbol": row["symbol"],
                "units": int(row["units"]),
                "cost": float(row["cost"]),
            })

    return holdings