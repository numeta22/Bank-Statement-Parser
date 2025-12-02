# Contributing to Bank Statement Parser

Thank you for your interest in contributing to Bank Statement Parser! This document provides guidelines and instructions for contributing.

## Code of Conduct

- Be respectful and inclusive
- Welcome newcomers and encourage diverse perspectives
- Focus on constructive feedback
- Prioritize the community's well-being

## How to Contribute

### Reporting Bugs

1. Check if the bug has already been reported in Issues
2. If not, create a new issue with:
   - Clear, descriptive title
   - Detailed description of the problem
   - Steps to reproduce
   - Expected vs actual behavior
   - Environment details (OS, Python version, etc.)
   - Code samples or error messages

### Suggesting Enhancements

1. Check if the enhancement has been suggested
2. Create an issue describing:
   - The problem you're trying to solve
   - Your proposed solution
   - Alternative solutions you've considered
   - How it benefits the project

### Pull Requests

1. **Fork the repository** and create your branch from `main`
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes**:
   - Write clear, concise code
   - Follow the existing code style
   - Add or update tests as needed
   - Update documentation

3. **Test your changes**:
   ```bash
   pytest
   black src/ tests/
   flake8 src/ tests/
   ```

4. **Commit your changes**:
   - Use clear, descriptive commit messages
   - Reference relevant issues
   ```bash
   git commit -m "Add feature: description of feature (#issue-number)"
   ```

5. **Push to your fork** and submit a pull request

## Development Setup

1. Fork and clone the repository:
   ```bash
   git clone https://github.com/YOUR-USERNAME/Bank-Statement-Parser.git
   cd Bank-Statement-Parser
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install development dependencies:
   ```bash
   pip install -e ".[dev]"
   ```

## Code Style

- Follow PEP 8 guidelines
- Use Black for code formatting (line length: 100)
- Use isort for import sorting
- Write docstrings for all public functions and classes
- Add type hints where appropriate

### Example:

```python
def parse_transaction(data: dict) -> Transaction:
    """
    Parse a transaction from raw data.
    
    Args:
        data: Dictionary containing transaction data
        
    Returns:
        Transaction object
        
    Raises:
        ValueError: If required fields are missing
    """
    # Implementation
    pass
```

## Testing

- Write tests for all new features
- Maintain or improve code coverage
- Use pytest for testing
- Place tests in the `tests/` directory

Run tests:
```bash
pytest
pytest --cov=bank_statement_parser --cov-report=html
```

## Documentation

- Update README.md for user-facing changes
- Add docstrings to all public APIs
- Update or add examples in `examples/`
- Build documentation locally to verify changes

## Review Process

1. All submissions require review
2. Maintainers may request changes
3. Address feedback promptly
4. Once approved, a maintainer will merge your PR

## Questions?

Feel free to open an issue for questions or join discussions in existing issues.

## Recognition

Contributors will be recognized in the project documentation and release notes.

Thank you for contributing! 🎉
