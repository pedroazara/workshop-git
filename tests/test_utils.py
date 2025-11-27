"""
Unit tests for utils module
"""

import pytest
import sys
sys.path.insert(0, '../src')

from src.utils import (
    format_currency,
    calculate_percentage_change,
    get_date_range
)


def test_format_currency_usd():
    """Test USD currency formatting."""
    result = format_currency(1234.56, 'USD')
    assert result == '$1,234.56'


def test_format_currency_eur():
    """Test EUR currency formatting."""
    result = format_currency(1234.56, 'EUR')
    assert result == '€1,234.56'


def test_format_currency_default():
    """Test default currency formatting."""
    result = format_currency(999.99)
    assert '$' in result


def test_calculate_percentage_change_increase():
    """Test percentage change calculation for increase."""
    result = calculate_percentage_change(100, 150)
    assert result == 50.0


def test_calculate_percentage_change_decrease():
    """Test percentage change calculation for decrease."""
    result = calculate_percentage_change(100, 75)
    assert result == -25.0


def test_calculate_percentage_change_zero():
    """Test percentage change with zero old value."""
    result = calculate_percentage_change(0, 100)
    assert result == 0


def test_get_date_range():
    """Test date range generation."""
    dates = get_date_range(7)

    # Should return 8 dates (including today)
    assert len(dates) == 8

    # Each element should be a string
    assert all(isinstance(d, str) for d in dates)

    # Should be in YYYY-MM-DD format
    assert all(len(d) == 10 for d in dates)


def test_get_date_range_custom_days():
    """Test date range with custom number of days."""
    dates = get_date_range(30)
    assert len(dates) == 31  # 30 days back + today


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
