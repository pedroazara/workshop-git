"""
Data Visualization Example Script
Demonstrates data visualization using matplotlib and seaborn.
"""

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd


def create_sample_data():
    """Generate sample data for visualization."""
    np.random.seed(42)

    dates = pd.date_range('2024-01-01', periods=30, freq='D')
    data = {
        'date': dates,
        'sales': np.random.randint(100, 500, 30) + np.arange(30) * 5,
        'expenses': np.random.randint(50, 300, 30),
        'visitors': np.random.randint(200, 1000, 30)
    }

    return pd.DataFrame(data)


def plot_time_series(df, save_path='data/time_series.png'):
    """
    Create a time series plot.

    Args:
        df (pd.DataFrame): Input dataframe
        save_path (str): Path to save the plot
    """
    plt.figure(figsize=(12, 6))

    plt.plot(df['date'], df['sales'], marker='o', label='Sales', linewidth=2)
    plt.plot(df['date'], df['expenses'], marker='s', label='Expenses', linewidth=2)

    plt.title('Sales and Expenses Over Time', fontsize=16, fontweight='bold')
    plt.xlabel('Date', fontsize=12)
    plt.ylabel('Amount ($)', fontsize=12)
    plt.legend(loc='upper left')
    plt.grid(True, alpha=0.3)
    plt.xticks(rotation=45)
    plt.tight_layout()

    try:
        plt.savefig(save_path, dpi=150, bbox_inches='tight')
        print(f"Plot saved to {save_path}")
    except Exception as e:
        print(f"Could not save plot: {e}")

    plt.close()


def plot_distribution(df, save_path='data/distribution.png'):
    """
    Create distribution plots.

    Args:
        df (pd.DataFrame): Input dataframe
        save_path (str): Path to save the plot
    """
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    # Histogram
    axes[0].hist(df['sales'], bins=15, color='skyblue', edgecolor='black', alpha=0.7)
    axes[0].set_title('Sales Distribution', fontsize=14, fontweight='bold')
    axes[0].set_xlabel('Sales ($)')
    axes[0].set_ylabel('Frequency')
    axes[0].grid(True, alpha=0.3)

    # Box plot
    data_to_plot = [df['sales'], df['expenses'], df['visitors']]
    axes[1].boxplot(data_to_plot, labels=['Sales', 'Expenses', 'Visitors'])
    axes[1].set_title('Data Comparison', fontsize=14, fontweight='bold')
    axes[1].set_ylabel('Values')
    axes[1].grid(True, alpha=0.3)

    plt.tight_layout()

    try:
        plt.savefig(save_path, dpi=150, bbox_inches='tight')
        print(f"Plot saved to {save_path}")
    except Exception as e:
        print(f"Could not save plot: {e}")

    plt.close()


def create_correlation_heatmap(df, save_path='data/correlation.png'):
    """
    Create a correlation heatmap.

    Args:
        df (pd.DataFrame): Input dataframe
        save_path (str): Path to save the plot
    """
    # Select numeric columns
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    corr_matrix = df[numeric_cols].corr()

    plt.figure(figsize=(8, 6))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0,
                square=True, linewidths=1, cbar_kws={"shrink": 0.8})
    plt.title('Correlation Matrix', fontsize=16, fontweight='bold')
    plt.tight_layout()

    try:
        plt.savefig(save_path, dpi=150, bbox_inches='tight')
        print(f"Plot saved to {save_path}")
    except Exception as e:
        print(f"Could not save plot: {e}")

    plt.close()


if __name__ == '__main__':
    # Create sample data
    print("Creating sample data...")
    df = create_sample_data()

    print("\nDataset preview:")
    print(df.head())

    # Create visualizations
    print("\nGenerating visualizations...")
    plot_time_series(df)
    plot_distribution(df)
    create_correlation_heatmap(df)

    print("\nVisualization complete!")
