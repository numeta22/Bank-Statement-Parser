"""
Tests for the TransactionAnalyzer module.
"""

import pytest
from bank_statement_parser.analyzer import TransactionAnalyzer
from bank_statement_parser.parser import Transaction


def test_analyzer_initialization():
    """Test TransactionAnalyzer initialization."""
    analyzer = TransactionAnalyzer()
    
    assert analyzer is not None
    assert analyzer.transactions == []
    assert analyzer.analysis_results == {}


def test_analyze_empty_transactions():
    """Test analyzing empty transaction list."""
    analyzer = TransactionAnalyzer()
    results = analyzer.analyze([])
    
    assert results['total_transactions'] == 0
    assert results['total_amount'] == 0
    assert results['average_amount'] == 0.0


def test_analyze_transactions():
    """Test analyzing transaction list."""
    analyzer = TransactionAnalyzer()
    
    transactions = [
        Transaction(date="2024-01-01", description="Test 1", amount=100.0),
        Transaction(date="2024-01-02", description="Test 2", amount=200.0),
        Transaction(date="2024-01-03", description="Test 3", amount=300.0),
    ]
    
    results = analyzer.analyze(transactions)
    
    assert results['total_transactions'] == 3
    assert results['total_amount'] == 600.0
    assert results['average_amount'] == 200.0


def test_generate_report():
    """Test report generation."""
    analyzer = TransactionAnalyzer()
    
    transactions = [
        Transaction(date="2024-01-01", description="Test", amount=100.0),
    ]
    
    analyzer.analyze(transactions)
    report = analyzer.generate_report()
    
    assert "Transaction Analysis Report" in report
    assert "Total Transactions: 1" in report
