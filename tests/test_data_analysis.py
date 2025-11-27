"""
Unit tests for data_analysis module
"""

import pytest
import pandas as pd
import sys
sys.path.insert(0, '../src')

from src.data_analysis import generate_sample_data, analyze_data, filter_high_performers


def test_generate_sample_data():
    """Test sample data generation."""
    df = generate_sample_data(50)

    assert len(df) == 50
    assert 'id' in df.columns
    assert 'name' in df.columns
    assert 'age' in df.columns
    assert 'score' in df.columns
    assert 'category' in df.columns
    assert 'active' in df.columns


def test_analyze_data():
    """Test data analysis function."""
    df = generate_sample_data(100)
    results = analyze_data(df)

    assert 'total_records' in results
    assert results['total_records'] == 100
    assert 'average_age' in results
    assert 'average_score' in results
    assert 'category_distribution' in results
    assert isinstance(results['category_distribution'], dict)


def test_filter_high_performers():
    """Test high performers filter."""
    df = generate_sample_data(100)
    high_performers = filter_high_performers(df, threshold=80)

    # All filtered records should have score >= 80
    assert all(high_performers['score'] >= 80)

    # Should return a DataFrame
    assert isinstance(high_performers, pd.DataFrame)


def test_filter_high_performers_threshold():
    """Test different thresholds."""
    df = generate_sample_data(100)

    threshold_90 = filter_high_performers(df, threshold=90)
    threshold_70 = filter_high_performers(df, threshold=70)

    # Higher threshold should return fewer results
    assert len(threshold_90) <= len(threshold_70)


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
