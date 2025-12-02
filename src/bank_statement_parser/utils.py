"""
Utility Functions Module

Common utility functions used across the package.
"""

import json
from pathlib import Path
from typing import List, Dict, Any
from datetime import datetime


def load_config(config_path: str) -> Dict[str, Any]:
    """
    Load configuration from JSON file.
    
    Args:
        config_path: Path to configuration file
        
    Returns:
        Dictionary containing configuration
    """
    with open(config_path, 'r') as f:
        return json.load(f)


def save_config(config: Dict[str, Any], config_path: str):
    """
    Save configuration to JSON file.
    
    Args:
        config: Configuration dictionary
        config_path: Path to save configuration
    """
    with open(config_path, 'w') as f:
        json.dump(config, f, indent=2)


def format_currency(amount: float, currency: str = "USD") -> str:
    """
    Format amount as currency string.
    
    Args:
        amount: Numeric amount
        currency: Currency code
        
    Returns:
        Formatted currency string
    """
    symbols = {
        'USD': '$',
        'EUR': '€',
        'GBP': '£',
        'JPY': '¥',
    }
    
    symbol = symbols.get(currency, currency)
    return f"{symbol}{amount:,.2f}"


def parse_date(date_str: str, format: str = "%Y-%m-%d") -> datetime:
    """
    Parse date string to datetime object.
    
    Args:
        date_str: Date string
        format: Date format string
        
    Returns:
        datetime object
    """
    return datetime.strptime(date_str, format)


def ensure_directory(directory: Path):
    """
    Ensure directory exists, create if it doesn't.
    
    Args:
        directory: Path to directory
    """
    directory = Path(directory)
    directory.mkdir(parents=True, exist_ok=True)


def get_file_extension(filepath: str) -> str:
    """
    Get file extension from filepath.
    
    Args:
        filepath: Path to file
        
    Returns:
        File extension including dot (e.g., '.csv')
    """
    return Path(filepath).suffix.lower()


def validate_transactions(transactions: List) -> bool:
    """
    Validate that all transactions have required fields.
    
    Args:
        transactions: List of transaction objects
        
    Returns:
        True if all valid, False otherwise
    """
    required_fields = ['date', 'description', 'amount']
    
    for transaction in transactions:
        for field in required_fields:
            if not hasattr(transaction, field):
                return False
    
    return True
