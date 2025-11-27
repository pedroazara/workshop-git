"""
Data Analysis Example Script
Demonstrates basic data analysis operations using pandas and numpy.
"""

import pandas as pd
import numpy as np


def generate_sample_data(n_rows=100):
    """
    Generate sample data for demonstration.

    Args:
        n_rows (int): Number of rows to generate

    Returns:
        pd.DataFrame: Sample dataset
    """
    np.random.seed(42)

    data = {
        'id': range(1, n_rows + 1),
        'name': [f'User_{i}' for i in range(1, n_rows + 1)],
        'age': np.random.randint(18, 70, n_rows),
        'score': np.random.normal(75, 15, n_rows).round(2),
        'category': np.random.choice(['A', 'B', 'C', 'D'], n_rows),
        'active': np.random.choice([True, False], n_rows)
    }

    return pd.DataFrame(data)


def analyze_data(df):
    """
    Perform basic data analysis.

    Args:
        df (pd.DataFrame): Input dataframe

    Returns:
        dict: Analysis results
    """
    results = {
        'total_records': len(df),
        'average_age': df['age'].mean(),
        'average_score': df['score'].mean(),
        'category_distribution': df['category'].value_counts().to_dict(),
        'active_users': df['active'].sum(),
        'score_stats': df['score'].describe().to_dict()
    }

    return results


def filter_high_performers(df, threshold=80):
    """
    Filter users with scores above threshold.

    Args:
        df (pd.DataFrame): Input dataframe
        threshold (float): Score threshold

    Returns:
        pd.DataFrame: Filtered dataframe
    """
    return df[df['score'] >= threshold]


if __name__ == '__main__':
    # Generate sample data
    print("Generating sample data...")
    df = generate_sample_data(100)

    # Display first few rows
    print("\nFirst 5 rows:")
    print(df.head())

    # Analyze data
    print("\nData Analysis:")
    results = analyze_data(df)
    for key, value in results.items():
        print(f"{key}: {value}")

    # Filter high performers
    print("\nHigh Performers (score >= 80):")
    high_performers = filter_high_performers(df, 80)
    print(f"Number of high performers: {len(high_performers)}")
    print(high_performers[['name', 'score']].head())
