"""Tests for portfolio operations."""

from portfolio import read_portfolio


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
