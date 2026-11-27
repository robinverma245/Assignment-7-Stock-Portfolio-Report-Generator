"""Tests for portfolio operations."""

from portfolio import read_portfolio, get_stock_price, calculate_performance


def test_read_portfolio(tmp_path):
    """Test reading stock holdings from a CSV file."""
    source = tmp_path / "portfolio.csv"
    source.write_text(
        "symbol,units,cost\nAAPL,10,150\n",
        encoding="utf-8",
    )

    result = read_portfolio(source)

    assert result == [
        {"symbol": "AAPL", "units": 10, "cost": 150.0}
    ]


def test_get_stock_price(requests_mock):
    """Test retrieving a stock price using a mocked API."""
    requests_mock.get(
        "https://www.alphavantage.co/query",
        json={
            "Global Quote": {
                "05. price": "204.29"
            }
        },
    )

    assert get_stock_price("AAPL", "test_key") == 204.29
def test_calculate_performance():
    """Test portfolio performance calculations."""


    result = calculate_performance(10, 150, 200)

    assert result["book_value"] == 1500
    assert result["market_value"] == 2000
    assert result["gain_loss"] == 500
    assert result["change"] == 500 / 1500
