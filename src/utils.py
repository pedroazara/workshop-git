"""
Utility Functions
Common utility functions for data processing and manipulation.
"""

from datetime import datetime, timedelta
import json


def format_currency(amount, currency='USD'):
    """
    Format a number as currency.

    Args:
        amount (float): Amount to format
        currency (str): Currency code

    Returns:
        str: Formatted currency string
    """
    symbols = {
        'USD': '$',
        'EUR': '€',
        'GBP': '£',
        'JPY': '¥'
    }

    symbol = symbols.get(currency, '$')
    return f"{symbol}{amount:,.2f}"


def calculate_percentage_change(old_value, new_value):
    """
    Calculate percentage change between two values.

    Args:
        old_value (float): Original value
        new_value (float): New value

    Returns:
        float: Percentage change
    """
    if old_value == 0:
        return 0
    return ((new_value - old_value) / old_value) * 100


def get_date_range(days=30):
    """
    Get a date range from today going back specified days.

    Args:
        days (int): Number of days to go back

    Returns:
        list: List of date strings
    """
    end_date = datetime.now()
    start_date = end_date - timedelta(days=days)

    date_range = []
    current_date = start_date
    while current_date <= end_date:
        date_range.append(current_date.strftime('%Y-%m-%d'))
        current_date += timedelta(days=1)

    return date_range


def save_to_json(data, filename):
    """
    Save data to a JSON file.

    Args:
        data (dict): Data to save
        filename (str): Output filename
    """
    try:
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)
        print(f"Data saved to {filename}")
    except Exception as e:
        print(f"Error saving data: {e}")


def load_from_json(filename):
    """
    Load data from a JSON file.

    Args:
        filename (str): Input filename

    Returns:
        dict: Loaded data
    """
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"File {filename} not found")
        return None
    except Exception as e:
        print(f"Error loading data: {e}")
        return None


if __name__ == '__main__':
    # Test utility functions
    print("Testing utility functions:\n")

    # Currency formatting
    print(f"Currency: {format_currency(1234.56)}")
    print(f"Currency EUR: {format_currency(1234.56, 'EUR')}")

    # Percentage change
    change = calculate_percentage_change(100, 150)
    print(f"\nPercentage change: {change:.2f}%")

    # Date range
    dates = get_date_range(7)
    print(f"\nLast 7 days: {dates[:3]}... {dates[-1]}")

    # JSON operations
    sample_data = {'name': 'Workshop', 'year': 2024, 'participants': 25}
    print(f"\nSample data: {sample_data}")
