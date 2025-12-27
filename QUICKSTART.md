# PyAutokit Quick Start Guide 🚀

Get started with PyAutokit in 5 minutes!

## 📦 Installation

### 1. Basic Installation

```bash
pip install pyautokit
```

That's it! You now have access to 11 automation modules.

### 2. Optional Dependencies

```bash
# For browser automation (Playwright)
pip install 'pyautokit[browser]'
playwright install  # Download browser binaries

# For file watching (auto-organize)
pip install 'pyautokit[watch]'

# Install everything
pip install 'pyautokit[all]'
```

### 3. Verify Installation

```bash
pyautokit --version
# Should show: PyAutokit 1.0.0

# List all available commands
pyautokit --help
```

---

## ⚡ First Commands to Try

### 1. Generate a Secure Password

```bash
pyautokit-security genpass --length 20
# Output: X7k9#mP2@qR5$nL8&wY4
```

### 2. Check Crypto Prices

```bash
pyautokit-crypto --coin EGLD
# Output:
# EGLD Price: $45.23
# 24h Change: +2.5%
# Market Cap: $1.2B
```

### 3. Organize Your Downloads (Dry-Run)

```bash
pyautokit-organizer ~/Downloads --method category --dry-run
# Shows what would be organized without moving files
```

### 4. Convert CSV to JSON

```bash
pyautokit-data convert data.csv --to json --output data.json
```

### 5. Create a Backup

```bash
pyautokit-backup create ./my-project --compression tar.gz
# Creates timestamped backup
```

---

## 🎯 Common Use Cases

### Use Case 1: Clean Up Downloads Folder

**Problem**: Downloads folder is a mess with 500+ files  
**Solution**: Organize by category

```bash
# 1. See what would happen (safe)
pyautokit-organizer ~/Downloads --method category --dry-run

# 2. Review statistics
pyautokit-organizer ~/Downloads --stats

# 3. Actually organize
pyautokit-organizer ~/Downloads --method category

# 4. Set up auto-organization (requires watchdog)
pip install 'pyautokit[watch]'
pyautokit-organizer ~/Downloads --watch --interval 30
```

**Result**: Files organized into Documents/, Images/, Videos/, Code/, Archives/, etc.

---

### Use Case 2: Monitor Crypto Portfolio

**Problem**: Need to track multiple crypto prices  
**Solution**: Real-time monitoring

```bash
# Check multiple coins
pyautokit-crypto --coin EGLD --coin BTC --coin ETH

# Continuous monitoring (every 5 minutes)
pyautokit-crypto --coin EGLD --monitor --interval 300

# Save to JSON
pyautokit-crypto --coin EGLD --output prices.json

# Show trending coins
pyautokit-crypto --trending
```

---

### Use Case 3: Automated Backups

**Problem**: Need regular project backups  
**Solution**: Automated backup system

```bash
# Create backup
pyautokit-backup create ./my-project --compression tar.gz

# Keep only last 5 versions
pyautokit-backup create ./my-project --keep 5

# List all backups
pyautokit-backup list

# Restore backup
pyautokit-backup restore backups/my-project_20250127_120000.tar.gz ./restored
```

**Pro Tip**: Add to cron for automatic backups:

```bash
# Backup every day at 2 AM
0 2 * * * pyautokit-backup create ~/projects --keep 7
```

---

### Use Case 4: Data Processing Pipeline

**Problem**: Need to convert and process CSV data  
**Solution**: Data processing tools

```bash
# 1. Convert CSV to JSON
pyautokit-data convert sales.csv --to json --output sales.json

# 2. Filter active records
pyautokit-data filter sales.json --field status=active --output active.json

# 3. Calculate average
pyautokit-data aggregate active.json --field price --operation avg

# 4. Remove duplicates
pyautokit-data dedupe active.json --key email --output unique.json
```

---

### Use Case 5: Secure File Encryption

**Problem**: Need to encrypt sensitive files  
**Solution**: Security utilities

```bash
# 1. Generate encryption key
pyautokit-security genkey
# Save this key securely!

# 2. Encrypt file
pyautokit-security encrypt secrets.txt secrets.enc --password mypassword

# 3. Decrypt file
pyautokit-security decrypt secrets.enc secrets.txt --password mypassword

# 4. Hash file for verification
pyautokit-security hash important.pdf --file --algorithm sha256
```

---

### Use Case 6: GitHub Automation

**Problem**: Need to manage multiple GitHub repos  
**Solution**: GitHub utilities

```bash
# Set your GitHub token
export GITHUB_TOKEN="your-token-here"

# List your repositories
pyautokit-github list-repos --user YourUsername

# Create new repository
pyautokit-github create-repo my-new-project --private --description "My project"

# List issues
pyautokit-github list-issues --owner Gzeu --repo pyautokit --state open

# Create issue
pyautokit-github create-issue --owner Gzeu --repo pyautokit \
  --title "Feature request" \
  --body "Add awesome feature"
```

---

### Use Case 7: Browser Automation & Testing

**Problem**: Need to capture screenshots or test web pages  
**Solution**: Playwright browser automation

```bash
# Install browser support
pip install 'pyautokit[browser]'
playwright install

# Capture screenshot
pyautokit-browser screenshot https://example.com -o page.png --full-page

# Generate PDF
pyautokit-browser pdf https://docs.python.org -o docs.pdf --format A4

# Scrape dynamic content
pyautokit-browser scrape https://news.ycombinator.com \
  -s "titles:.titleline > a" \
  -o news.json

# Test on different browsers
pyautokit-browser --browser firefox screenshot https://example.com -o ff.png
pyautokit-browser --browser webkit screenshot https://example.com -o safari.png
```

---

## 📖 Module Overview

### Quick Reference Table

