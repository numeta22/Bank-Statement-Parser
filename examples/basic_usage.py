"""
Basic usage example for Bank Statement Parser.
"""

from bank_statement_parser import (
    StatementParser,
    TransactionAnalyzer,
    TransactionCategorizer,
    AnomalyDetector
)


def main():
    # Example: Parse a bank statement
    print("=" * 60)
    print("Bank Statement Parser - Basic Example")
    print("=" * 60)
    
    # Initialize components
    parser = StatementParser()
    analyzer = TransactionAnalyzer()
    categorizer = TransactionCategorizer()
    detector = AnomalyDetector()
    
    print("\nComponents initialized successfully!")
    print(f"Supported file formats: {parser.supported_formats}")
    
    # Note: This is a template example
    # In real usage, you would parse an actual file:
    # transactions = parser.parse_file("path/to/statement.csv")
    
    print("\nTo use this library:")
    print("1. Prepare your bank statement in CSV, Excel, or PDF format")
    print("2. Use StatementParser to parse the file")
    print("3. Use TransactionAnalyzer for insights")
    print("4. Use TransactionCategorizer to categorize transactions")
    print("5. Use AnomalyDetector to find suspicious transactions")
    
    print("\n" + "=" * 60)
    print("Example completed!")
    print("=" * 60)


if __name__ == "__main__":
    main()
