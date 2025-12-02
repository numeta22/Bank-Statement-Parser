"""
Bank Statement Parser

A high-efficiency workflow for loading, iterating, and analysis of bank statements
with focus on AML (anti-money laundering) compliance, transaction categorization,
anomaly detection, and financial performance analysis.
"""

__version__ = "0.1.0"
__author__ = "Bank Statement Parser Contributors"

from .parser import StatementParser
from .analyzer import TransactionAnalyzer
from .categorizer import TransactionCategorizer
from .anomaly_detector import AnomalyDetector

__all__ = [
    "StatementParser",
    "TransactionAnalyzer",
    "TransactionCategorizer",
    "AnomalyDetector",
]