| Need to... | Use | Command |
|------------|-----|----------|
| Organize files | File Organizer | `pyautokit-organizer` |
| Scrape websites | Web Scraper | `pyautokit-scraper` |
| Send emails | Email Automation | `pyautokit-email` |
| Create backups | Backup Manager | `pyautokit-backup` |
| Analyze logs | Log Analyzer | `pyautokit-logs` |
| Process data | Data Processor | `pyautokit-data` |
| Encrypt files | Security Utils | `pyautokit-security` |
| Track crypto | Blockchain Monitor | `pyautokit-crypto` |
| Manage GitHub | GitHub Utils | `pyautokit-github` |
| Automate browser | Playwright | `pyautokit-browser` |

---

## 🐍 Programmatic Usage

### Example 1: File Organization Script

```python
from pyautokit import FileOrganizer
from pathlib import Path

# Create organizer
organizer = FileOrganizer(
    create_folders=True,
    dry_run=False,
    handle_duplicates="rename"
)

# Organize by category
results = organizer.organize_by_category(Path("~/Downloads"))

print(f"Organized {sum(len(files) for files in results.values())} files")
print(f"Categories: {', '.join(results.keys())}")
```

### Example 2: Crypto Price Alert

```python
from pyautokit import BlockchainMonitor
import time

monitor = BlockchainMonitor()

while True:
    price_data = monitor.get_price("EGLD")
    price = price_data['price']
    change = price_data['change_24h']
    
    print(f"EGLD: ${price:.2f} ({change:+.2f}%)")
    
    if price > 50.0:
        print("⚠️ ALERT: EGLD above $50!")
        # Send notification, email, etc.
    
    time.sleep(300)  # Check every 5 minutes
```

### Example 3: Automated Backup Script

```python
from pyautokit import BackupManager
from pathlib import Path
import schedule

def backup_project():
    manager = BackupManager(
        compression="tar.gz",
        keep_versions=7
    )
    
    backup_path = manager.create_backup(Path("~/projects/myapp"))
    print(f"✅ Backup created: {backup_path}")

# Run daily at 2 AM
schedule.every().day.at("02:00").do(backup_project)

while True:
    schedule.run_pending()
    time.sleep(60)
```

### Example 4: GitHub Issue Reporter

```python
from pyautokit import GitHubUtils

gh = GitHubUtils(token="your-github-token")

# Create issue
issue = gh.create_issue(
    owner="Gzeu",
    repo="pyautokit",
    title="Bug: Feature X not working",
    body="""### Description
    Feature X crashes when...
    
    ### Steps to Reproduce
    1. Do this
    2. Do that
    
    ### Expected
    Should work
    
    ### Actual
    Crashes
    """,
    labels=["bug", "help-wanted"]
)

print(f"✅ Issue created: #{issue['number']}")
```

---

## ❓ Troubleshooting

### Issue: Command not found

**Problem**: `pyautokit-organizer: command not found`

**Solution**:

```bash
# 1. Check installation
pip list | grep pyautokit

# 2. Reinstall
pip uninstall pyautokit
pip install pyautokit

# 3. Check PATH
python -m pyautokit.file_organizer --help  # Alternative way
```

### Issue: Playwright not working

**Problem**: `Playwright not installed` error

**Solution**:

```bash
# Install browser support
pip install 'pyautokit[browser]'

# Download browser binaries (IMPORTANT!)
playwright install

# If still issues, install specific browser
playwright install chromium
```

### Issue: Import errors

**Problem**: `ImportError: No module named 'pyautokit'`

**Solution**:

```bash
# Check Python version (needs 3.9+)
python --version

# Use pip3 if needed
pip3 install pyautokit

# Or use python -m pip
python -m pip install pyautokit
```

### Issue: Permission denied

**Problem**: `Permission denied` when organizing files

**Solution**:

```bash
# Run with sudo (Linux/Mac) - be careful!
sudo pyautokit-organizer ~/Downloads

# Or organize a folder you own
pyautokit-organizer ~/Documents
```

---

## 🚀 Next Steps

### 1. Explore Examples

```bash
# Clone repository
git clone https://github.com/Gzeu/pyautokit.git
cd pyautokit

# Run examples
python examples/organize_downloads.py --watch
python examples/monitor_egld.py
python examples/playwright_automation.py
```

### 2. Read Documentation

- [README.md](README.md) - Full documentation
- [INSTALLATION.md](INSTALLATION.md) - Detailed installation
- [PUBLISHING.md](PUBLISHING.md) - For contributors
- [CONTRIBUTING.md](CONTRIBUTING.md) - Contribution guide

### 3. Get Help

- **Issues**: [GitHub Issues](https://github.com/Gzeu/pyautokit/issues)
- **Examples**: [examples/](examples/) directory
- **Tests**: [tests/](tests/) directory for usage examples

### 4. Customize

All modules are designed to be extended:

```python
from pyautokit import FileOrganizer

class MyOrganizer(FileOrganizer):
    def custom_organization(self, path):
        # Your custom logic here
        pass
```

---

## 📝 Quick Tips

1. **Always test with `--dry-run` first** when organizing files
2. **Use `-h` or `--help`** on any command for details
3. **Check output with `--output`** to save results
4. **Enable `--verbose`** for debugging
5. **Use environment variables** for sensitive data (tokens, passwords)

---

## ⭐ Support the Project

If PyAutokit helps you:

- ⭐ Star the [GitHub repository](https://github.com/Gzeu/pyautokit)
- 🐛 Report bugs or request features via [Issues](https://github.com/Gzeu/pyautokit/issues)
- 🤝 Contribute improvements via Pull Requests
- 📢 Share with others who might find it useful

---

**Ready to automate? Start with**: `pip install pyautokit` 🚀
