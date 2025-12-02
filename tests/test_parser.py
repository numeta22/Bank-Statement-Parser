"""
Tests for the StatementParser module.
"""

import pytest
from bank_statement_parser.parser import StatementParser, Transaction


def test_transaction_creation():
    """Test creating a Transaction object."""
    transaction = Transaction(
        date="2024-01-01",
        description="Test Transaction",
        amount=100.00,
        category="test"
    )
    
    assert transaction.date == "2024-01-01"
    assert transaction.description == "Test Transaction"
    assert transaction.amount == 100.00
    assert transaction.category == "test"


def test_parser_initialization():
    """Test StatementParser initialization."""
    parser = StatementParser()
    
    assert parser is not None
    assert len(parser.supported_formats) > 0
    assert '.csv' in parser.supported_formats


def test_parser_unsupported_format(tmp_path):
    """Test parser raises error for unsupported format."""
    parser = StatementParser()
    
    # Create a temporary file with unsupported format
    test_file = tmp_path / "test.txt"
    test_file.write_text("dummy content")
    
    with pytest.raises(ValueError):
        parser.parse_file(str(test_file))


def test_parser_file_not_found():
    """Test parser raises error for non-existent file."""
    parser = StatementParser()
    
    with pytest.raises(FileNotFoundError):
        parser.parse_file("nonexistent.csv")
