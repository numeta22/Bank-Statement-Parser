"""
Statement Parser Module

Handles parsing of bank statements from various formats (CSV, Excel, PDF).
"""

import pandas as pd
from typing import List, Dict, Union
from pathlib import Path


class Transaction:
    """Represents a single bank transaction."""
    
    def __init__(self, date, description, amount, category=None, **kwargs):
        self.date = date
        self.description = description
        self.amount = amount
        self.category = category
        self.metadata = kwargs
    
    def __repr__(self):
        return f"Transaction(date={self.date}, amount={self.amount}, desc={self.description})"


class StatementParser:
    """
    Parse bank statements from various file formats.
    
    Supports CSV, Excel (XLSX, XLS), and PDF formats.
    """
    
    def __init__(self):
        self.supported_formats = ['.csv', '.xlsx', '.xls', '.pdf']
    
    def parse_file(self, filepath: Union[str, Path]) -> List[Transaction]:
        """
        Parse a bank statement file.
        
        Args:
            filepath: Path to the statement file
            
        Returns:
            List of Transaction objects
            
        Raises:
            ValueError: If file format is not supported
            FileNotFoundError: If file doesn't exist
        """
        filepath = Path(filepath)
        
        if not filepath.exists():
            raise FileNotFoundError(f"File not found: {filepath}")
        
        if filepath.suffix.lower() not in self.supported_formats:
            raise ValueError(f"Unsupported format: {filepath.suffix}")
        
        if filepath.suffix == '.csv':
            return self._parse_csv(filepath)
        elif filepath.suffix in ['.xlsx', '.xls']:
            return self._parse_excel(filepath)
        elif filepath.suffix == '.pdf':
            return self._parse_pdf(filepath)
    
    def _parse_csv(self, filepath: Path) -> List[Transaction]:
        """Parse CSV format bank statement."""
        # TODO: Implement CSV parsing logic
        df = pd.read_csv(filepath)
        return self._dataframe_to_transactions(df)
    
    def _parse_excel(self, filepath: Path) -> List[Transaction]:
        """Parse Excel format bank statement."""
        # TODO: Implement Excel parsing logic
        df = pd.read_excel(filepath)
        return self._dataframe_to_transactions(df)
    
    def _parse_pdf(self, filepath: Path) -> List[Transaction]:
        """Parse PDF format bank statement."""
        # TODO: Implement PDF parsing logic
        raise NotImplementedError("PDF parsing not yet implemented")
    
    def _dataframe_to_transactions(self, df: pd.DataFrame) -> List[Transaction]:
        """Convert pandas DataFrame to list of Transaction objects."""
        transactions = []
        for _, row in df.iterrows():
            # TODO: Map DataFrame columns to Transaction fields
            transaction = Transaction(
                date=row.get('date'),
                description=row.get('description'),
                amount=row.get('amount')
            )
            transactions.append(transaction)
        return transactions
