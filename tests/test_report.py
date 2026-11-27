"""Tests for stock portfolio report generation."""

from report import generate_report


def test_generate_report(requests_mock):
    """Test report generation using mocked stock prices."""
    requests_mock.get(
        "https://www.alphavantage.co/query",
        json={"Global Quote": {"05. price": "200"}},
    )

    holdings = [
        {"symbol": "AAPL", "units": 10, "cost": 150}
    ]

    result = generate_report(holdings, "test_key")

    assert result == [
        {
            "symbol": "AAPL",
            "units": 10,
            "cost": 150,
            "latest_price": 200,
            "book_value": 1500,
            "market_value": 2000,
            "gain_loss": 500,
            "change": 500 / 1500,
        }
    ]
