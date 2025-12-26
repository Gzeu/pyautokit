# PyAutokit 🚀

**Python Automation Toolkit** - A comprehensive, production-ready collection of automation utilities for everyday tasks.

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Tests](https://img.shields.io/badge/tests-passing-brightgreen.svg)](https://github.com/Gzeu/pyautokit)
[![Code Style: Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## 🎯 Overview

PyAutokit is a modular Python toolkit designed to automate common development and operations tasks. **Each module has a complete CLI** with argparse and can be used programmatically. All modules are standalone, well-documented, and tested.

## ⚡ Quick Demo

```bash
# Clone and setup
git clone https://github.com/Gzeu/pyautokit.git && cd pyautokit
pip install -r requirements.txt

# Organize Downloads (dry-run)
python -m pyautokit.file_organizer ~/Downloads --dry-run

# Check EGLD price
python -m pyautokit.blockchain_monitor --coin EGLD

# Generate secure password
python -m pyautokit.security_utils genpass --length 20

# Run tests
pytest tests/ -v
```

## 📚 Complete CLI Reference

### 📁 File Organizer

```bash
# Organize by category (Documents, Images, Videos, etc.)
python -m pyautokit.file_organizer ~/Downloads --method category

# Organize by file extension
python -m pyautokit.file_organizer ~/Downloads --method extension

# Organize by date (YYYY-MM-DD folders)
python -m pyautokit.file_organizer ~/Downloads --method date

# Organize by file size
python -m pyautokit.file_organizer ~/Downloads --method size

# Test without moving files (dry-run)
python -m pyautokit.file_organizer ~/Downloads --dry-run

# Show directory statistics only
python -m pyautokit.file_organizer ~/Downloads --stats

# Recursive organization
python -m pyautokit.file_organizer ~/Downloads --recursive

# Handle duplicates (rename/skip/overwrite)
python -m pyautokit.file_organizer ~/Downloads --duplicates rename

# Auto-watch mode (continuous organization)
python examples/organize_downloads.py --watch --interval 30
```

### 🌐 Web Scraper

```bash
# Scrape page with CSS selectors
python -m pyautokit.web_scraper https://news.ycombinator.com \
  --selector "title:a.storylink" \
  --output news.json

# Extract all links from page
python -m pyautokit.web_scraper https://example.com \
  --links \
  --output links.json

# Include external links
python -m pyautokit.web_scraper https://example.com \
  --links --external

# Custom rate limiting and timeout
python -m pyautokit.web_scraper https://example.com \
  --rate-limit 2.0 \
  --timeout 30

# Multiple selectors
python -m pyautokit.web_scraper https://example.com \
  -s "headlines:h2.title" \
  -s "authors:.author-name" \
  -o data.json
```

### 📧 Email Automation

```bash
# Send single email
python -m pyautokit.email_automation \
  --to user@example.com \
  --subject "Hello" \
  --body "Test message"

# Send with attachment
python -m pyautokit.email_automation \
  --to user@example.com \
  --subject "Report" \
  --body-file report.txt \
  --attach document.pdf

# Send bulk emails from CSV
python -m pyautokit.email_automation \
  --bulk recipients.csv \
  --subject "Update" \
  --template email_template.txt

# Send templated emails with personalization
python -m pyautokit.email_automation \
  --templated recipients.json \
  --subject-template "Hi \$name" \
  --template email_body.txt

# Send HTML email
python -m pyautokit.email_automation \
  --to user@example.com \
  --subject "Newsletter" \
  --body-file newsletter.html \
  --html

# Dry-run (test without sending)
python -m pyautokit.email_automation \
  --to user@example.com \
  --subject "Test" \
  --body "Hello" \
  --dry-run
```

### 💾 Backup Manager

```bash
# Create backup (ZIP format)
python -m pyautokit.backup_manager create ./myproject

# Create backup with TAR.GZ compression
python -m pyautokit.backup_manager create ./myproject \
  --compression tar.gz

# Custom backup name
python -m pyautokit.backup_manager create ./myproject \
  --name project_backup_v1.zip

# Keep only 3 versions
python -m pyautokit.backup_manager create ./myproject \
  --keep 3

# List all backups
python -m pyautokit.backup_manager list

# List backups filtered by name
python -m pyautokit.backup_manager list --filter myproject

# Restore backup
python -m pyautokit.backup_manager restore \
  backups/myproject_20250101_120000.zip \
  ./restored

# Restore with overwrite
python -m pyautokit.backup_manager restore \
  backups/myproject.zip \
  ./restored \
  --overwrite

# Delete backup
python -m pyautokit.backup_manager delete backups/old_backup.zip
```

### 📊 Log Analyzer

```bash
# Analyze log file
python -m pyautokit.log_analyzer /var/log/app.log

# Save analysis to JSON
python -m pyautokit.log_analyzer /var/log/app.log \
  --output analysis.json

# Extract only errors
python -m pyautokit.log_analyzer /var/log/app.log \
  --level ERROR

# Extract IP addresses
python -m pyautokit.log_analyzer /var/log/access.log \
  --extract-ips

# Custom pattern search
python -m pyautokit.log_analyzer /var/log/app.log \
  --pattern "database error"

# Time range filter
python -m pyautokit.log_analyzer /var/log/app.log \
  --start "2025-01-01 00:00:00" \
  --end "2025-01-31 23:59:59"
```

### 📈 Data Processor

```bash
# Convert CSV to JSON
python -m pyautokit.data_processor convert data.csv --to json

# Convert JSON to CSV
python -m pyautokit.data_processor convert data.json --to csv

# Convert with custom output
python -m pyautokit.data_processor convert data.csv \
  --to json \
  --output result.json

# Filter data
python -m pyautokit.data_processor filter data.json \
  --field status=active \
  --field role=admin \
  --output filtered.json

# Aggregate data
python -m pyautokit.data_processor aggregate data.json \
  --field price \
  --operation avg

# Sum aggregation
python -m pyautokit.data_processor aggregate sales.json \
  --field total \
  --operation sum

# Remove duplicates
python -m pyautokit.data_processor dedupe data.json \
  --key email \
  --output unique.json

# Count records
python -m pyautokit.data_processor aggregate data.json \
  --field id \
  --operation count
```

### 🔐 Security Utils

```bash
# Generate encryption key
python -m pyautokit.security_utils genkey

# Encrypt file with password
python -m pyautokit.security_utils encrypt \
  file.txt \
  file.enc \
  --password mysecretpass

# Decrypt file
python -m pyautokit.security_utils decrypt \
  file.enc \
  file.txt \
  --password mysecretpass

# Encrypt with key
python -m pyautokit.security_utils encrypt \
  file.txt \
  file.enc \
  --key "gAAAAABh..."

# Hash file (SHA256)
python -m pyautokit.security_utils hash file.txt \
  --file \
  --algorithm sha256

# Hash text
python -m pyautokit.security_utils hash "Hello World" \
  --algorithm sha512

# Generate secure password
python -m pyautokit.security_utils genpass --length 20

# Generate password (no special chars)
python -m pyautokit.security_utils genpass \
  --length 16 \
  --no-special

# Generate random token
python -m pyautokit.security_utils token --length 32
```

### ⛓️ Blockchain Monitor

```bash
# Check EGLD price
python -m pyautokit.blockchain_monitor --coin EGLD

# Check multiple coins
python -m pyautokit.blockchain_monitor \
  --coin EGLD \
  --coin BTC \
  --coin ETH

# Monitor continuously (every 5 minutes)
python -m pyautokit.blockchain_monitor \
  --coin EGLD \
  --monitor \
  --interval 300

# Set price alert (notify when change > 5%)
python -m pyautokit.blockchain_monitor \
  --coin EGLD \
  --monitor \
  --alert 5.0

# Show trending coins
python -m pyautokit.blockchain_monitor --trending

# Save to JSON
python -m pyautokit.blockchain_monitor \
  --coin EGLD \
  --output prices.json
```

### 🕹️ Unified CLI

```bash
# Use unified pyautokit command
python -m pyautokit file-organizer ~/Downloads --method category
python -m pyautokit crypto --coin EGLD
python -m pyautokit backup create ./project
python -m pyautokit security genpass --length 20

# Get help for any module
python -m pyautokit.file_organizer --help
python -m pyautokit.web_scraper --help
python -m pyautokit.email_automation --help
```

## 📖 Programmatic Usage

### File Organization

```python
from pathlib import Path
from pyautokit.file_organizer import FileOrganizer

organizer = FileOrganizer(
    create_folders=True,
    dry_run=False,
    handle_duplicates="rename"
)

# Organize by category
results = organizer.organize_by_category(Path("~/Downloads"))
print(f"Organized into {len(results)} categories")

# Get statistics
stats = organizer.get_directory_stats(Path("~/Downloads"))
print(f"Total: {stats['total_files']} files, {stats['total_size']} bytes")
```

### Web Scraping

```python
from pyautokit.web_scraper import WebScraper

scraper = WebScraper(rate_limit=1.0)
selectors = {"headlines": "h2.title", "links": "a.story"}
data = scraper.scrape_page("https://news.ycombinator.com", selectors)
```

### Email Automation

```python
from pyautokit.email_automation import EmailClient

client = EmailClient()
recipients = [
    {"email": "alice@example.com", "name": "Alice", "project": "Web"},
    {"email": "bob@example.com", "name": "Bob", "project": "API"}
]

results = client.send_templated_emails(
    recipients,
    subject_template="Update on \$project",
    body_template="Hi \$name, your \$project is ready!"
)
print(f"✅ {results['success']}, ❌ {results['failed']}")
```

### Backup Management

```python
from pathlib import Path
from pyautokit.backup_manager import BackupManager

manager = BackupManager(compression="tar.gz", keep_versions=5)
backup_path = manager.create_backup(Path("./myproject"))
print(f"Backup created: {backup_path}")

# Restore
manager.restore_backup(backup_path, Path("./restored"))
```

### Data Processing

```python
from pathlib import Path
from pyautokit.data_processor import DataProcessor

processor = DataProcessor()

# Convert
data = processor.csv_to_json(Path("data.csv"))

# Filter
filtered = processor.filter_data(data, {"status": "active"})

# Aggregate
avg_price = processor.aggregate(data, "price", "avg")
print(f"Average price: ${avg_price:.2f}")
```

### Security Utils

```python
from pathlib import Path
from pyautokit.security_utils import SecurityUtils

utils = SecurityUtils()

# Generate password
password = utils.generate_password(length=20, use_special=True)
print(f"Generated: {password}")

# Encrypt file
key, salt = utils.derive_key("mysecretpassword")
utils.encrypt_file(Path("file.txt"), Path("file.enc"), key)

# Hash
file_hash = utils.hash_file(Path("file.txt"), "sha256")
print(f"SHA256: {file_hash}")
```

### Blockchain Monitor

```python
from pyautokit.blockchain_monitor import BlockchainMonitor

monitor = BlockchainMonitor()

# Single coin
price_data = monitor.get_price("EGLD")
print(f"EGLD: ${price_data['price']} ({price_data['change_24h']:.2f}%)")

# Multiple coins
prices = monitor.get_multiple_prices(["EGLD", "BTC", "ETH", "BNB"])
for p in prices:
    print(f"{p['coin']:5} ${p['price']:>10,.2f} {p['change_24h']:+.2f}%")

# Trending
trending = monitor.get_trending_coins()
for coin in trending[:5]:
    print(f"{coin['rank']}. {coin['name']} - {coin['symbol']}")
```

## 📚 Examples

Complete working examples in `examples/` directory:

| Example | Description | Command |
|---------|-------------|----------|
| **organize_downloads.py** | Organize Downloads with auto-watch | `python examples/organize_downloads.py --watch` |
| **scrape_news.py** | Scrape Hacker News headlines | `python examples/scrape_news.py` |
| **send_bulk_emails.py** | Send personalized bulk emails | `python examples/send_bulk_emails.py` |
| **backup_project.py** | Create versioned project backups | `python examples/backup_project.py` |
| **analyze_logs.py** | Analyze log files for patterns | `python examples/analyze_logs.py` |
| **monitor_egld.py** | Monitor EGLD and crypto prices | `python examples/monitor_egld.py` |

See [examples/README.md](examples/README.md) for detailed documentation.

## 🧪 Testing

```bash
# Run all tests
pytest

# Verbose output
pytest -v

# With coverage
pytest --cov=pyautokit --cov-report=html

# Test specific module
pytest tests/test_file_organizer.py

# Open coverage report
open htmlcov/index.html
```

**Current Coverage**: file_organizer.py = 95%+

See [CONTRIBUTING.md](CONTRIBUTING.md) for testing guidelines.

## 📝 Project Structure

```
pyautokit/
├── pyautokit/              # Main package
│   ├── __init__.py         # Package init
│   ├── __main__.py         # ✅ Unified CLI entry point
│   ├── config.py           # Configuration
│   ├── logger.py           # Logging
│   ├── utils.py            # Common utilities
│   ├── file_organizer.py   # ✅ CLI + 95% test coverage
│   ├── web_scraper.py      # ✅ Complete CLI
│   ├── email_automation.py # ✅ Complete CLI
│   ├── backup_manager.py   # ✅ Complete CLI
│   ├── log_analyzer.py     # ✅ Complete CLI
│   ├── api_client.py       # ✅ Complete CLI
│   ├── data_processor.py   # ✅ Complete CLI
│   ├── task_scheduler.py   # ✅ Complete CLI
│   ├── security_utils.py   # ✅ Complete CLI
│   └── blockchain_monitor.py # ✅ Complete CLI
├── examples/               # Working examples
├── tests/                  # Test suite
├── .github/                # GitHub templates
├── CONTRIBUTING.md         # ✅ Complete guide
├── requirements.txt        # ✅ All dependencies
└── README.md               # ✅ Complete CLI reference
```

## 🔧 Configuration (.env)

```bash
# Logging
LOG_LEVEL=INFO

# Email (Gmail example)
EMAIL_SMTP_SERVER=smtp.gmail.com
EMAIL_SMTP_PORT=587
EMAIL_SENDER=your-email@gmail.com
EMAIL_PASSWORD=your-app-password

# Blockchain
BLOCKCHAIN_MONITOR_INTERVAL=300

# Backup
BACKUP_COMPRESSION=zip
BACKUP_KEEP_VERSIONS=5

# Web Scraper
SCRAPER_RATE_LIMIT=1.0
SCRAPER_TIMEOUT=10
```

## 🤝 Contributing

1. Fork repository
2. Create feature branch (`git checkout -b feature/amazing`)
3. Commit changes (`git commit -m 'feat: add amazing feature'`)
4. Push branch (`git push origin feature/amazing`)
5. Open Pull Request

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

## 📝 License

MIT License - Free to use in personal and commercial projects.

## 👤 Author

**George Pricop**
- Blockchain Developer & AI Automation Specialist
- GitHub: [@Gzeu](https://github.com/Gzeu)
- Building on MultiversX (EGLD) ecosystem
- Location: București, Romania

## 🔗 Links

- **Repository**: [github.com/Gzeu/pyautokit](https://github.com/Gzeu/pyautokit)
- **Issues**: [Report bugs](https://github.com/Gzeu/pyautokit/issues)
- **Examples**: [Working examples](examples/)
- **Tests**: [Test coverage](tests/)

---

**Built with ❤️ for automation enthusiasts. Every module has a complete CLI! 🚀**
