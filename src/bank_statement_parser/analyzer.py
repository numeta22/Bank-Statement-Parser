"""
Transaction Analyzer Module

Provides analysis capabilities for bank transactions including
statistical analysis, pattern recognition, and reporting.
"""

import pandas as pd
from typing import List, Dict
from .parser import Transaction


class TransactionAnalyzer:
    """
    Analyze bank transactions for insights and patterns.
    
    Provides methods for statistical analysis, trend detection,
    and report generation.
    """
    
    def __init__(self):
        self.transactions = []
        self.analysis_results = {}
    
    def analyze(self, transactions: List[Transaction]) -> Dict:
        """
        Perform comprehensive analysis on transactions.
        
        Args:
            transactions: List of Transaction objects to analyze
            
        Returns:
            Dictionary containing analysis results
        """
        self.transactions = transactions
        
        results = {
            'total_transactions': len(transactions),
            'total_amount': self._calculate_total_amount(),
            'average_amount': self._calculate_average_amount(),
            'date_range': self._get_date_range(),
            'summary_statistics': self._get_summary_statistics(),
        }
        
        self.analysis_results = results
        return results
    
    def _calculate_total_amount(self) -> float:
        """Calculate total amount of all transactions."""
        return sum(t.amount for t in self.transactions if t.amount is not None)
    
    def _calculate_average_amount(self) -> float:
        """Calculate average transaction amount."""
        if not self.transactions:
            return 0.0
        total = self._calculate_total_amount()
        return total / len(self.transactions)
    
    def _get_date_range(self) -> Dict:
        """Get the date range of transactions."""
        if not self.transactions:
            return {'start': None, 'end': None}
        
        dates = [t.date for t in self.transactions if t.date is not None]
        if not dates:
            return {'start': None, 'end': None}
        
        return {
            'start': min(dates),
            'end': max(dates)
        }
    
    def _get_summary_statistics(self) -> Dict:
        """Calculate summary statistics for transactions."""
        amounts = [t.amount for t in self.transactions if t.amount is not None]
        
        if not amounts:
            return {}
        
        df = pd.DataFrame({'amount': amounts})
        stats = df.describe()
        
        return {
            'count': stats.loc['count', 'amount'],
            'mean': stats.loc['mean', 'amount'],
            'std': stats.loc['std', 'amount'],
            'min': stats.loc['min', 'amount'],
            'max': stats.loc['max', 'amount'],
        }
    
    def generate_report(self) -> str:
        """
        Generate a formatted text report of analysis results.
        
        Returns:
            Formatted string report
        """
        if not self.analysis_results:
            return "No analysis results available. Run analyze() first."
        
        report = []
        report.append("=" * 50)
        report.append("Transaction Analysis Report")
        report.append("=" * 50)
        report.append(f"Total Transactions: {self.analysis_results.get('total_transactions', 0)}")
        report.append(f"Total Amount: ${self.analysis_results.get('total_amount', 0):.2f}")
        report.append(f"Average Amount: ${self.analysis_results.get('average_amount', 0):.2f}")
        
        date_range = self.analysis_results.get('date_range', {})
        if date_range.get('start') and date_range.get('end'):
            report.append(f"Date Range: {date_range['start']} to {date_range['end']}")
        
        report.append("=" * 50)
        
        return "\n".join(report)
