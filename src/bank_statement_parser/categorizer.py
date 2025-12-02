"""
Transaction Categorizer Module

Automatically categorizes transactions based on description and amount patterns.
"""

from typing import List, Dict
from .parser import Transaction


class TransactionCategorizer:
    """
    Categorize bank transactions based on patterns and rules.
    
    Uses keyword matching and amount patterns to assign categories
    to transactions.
    """
    
    def __init__(self):
        self.categories = self._initialize_categories()
    
    def _initialize_categories(self) -> Dict[str, List[str]]:
        """
        Initialize default category keywords.
        
        Returns:
            Dictionary mapping categories to keyword lists
        """
        return {
            'groceries': ['grocery', 'supermarket', 'walmart', 'target', 'food'],
            'dining': ['restaurant', 'cafe', 'coffee', 'pizza', 'burger'],
            'utilities': ['electric', 'water', 'gas', 'internet', 'phone'],
            'transportation': ['gas station', 'uber', 'lyft', 'transit', 'parking'],
            'entertainment': ['netflix', 'spotify', 'movie', 'game', 'subscription'],
            'healthcare': ['pharmacy', 'doctor', 'hospital', 'medical', 'health'],
            'shopping': ['amazon', 'ebay', 'shop', 'store', 'retail'],
            'income': ['salary', 'payroll', 'deposit', 'payment received'],
            'transfer': ['transfer', 'atm withdrawal'],
            'other': []
        }
    
    def categorize(self, transactions: List[Transaction]) -> List[Transaction]:
        """
        Categorize a list of transactions.
        
        Args:
            transactions: List of Transaction objects to categorize
            
        Returns:
            List of Transaction objects with categories assigned
        """
        for transaction in transactions:
            if transaction.category is None:
                transaction.category = self._categorize_single(transaction)
        
        return transactions
    
    def _categorize_single(self, transaction: Transaction) -> str:
        """
        Categorize a single transaction.
        
        Args:
            transaction: Transaction object to categorize
            
        Returns:
            Category name as string
        """
        description = str(transaction.description).lower()
        
        # Check each category's keywords
        for category, keywords in self.categories.items():
            if category == 'other':
                continue
            
            for keyword in keywords:
                if keyword.lower() in description:
                    return category
        
        # Default to 'other' if no match found
        return 'other'
    
    def add_category_rule(self, category: str, keywords: List[str]):
        """
        Add or update a category with new keywords.
        
        Args:
            category: Category name
            keywords: List of keywords for this category
        """
        if category in self.categories:
            self.categories[category].extend(keywords)
        else:
            self.categories[category] = keywords
    
    def get_category_summary(self, transactions: List[Transaction]) -> Dict[str, Dict]:
        """
        Generate summary statistics by category.
        
        Args:
            transactions: List of categorized transactions
            
        Returns:
            Dictionary with category statistics
        """
        summary = {}
        
        for transaction in transactions:
            category = transaction.category or 'uncategorized'
            
            if category not in summary:
                summary[category] = {
                    'count': 0,
                    'total_amount': 0.0,
                    'average_amount': 0.0
                }
            
            summary[category]['count'] += 1
            summary[category]['total_amount'] += transaction.amount or 0.0
        
        # Calculate averages
        for category in summary:
            if summary[category]['count'] > 0:
                summary[category]['average_amount'] = (
                    summary[category]['total_amount'] / summary[category]['count']
                )
        
        return summary
