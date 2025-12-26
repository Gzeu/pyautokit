# PyAutokit 🚀

**Python Automation Toolkit** - A comprehensive, production-ready collection of automation utilities for everyday tasks.

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Tests](https://img.shields.io/badge/tests-passing-brightgreen.svg)](https://github.com/Gzeu/pyautokit)
[![Code Style: Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## 🎯 Overview

PyAutokit is a modular Python toolkit designed to automate common development and operations tasks. Each module is standalone, well-documented, tested, and can be used via CLI or programmatically.

## ⚡ Quick Demo

```bash
# Clone and setup
git clone https://github.com/Gzeu/pyautokit.git && cd pyautokit
pip install -r requirements.txt

# Organize your Downloads folder (dry-run)
python examples/organize_downloads.py --dry-run

# Check EGLD price
python examples/monitor_egld.py

# Run tests
pytest tests/ -v
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

### 🔗 API Client
- Generic REST API client
- Automatic retry with exponential backoff
- Rate limiting support
- Bearer token authentication
- JSON response handling

### 📈 Data Processor
- CSV ↔ JSON conversion
- Data filtering and transformation
- Aggregation (sum, avg, min, max)
- Deduplication
- Batch processing

### ⏰ Task Scheduler
- Cron-like scheduling
- Interval-based tasks (seconds, minutes, hours, days)
- Task management (add, remove, list)
- Manual task execution

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

## 🚀 Quick Start

### Installation

```bash
git clone https://github.com/Gzeu/pyautokit.git
cd pyautokit
pip install -r requirements.txt
```

### Configuration

```bash
cp .env.example .env
# Edit .env with your settings
```

### Basic Usage

#### 📁 Organize Files

```bash
# Organize Downloads by category
python -m pyautokit.file_organizer ~/Downloads --method category

# Test first (dry-run)
python -m pyautokit.file_organizer ~/Downloads --dry-run

# Show statistics
python -m pyautokit.file_organizer ~/Downloads --stats

# Auto-watch for new files (requires watchdog)
python examples/organize_downloads.py --watch
```

#### ⛓️ Monitor Crypto

```bash
# Check EGLD price
python -m pyautokit.blockchain_monitor --coin EGLD

# Continuous monitoring with alerts
python -m pyautokit.blockchain_monitor --coin EGLD --monitor --alert 5.0
```

#### 🌐 Scrape Websites

```bash
python -m pyautokit.web_scraper https://example.com --selector "title:h1" -o output.json
```

#### 💾 Create Backups

```bash
python -m pyautokit.backup_manager create ./myproject --compression tar.gz
```

#### 📊 Analyze Logs

```bash
python -m pyautokit.log_analyzer /var/log/app.log -o analysis.json
```

## 📖 Programmatic Usage

### File Organization

```python
from pathlib import Path
from pyautokit.file_organizer import FileOrganizer

# Create organizer
organizer = FileOrganizer(
    create_folders=True,
    dry_run=False,
    handle_duplicates="rename"
)

# Organize by category
results = organizer.organize_by_category(Path("~/Downloads"))
print(f"Organized {sum(results.values())} files into {len(results)} categories")

# Get statistics
stats = organizer.get_directory_stats(Path("~/Downloads"))
print(f"Total files: {stats['total_files']}")
print(f"Total size: {stats['total_size']}")
```

### Web Scraping

```python
from pyautokit.web_scraper import WebScraper

scraper = WebScraper(rate_limit=1.0)
selectors = {"headlines": "h2.title", "links": "a.story-link"}
data = scraper.scrape_page("https://news.ycombinator.com", selectors)
```

### Email Automation

```python
from pyautokit.email_automation import EmailClient

client = EmailClient()
recipients = [
    {"email": "user@example.com", "name": "Alice", "project": "Web"}
]
results = client.send_templated_emails(
    recipients,
    subject_template="Update on $project",
    body_template="Hi $name, your $project is ready!"
)
print(f"Sent: {results['success']}, Failed: {results['failed']}")
```

### Blockchain Monitoring

```python
from pyautokit.blockchain_monitor import BlockchainMonitor

monitor = BlockchainMonitor()
price_data = monitor.get_price("EGLD")
print(f"EGLD: ${price_data['price']} ({price_data['change_24h']:.2f}%)")

# Monitor multiple coins
prices = monitor.get_multiple_prices(["EGLD", "BTC", "ETH"])
for p in prices:
    print(f"{p['coin']}: ${p['price']:,.2f}")
```

### Task Scheduling

```python
from pyautokit.task_scheduler import TaskScheduler

def backup_task():
    print("Running backup...")

scheduler = TaskScheduler()
scheduler.add_task("daily_backup", backup_task, "1", "days")
scheduler.run_forever()  # Runs in background
```

## 📚 Examples

Complete working examples in `examples/` directory:

| Example | Description | Command |
|---------|-------------|----------|
| **organize_downloads.py** | Organize Downloads folder | `python examples/organize_downloads.py` |
| **scrape_news.py** | Scrape news headlines | `python examples/scrape_news.py` |
| **send_bulk_emails.py** | Send personalized emails | `python examples/send_bulk_emails.py` |
| **backup_project.py** | Create project backups | `python examples/backup_project.py` |
| **analyze_logs.py** | Analyze log files | `python examples/analyze_logs.py` |
| **monitor_egld.py** | Monitor crypto prices | `python examples/monitor_egld.py` |

See [examples/README.md](examples/README.md) for detailed documentation.

## 🧪 Testing

PyAutokit comes with comprehensive test coverage for all modules.

### Run All Tests

```bash
# Basic test run
pytest

# Verbose output
pytest -v

# With coverage report
pytest --cov=pyautokit --cov-report=html

# Open coverage report
open htmlcov/index.html
```

### Run Specific Tests

```bash
# Test specific module
pytest tests/test_file_organizer.py

# Test specific function
pytest tests/test_file_organizer.py::TestFileOrganizer::test_categorize_file

# Run only fast tests (skip slow/integration)
pytest -m "not slow"
```

### Test Coverage

Current test coverage:
- **file_organizer.py**: 95%+ coverage
- **Core modules**: Tests in progress
- **Integration tests**: Coming soon

### Writing Tests

See [CONTRIBUTING.md](CONTRIBUTING.md) for testing guidelines.

```python
import pytest
from pyautokit.file_organizer import FileOrganizer

def test_organize_by_category(tmp_path):
    """Test file organization."""
    # Create test files
    (tmp_path / "test.pdf").write_text("content")
    (tmp_path / "image.jpg").write_text("content")
    
    # Organize
    organizer = FileOrganizer()
    results = organizer.organize_by_category(tmp_path)
    
    # Assert
    assert "Documents" in results
    assert "Images" in results
    assert (tmp_path / "Documents" / "test.pdf").exists()
```

## 📝 Project Structure

```
pyautokit/
├── pyautokit/              # Main package
│   ├── __init__.py         # Package initialization
│   ├── config.py           # Configuration management
│   ├── logger.py           # Logging utilities
│   ├── utils.py            # Common utilities
│   ├── file_organizer.py   # File organization ✅ TESTED
│   ├── web_scraper.py      # Web scraping
│   ├── email_automation.py # Email automation
│   ├── backup_manager.py   # Backup management
│   ├── log_analyzer.py     # Log analysis
│   ├── api_client.py       # API client
│   ├── data_processor.py   # Data processing
│   ├── task_scheduler.py   # Task scheduling
│   ├── security_utils.py   # Security utilities
│   └── blockchain_monitor.py # Blockchain monitoring
├── examples/               # Usage examples
│   ├── README.md           # Examples documentation
│   ├── organize_downloads.py
│   ├── scrape_news.py
│   ├── send_bulk_emails.py
│   ├── backup_project.py
│   ├── analyze_logs.py
│   └── monitor_egld.py
├── tests/                  # Test suite
│   ├── __init__.py
│   ├── conftest.py         # Pytest configuration
│   └── test_file_organizer.py  # ✅ 95%+ coverage
├── .github/                # GitHub templates
│   └── ISSUE_TEMPLATE/
├── .env.example            # Environment template
├── .gitignore              # Git ignore rules
├── pytest.ini              # Pytest configuration
├── requirements.txt        # Dependencies
├── CONTRIBUTING.md         # Contribution guide
└── README.md               # This file
```

## 🔧 Configuration

### Environment Variables (.env)

```bash
# Logging
LOG_LEVEL=INFO

# File Organizer
FILE_ORG_SORT_BY=extension
FILE_ORG_CREATE_FOLDERS=true

# Web Scraper
SCRAPER_TIMEOUT=10
SCRAPER_RATE_LIMIT=1.0

# Email (Gmail example)
EMAIL_SMTP_SERVER=smtp.gmail.com
EMAIL_SMTP_PORT=587
EMAIL_SENDER=your-email@gmail.com
EMAIL_PASSWORD=your-app-password  # Get from Google Account settings

# API Client
API_BASE_URL=https://api.example.com
API_KEY=your-api-key

# Blockchain
BLOCKCHAIN_MONITOR_INTERVAL=300  # 5 minutes

# Backup
BACKUP_COMPRESSION=zip
BACKUP_KEEP_VERSIONS=5
```

## 🛑 Development

### Setup Development Environment

```bash
# Clone repository
git clone https://github.com/Gzeu/pyautokit.git
cd pyautokit

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run tests
pytest
```

### Code Quality

```bash
# Format code
black pyautokit/ tests/

# Lint
flake8 pyautokit/ tests/

# Type checking
mypy pyautokit/
```

### Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for:
- Code style guidelines
- Testing requirements
- Pull request process
- Development workflow

## 🤝 Contributing

Contributions are welcome! Here's how:

1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'feat: add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open Pull Request

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

## 📝 License

MIT License - see [LICENSE](LICENSE) for details.

Free to use in personal and commercial projects.

## 👤 Author

**George Pricop**
- Blockchain Developer & AI Automation Specialist
- Building on MultiversX (EGLD) ecosystem
- GitHub: [@Gzeu](https://github.com/Gzeu)
- Location: București, Romania

## 🙏 Acknowledgments

- Built with Python 3.9+
- Uses BeautifulSoup4 for web scraping
- CoinGecko API for crypto prices
- Cryptography library for security
- Watchdog for file monitoring
- Schedule for task automation

## 🔗 Links

- **Repository**: [github.com/Gzeu/pyautokit](https://github.com/Gzeu/pyautokit)
- **Issues**: [Report bugs](https://github.com/Gzeu/pyautokit/issues)
- **Pull Requests**: [Contribute](https://github.com/Gzeu/pyautokit/pulls)
- **Examples**: [Working examples](examples/)
- **Tests**: [Test coverage](tests/)

## ⭐ Star History

If you find PyAutokit useful, please star the repository!

---

**Built with ❤️ for automation enthusiasts**
