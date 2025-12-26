# Contributing to PyAutokit

Thank you for your interest in contributing to PyAutokit! This document provides guidelines and instructions for contributing.

## 🚀 Quick Start

### 1. Fork and Clone

```bash
git clone https://github.com/YOUR_USERNAME/pyautokit.git
cd pyautokit
```

### 2. Set Up Development Environment

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install development dependencies
pip install pytest pytest-cov black flake8 mypy
```

### 3. Configure Environment

```bash
cp .env.example .env
# Edit .env with your settings
```

## 📝 Code Style

### Python Standards

- **Python Version**: 3.9+
- **Style Guide**: PEP 8
- **Docstrings**: Google-style
- **Type Hints**: Required for all functions

### Formatting

```bash
# Auto-format code
black pyautokit/
black tests/

# Check style
flake8 pyautokit/
flake8 tests/

# Type checking
mypy pyautokit/
```

### Example Code Style

```python
def process_files(
    directory: Path,
    pattern: str = "*.txt",
    recursive: bool = False
) -> List[Path]:
    """Process files in directory.
    
    Args:
        directory: Directory to process
        pattern: File pattern to match
        recursive: Search recursively
        
    Returns:
        List of processed file paths
        
    Raises:
        ValueError: If directory doesn't exist
    """
    if not directory.exists():
        raise ValueError(f"Directory not found: {directory}")
    
    # Implementation
    ...
```

## ✅ Testing

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=pyautokit --cov-report=html

# Run specific test file
pytest tests/test_file_organizer.py

# Run specific test
pytest tests/test_file_organizer.py::TestFileOrganizer::test_categorize_file

# Verbose output
pytest -v
```

### Writing Tests

1. **Place tests in** `tests/` directory
2. **Name test files** `test_*.py`
3. **Name test functions** `test_*`
4. **Use fixtures** for common setup

```python
import pytest
from pathlib import Path
from pyautokit.your_module import YourClass


@pytest.fixture
def sample_data():
    """Create sample test data."""
    return {"key": "value"}


class TestYourClass:
    """Test YourClass functionality."""
    
    def test_basic_functionality(self, sample_data):
        """Test basic functionality."""
        instance = YourClass()
        result = instance.process(sample_data)
        assert result is not None
```

## 🔨 Adding a New Module

### 1. Create Module File

```bash
touch pyautokit/your_module.py
```

### 2. Module Template

```python
"""Short description of module.

Longer description explaining what the module does,
its main features, and usage patterns.
"""

import argparse
from pathlib import Path
from typing import Dict, List, Optional
from .logger import setup_logger
from .config import Config

logger = setup_logger("YourModule", level=Config.LOG_LEVEL)


class YourClass:
    """Main class for your module."""
    
    def __init__(self, param: str = "default"):
        """Initialize your class.
        
        Args:
            param: Description of parameter
        """
        self.param = param
    
    def main_method(self, data: Dict) -> List:
        """Main functionality.
        
        Args:
            data: Input data
            
        Returns:
            Processed results
        """
        # Implementation
        pass


def main() -> None:
    """CLI entry point."""
    parser = argparse.ArgumentParser(description="Your module description")
    parser.add_argument("input", help="Input description")
    parser.add_argument("--option", help="Optional parameter")
    
    args = parser.parse_args()
    
    # Implementation
    logger.info("Module executed")


if __name__ == "__main__":
    main()
```

### 3. Add Tests

```bash
touch tests/test_your_module.py
```

### 4. Add Example

```bash
touch examples/your_example.py
```

### 5. Update Documentation

- Add to `README.md` features section
- Update `requirements.txt` if new dependencies
- Document in module docstring

## 📦 Pull Request Process

### 1. Create Feature Branch

```bash
git checkout -b feature/your-feature-name
```

### 2. Make Changes

- Write code following style guidelines
- Add tests for new functionality
- Update documentation
- Ensure all tests pass

### 3. Commit Changes

```bash
# Format commits using conventional commits
git commit -m "feat: add new feature"
git commit -m "fix: resolve bug in module"
git commit -m "docs: update README"
git commit -m "test: add tests for feature"
```

**Commit Types**:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `test`: Test additions/changes
- `refactor`: Code refactoring
- `style`: Code style changes
- `chore`: Build/tooling changes

### 4. Push and Create PR

```bash
git push origin feature/your-feature-name
```

Then create Pull Request on GitHub with:
- Clear description of changes
- Reference any related issues
- Screenshots if UI changes
- Test results

### 5. Code Review

- Address review comments
- Update PR as needed
- Ensure CI passes

## 📝 Documentation

### Module Documentation

- **Docstrings**: Required for all public functions/classes
- **Type Hints**: Required for all parameters and returns
- **Examples**: Include in docstrings when helpful

### README Updates

When adding features, update:

1. **Features section** - Add bullet point
2. **Usage section** - Add example
3. **API section** - Document new functions

## 🐛 Bug Reports

### Include in Bug Report:

1. **Description**: Clear description of the bug
2. **Steps to Reproduce**: Exact steps to reproduce
3. **Expected Behavior**: What should happen
4. **Actual Behavior**: What actually happens
5. **Environment**: OS, Python version, etc.
6. **Logs**: Relevant log output

### Template:

```markdown
**Bug Description**
A clear description of the bug.

**To Reproduce**
1. Run command '...'
2. With parameters '...'
3. See error

**Expected Behavior**
What you expected to happen.

**Environment**
- OS: [e.g., Ubuntu 22.04]
- Python: [e.g., 3.11.0]
- PyAutokit: [e.g., 1.0.0]

**Logs**
```
Paste relevant logs here
```
```

## ✨ Feature Requests

### Include in Feature Request:

1. **Use Case**: Why is this needed?
2. **Proposed Solution**: How should it work?
3. **Alternatives**: Other approaches considered
4. **Additional Context**: Any other relevant info

## 💬 Questions?

- **Issues**: [GitHub Issues](https://github.com/Gzeu/pyautokit/issues)
- **Discussions**: [GitHub Discussions](https://github.com/Gzeu/pyautokit/discussions)

## 🙏 Thank You!

Every contribution helps make PyAutokit better. Thank you for your time and effort!

---

**Happy Coding! 🚀**
