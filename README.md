# PyAutokit 🚀

**Python Automation Toolkit** - A comprehensive, production-ready collection of automation utilities for everyday tasks.

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 🎯 Overview

PyAutokit is a modular Python toolkit designed to automate common development and operations tasks. Each module is standalone, well-documented, and can be used via CLI or programmatically.

## ✨ Features

### 📁 File Organizer
- Organize files by extension, date, or category
- Smart categorization (Documents, Images, Videos, Code, etc.)
- Recursive directory scanning
- Dry-run mode for safe testing

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

#### Organize Downloads Folder

```bash
python -m pyautokit.file_organizer ~/Downloads --method category
```

#### Monitor EGLD Price

```bash
python -m pyautokit.blockchain_monitor --coin EGLD --monitor --interval 60
```

#### Scrape Website

```bash
python -m pyautokit.web_scraper https://example.com --selector "title:h1" -o output.json
```

#### Create Backup

```bash
python -m pyautokit.backup_manager create ./myproject --compression tar.gz
```

#### Analyze Logs

```bash
python -m pyautokit.log_analyzer /var/log/app.log -o analysis.json
```

## 📖 Programmatic Usage

### File Organization

```python
from pathlib import Path
from pyautokit.file_organizer import FileOrganizer

organizer = FileOrganizer(create_folders=True)
results = organizer.organize_by_category(Path("~/Downloads"))
print(f"Organized {sum(results.values())} files")
```

### Web Scraping

```python
from pyautokit.web_scraper import WebScraper

scraper = WebScraper(rate_limit=1.0)
selectors = {"headlines": "h2.title"}
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
    "Update on $project",
    "Hi $name, your $project is ready!"
)
```

### Blockchain Monitoring

```python
from pyautokit.blockchain_monitor import BlockchainMonitor

monitor = BlockchainMonitor()
price_data = monitor.get_price("EGLD")
print(f"EGLD: ${price_data['price']} ({price_data['change_24h']:.2f}%)")
```

### Task Scheduling

```python
from pyautokit.task_scheduler import TaskScheduler

def my_task():
    print("Task executed!")

scheduler = TaskScheduler()
scheduler.add_task("daily_backup", my_task, "1", "days")
scheduler.run_forever()
```

## 📂 Project Structure

```
pyautokit/
├── pyautokit/              # Main package
│   ├── __init__.py         # Package initialization
│   ├── config.py           # Configuration management
│   ├── logger.py           # Logging utilities
│   ├── utils.py            # Common utilities
│   ├── file_organizer.py   # File organization
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
│   ├── organize_downloads.py
│   ├── scrape_news.py
│   ├── send_bulk_emails.py
│   ├── backup_project.py
│   ├── analyze_logs.py
│   └── monitor_egld.py
├── .env.example            # Environment template
├── .gitignore              # Git ignore rules
├── requirements.txt        # Dependencies
└── README.md               # This file
```

## 🔧 Configuration Options

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

# Email
EMAIL_SMTP_SERVER=smtp.gmail.com
EMAIL_SMTP_PORT=587
EMAIL_SENDER=your-email@gmail.com
EMAIL_PASSWORD=your-app-password

# API Client
API_BASE_URL=https://api.example.com
API_KEY=your-api-key

# Blockchain
BLOCKCHAIN_MONITOR_INTERVAL=300

# Backup
BACKUP_COMPRESSION=zip
BACKUP_KEEP_VERSIONS=5
```

## 📚 Examples

Check the `examples/` directory for complete working examples:

- **organize_downloads.py** - Organize Downloads folder by file type
- **scrape_news.py** - Scrape news headlines with BeautifulSoup
- **send_bulk_emails.py** - Send personalized bulk emails
- **backup_project.py** - Create versioned project backups
- **analyze_logs.py** - Analyze log files for errors and patterns
- **monitor_egld.py** - Monitor cryptocurrency prices

Run any example:

```bash
python examples/organize_downloads.py
python examples/monitor_egld.py
```

## 🛠️ Development

### Running Tests

```bash
pytest tests/
pytest --cov=pyautokit tests/
```

### Code Formatting

```bash
black pyautokit/
flake8 pyautokit/
mypy pyautokit/
```

## 🤝 Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

MIT License - see [LICENSE](LICENSE) for details.

## 👤 Author

**George Pricop**
- Blockchain Developer & AI Automation Specialist
- GitHub: [@Gzeu](https://github.com/Gzeu)
- Location: București, Romania

## 🙏 Acknowledgments

- Built with Python 3.9+
- Uses BeautifulSoup4 for web scraping
- CoinGecko API for crypto prices
- Cryptography library for security features

## 🔗 Links

- [Repository](https://github.com/Gzeu/pyautokit)
- [Issues](https://github.com/Gzeu/pyautokit/issues)
- [Pull Requests](https://github.com/Gzeu/pyautokit/pulls)

---

**Built with ❤️ for automation enthusiasts**
