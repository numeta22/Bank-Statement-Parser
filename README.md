# Bank Statement Parser

High-efficiency workflow for loading, iterating, and analysis of IBM's AML (anti money laundering) dataset. Transaction categorization, anomaly detection, and financial performance are all focal points.

## Features

- 📊 **Transaction Analysis**: Parse and analyze bank statements from multiple formats
- 🔍 **Anomaly Detection**: Identify suspicious transactions and patterns
- 🏷️ **Transaction Categorization**: Automatically categorize transactions
- 📈 **Financial Performance**: Generate insights and reports
- 🔐 **AML Compliance**: Tools for anti-money laundering analysis

## Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Setup

1. Clone the repository:
```bash
git clone https://github.com/numeta22/Bank-Statement-Parser.git
cd Bank-Statement-Parser
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

Or install in development mode:
```bash
pip install -e ".[dev]"
```

## Project Structure

```
Bank-Statement-Parser/
├── src/
│   └── bank_statement_parser/    # Main package
│       ├── __init__.py
│       ├── parser.py              # Statement parsing logic
│       ├── analyzer.py            # Transaction analysis
│       ├── categorizer.py         # Transaction categorization
│       └── utils.py               # Utility functions
├── tests/                         # Unit tests
├── data/
│   ├── raw/                       # Raw data files
│   └── processed/                 # Processed data
├── docs/                          # Documentation
├── examples/                      # Example scripts and notebooks
├── requirements.txt               # Project dependencies
├── pyproject.toml                 # Project configuration
├── LICENSE                        # MIT License
└── README.md                      # This file
```

## Usage

### Basic Example

```python
from bank_statement_parser import StatementParser, TransactionAnalyzer

# Parse a bank statement
parser = StatementParser()
transactions = parser.parse_file("path/to/statement.csv")

# Analyze transactions
analyzer = TransactionAnalyzer()
results = analyzer.analyze(transactions)

# Generate report
report = analyzer.generate_report()
print(report)
```

### Advanced Features

#### Transaction Categorization

```python
from bank_statement_parser import TransactionCategorizer

categorizer = TransactionCategorizer()
categorized_transactions = categorizer.categorize(transactions)
```

#### Anomaly Detection

```python
from bank_statement_parser import AnomalyDetector

detector = AnomalyDetector()
anomalies = detector.detect(transactions)
```

## Development

### Running Tests

```bash
pytest
```

### Code Formatting

```bash
black src/ tests/
isort src/ tests/
```

### Linting

```bash
flake8 src/ tests/
```

## Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for details.

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- IBM AML Dataset
- Contributors and maintainers

## Contact

For questions or issues, please open an issue on GitHub.

---

**Note**: This is a work in progress. Features and documentation are being actively developed.
