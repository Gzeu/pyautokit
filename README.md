# PyAutokit 🚀

**Python Automation Toolkit** - A comprehensive, production-ready collection of automation utilities for everyday tasks.

[![PyPI version](https://badge.fury.io/py/pyautokit.svg)](https://badge.fury.io/py/pyautokit)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Tests](https://img.shields.io/github/actions/workflow/status/Gzeu/pyautokit/tests.yml?branch=main&label=tests)](https://github.com/Gzeu/pyautokit/actions)
[![Code Style: Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Downloads](https://pepy.tech/badge/pyautokit)](https://pepy.tech/project/pyautokit)

## 🎯 Overview

PyAutokit is a modular Python toolkit designed to automate common development and operations tasks. **Each module has a complete CLI** with argparse and can be used programmatically. All modules are standalone, well-documented, and tested.

## 📦 Installation

### From PyPI (Recommended)

```bash
pip install pyautokit
```

That's it! All commands are now available:

```bash
pyautokit --version
pyautokit-organizer ~/Downloads --dry-run
pyautokit-crypto --coin EGLD
pyautokit-security genpass --length 20
```

### From Source

```bash
git clone https://github.com/Gzeu/pyautokit.git
cd pyautokit
pip install -e .
```

### With Optional Dependencies

```bash
# File watching support (for auto-organize)
pip install pyautokit[watch]

# Development tools
pip install pyautokit[dev]

# Everything
pip install pyautokit[all]
```

See [INSTALLATION.md](INSTALLATION.md) for detailed installation guide.

## ⚡ Quick Start

```bash
# After installation, try these commands:

# Organize your Downloads folder
pyautokit-organizer ~/Downloads --method category --dry-run

# Check EGLD price
pyautokit-crypto --coin EGLD

# Generate secure password
pyautokit-security genpass --length 20

# Convert CSV to JSON
pyautokit-data convert data.csv --to json

# Create backup
pyautokit-backup create ./myproject --compression tar.gz
```

## ✨ Features

### 📁 File Organizer
- Organize files by extension, date, category, or size
- Smart categorization (Documents, Images, Videos, Code, etc.)
- Dry-run mode for safe testing
- Auto-watch mode for continuous organization
- Duplicate handling (rename, skip, overwrite)
- Comprehensive statistics

### 🌐 Web Scraper
- Ethical scraping with rate limiting
- BeautifulSoup4 integration
- CSS selector support
- Link extraction and text parsing
- Session management

### 📧 Email Automation
- SMTP support (Gmail, custom servers)
- Template-based personalization
- Bulk email sending
- Attachment support
- HTML and plain text emails

### 💾 Backup Manager
- Multiple compression formats (ZIP, TAR, TAR.GZ)
- Version management (keep N backups)
- Incremental backups
- Easy restore functionality

### 📊 Log Analyzer
- Parse common log formats
- Extract errors, warnings, patterns
- IP address and email extraction
- Timestamp analysis
- Statistical summaries

### 📈 Data Processor
- CSV ↔ JSON conversion
- Data filtering and transformation
- Aggregation (sum, avg, min, max)
- Deduplication
- Batch processing

### 🔐 Security Utils
- File encryption/decryption (Fernet)
- Password-based key derivation (PBKDF2)
- Secure password generation
- Hashing utilities (MD5, SHA256, SHA512)
- Token generation

### ⛓️ Blockchain Monitor
- Real-time crypto price monitoring
- Support for EGLD, BTC, ETH, BNB, SOL
- 24h change tracking
- Market cap and volume data
- Trending coins detection
- Price alerts

## 📚 Complete CLI Reference

### Available Commands

After installation via pip, these commands are available:

```bash
pyautokit              # Unified CLI entry point
pyautokit-organizer    # File organization
pyautokit-scraper      # Web scraping
pyautokit-email        # Email automation  
pyautokit-backup       # Backup management
pyautokit-logs         # Log analysis
pyautokit-data         # Data processing
pyautokit-security     # Encryption & security
pyautokit-crypto       # Blockchain monitoring
```

### 📁 File Organizer

```bash
# Organize by category
pyautokit-organizer ~/Downloads --method category

# Test without moving files
pyautokit-organizer ~/Downloads --dry-run

# Show statistics
pyautokit-organizer ~/Downloads --stats

# Auto-watch mode (requires watchdog)
pyautokit-organizer ~/Downloads --watch --interval 30
```

### ⛓️ Blockchain Monitor

```bash
# Check EGLD price
pyautokit-crypto --coin EGLD

# Monitor multiple coins
pyautokit-crypto --coin EGLD --coin BTC --coin ETH

# Continuous monitoring
pyautokit-crypto --coin EGLD --monitor --interval 300

# Show trending
pyautokit-crypto --trending
```

### 🔐 Security Utils

```bash
# Generate password
pyautokit-security genpass --length 20

# Encrypt file
pyautokit-security encrypt file.txt file.enc --password secret

# Hash file
pyautokit-security hash file.txt --file --algorithm sha256

# Generate token
pyautokit-security token --length 32
```

### 📈 Data Processor

```bash
# Convert CSV to JSON
pyautokit-data convert data.csv --to json

# Filter data
pyautokit-data filter data.json --field status=active

# Aggregate
pyautokit-data aggregate data.json --field price --operation avg

# Remove duplicates
pyautokit-data dedupe data.json --key email
```

### 💾 Backup Manager

```bash
# Create backup
pyautokit-backup create ./myproject --compression tar.gz

# List backups
pyautokit-backup list

# Restore
pyautokit-backup restore backup.tar.gz ./restored
```

See complete CLI documentation in [README sections below](#complete-cli-reference) or run any command with `--help`.

## 📖 Programmatic Usage

### File Organization

```python
from pyautokit import FileOrganizer
from pathlib import Path

organizer = FileOrganizer(dry_run=False)
results = organizer.organize_by_category(Path("~/Downloads"))
print(f"Organized into {len(results)} categories")
```

### Blockchain Monitoring

```python
from pyautokit import BlockchainMonitor

monitor = BlockchainMonitor()
price_data = monitor.get_price("EGLD")
print(f"EGLD: ${price_data['price']} ({price_data['change_24h']:.2f}%)")
```

### Email Automation

```python
from pyautokit import EmailClient

client = EmailClient()
recipients = [{"email": "user@test.com", "name": "Alice"}]
results = client.send_templated_emails(
    recipients,
    "Hi \$name",
    "Your project is ready!"
)
```

### Security Utils

```python
from pyautokit import SecurityUtils

utils = SecurityUtils()
password = utils.generate_password(length=20)
print(f"Generated: {password}")
```

### Data Processing

```python
from pyautokit import DataProcessor
from pathlib import Path

processor = DataProcessor()
data = processor.csv_to_json(Path("data.csv"))
avg = processor.aggregate(data, "price", "avg")
```

See more examples in [examples/](examples/) directory.

## 📚 Examples

Complete working examples:

| Example | Command |
|---------|----------|
| **Organize Downloads** | `python examples/organize_downloads.py --watch` |
| **Monitor EGLD** | `python examples/monitor_egld.py` |
| **Scrape News** | `python examples/scrape_news.py` |
| **Bulk Emails** | `python examples/send_bulk_emails.py` |
| **Backup Project** | `python examples/backup_project.py` |
| **Analyze Logs** | `python examples/analyze_logs.py` |

## 🧪 Testing

```bash
# Run tests
pytest

# With coverage
pytest --cov=pyautokit --cov-report=html

# Test specific module
pytest tests/test_file_organizer.py -v
```

**Current Coverage**: file_organizer.py = 95%+

## 📦 Publishing to PyPI

See [PUBLISHING.md](PUBLISHING.md) for complete PyPI publishing guide.

Quick reference:

```bash
# Build
python -m build

# Upload to TestPyPI
twine upload --repository testpypi dist/*

# Upload to PyPI
twine upload dist/*
```

## 📝 Project Structure

```
pyautokit/
├── pyautokit/              # Main package
│   ├── __init__.py         # Package exports
│   ├── __main__.py         # ✅ Unified CLI
│   ├── file_organizer.py   # ✅ CLI + 95% tests
│   ├── web_scraper.py      # ✅ Complete CLI
│   ├── email_automation.py # ✅ Complete CLI
│   ├── backup_manager.py   # ✅ Complete CLI
│   ├── data_processor.py   # ✅ Complete CLI
│   ├── security_utils.py   # ✅ Complete CLI
│   └── blockchain_monitor.py # ✅ Complete CLI
├── examples/               # Working examples
├── tests/                  # Test suite
├── .github/workflows/      # CI/CD pipelines
├── setup.py                # ✅ PyPI setup
├── pyproject.toml          # ✅ Build config
├── PUBLISHING.md           # ✅ PyPI guide
├── INSTALLATION.md         # ✅ Install guide
└── CONTRIBUTING.md         # ✅ Contribution guide
```

## 🤝 Contributing

1. Fork repository
2. Create feature branch
3. Commit changes
4. Push and create PR

See [CONTRIBUTING.md](CONTRIBUTING.md) for details.

## 📝 License

MIT License - Free for personal and commercial use.

## 👤 Author

**George Pricop**
- Blockchain Developer & AI Automation Specialist  
- GitHub: [@Gzeu](https://github.com/Gzeu)
- Building on MultiversX (EGLD) ecosystem
- Location: București, Romania

## 🔗 Links

- **PyPI**: [pypi.org/project/pyautokit](https://pypi.org/project/pyautokit/)
- **GitHub**: [github.com/Gzeu/pyautokit](https://github.com/Gzeu/pyautokit)
- **Issues**: [Report bugs](https://github.com/Gzeu/pyautokit/issues)
- **Examples**: [Working examples](examples/)
- **Installation**: [INSTALLATION.md](INSTALLATION.md)
- **Publishing**: [PUBLISHING.md](PUBLISHING.md)

---

**Built with ❤️ for automation enthusiasts. Install with `pip install pyautokit`! 🚀**
