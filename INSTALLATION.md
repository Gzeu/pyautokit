# PyAutokit Installation Guide

Multiple ways to install and use PyAutokit.

## 🚀 Quick Install

### From PyPI (Recommended)

```bash
pip install pyautokit
```

That's it! All commands are now available:

```bash
pyautokit --version
pyautokit-organizer --help
pyautokit-crypto --coin EGLD
```

## 📘 Installation Methods

### 1. Standard Installation

```bash
# Install latest stable version
pip install pyautokit

# Install specific version
pip install pyautokit==1.0.0

# Upgrade to latest
pip install --upgrade pyautokit
```

### 2. Install with Optional Dependencies

```bash
# Install with file watching support
pip install pyautokit[watch]

# Install with development tools
pip install pyautokit[dev]

# Install everything
pip install pyautokit[all]
```

### 3. Install from Source

```bash
# Clone repository
git clone https://github.com/Gzeu/pyautokit.git
cd pyautokit

# Install in development mode
pip install -e .

# Or install normally
pip install .
```

### 4. Install from GitHub

```bash
# Latest from main branch
pip install git+https://github.com/Gzeu/pyautokit.git

# Specific branch
pip install git+https://github.com/Gzeu/pyautokit.git@develop

# Specific tag/release
pip install git+https://github.com/Gzeu/pyautokit.git@v1.0.0
```

## 💻 Platform-Specific

### Linux/macOS

```bash
# System-wide (requires sudo)
sudo pip install pyautokit

# User install (recommended)
pip install --user pyautokit

# Virtual environment (best practice)
python3 -m venv venv
source venv/bin/activate
pip install pyautokit
```

### Windows

```powershell
# Standard install
pip install pyautokit

# Virtual environment
python -m venv venv
venv\Scripts\activate
pip install pyautokit
```

### Docker

```dockerfile
FROM python:3.11-slim

RUN pip install pyautokit

ENTRYPOINT ["pyautokit"]
```

Build and run:

```bash
docker build -t pyautokit .
docker run pyautokit --version
docker run -v $(pwd):/data pyautokit-organizer /data --stats
```

## ⚙️ Configuration

### Environment Setup

```bash
# Create .env file
cat > .env << EOF
LOG_LEVEL=INFO
EMAIL_SMTP_SERVER=smtp.gmail.com
EMAIL_SMTP_PORT=587
EMAIL_SENDER=your-email@gmail.com
EMAIL_PASSWORD=your-app-password
EOF
```

### Verify Installation

```bash
# Check version
pyautokit --version
python -c "import pyautokit; print(pyautokit.__version__)"

# List available commands
pyautokit --help

# Test each module
pyautokit-organizer --help
pyautokit-scraper --help
pyautokit-email --help
pyautokit-backup --help
pyautokit-logs --help
pyautokit-data --help
pyautokit-security --help
pyautokit-crypto --help
```

## 🐍 Python Version Requirements

- **Minimum**: Python 3.9
- **Recommended**: Python 3.11+
- **Tested**: 3.9, 3.10, 3.11, 3.12

Check your Python version:

```bash
python --version
```

## 📦 Dependencies

### Core Dependencies (Auto-installed)

- `python-dotenv>=1.0.0` - Environment configuration
- `requests>=2.31.0` - HTTP requests
- `beautifulsoup4>=4.12.0` - Web scraping
- `lxml>=4.9.0` - XML/HTML parsing
- `schedule>=1.2.0` - Task scheduling
- `cryptography>=41.0.0` - Encryption/security

### Optional Dependencies

```bash
# File monitoring (for auto-watch mode)
pip install watchdog>=3.0.0

# Development tools
pip install pytest pytest-cov black flake8 mypy
```

## 🔧 Troubleshooting

### Common Issues

#### "Command not found: pyautokit"

**Solution**: Ensure pip bin directory is in PATH:

```bash
# Linux/macOS
export PATH="$HOME/.local/bin:$PATH"

# Windows (add to PATH environment variable)
C:\Users\YourName\AppData\Local\Programs\Python\Python311\Scripts
```

#### "Permission denied"

**Solution**: Use `--user` flag:

```bash
pip install --user pyautokit
```

#### "Module not found: cryptography"

**Solution**: Install build dependencies:

```bash
# Ubuntu/Debian
sudo apt-get install build-essential libssl-dev libffi-dev python3-dev

# macOS
brew install openssl

# Then retry
pip install pyautokit
```

#### "SSL Certificate Error"

**Solution**: Update certificates:

```bash
pip install --upgrade certifi
```

## 🔄 Updating

```bash
# Upgrade to latest version
pip install --upgrade pyautokit

# Force reinstall
pip install --force-reinstall pyautokit

# Check current version
pip show pyautokit
```

## 🗑️ Uninstalling

```bash
# Remove package
pip uninstall pyautokit

# Remove with dependencies
pip uninstall pyautokit python-dotenv requests beautifulsoup4 lxml schedule cryptography
```

## 🐳 Using with Pipenv

```bash
# Install with Pipenv
pipenv install pyautokit

# With optional dependencies
pipenv install pyautokit[all]

# Activate environment
pipenv shell

# Use commands
pyautokit --version
```

## 🐍 Using with Poetry

```bash
# Add to project
poetry add pyautokit

# With extras
poetry add pyautokit[all]

# Use in project
poetry run pyautokit --version
```

## 🧪 Testing Installation

```bash
# Run quick test
python << EOF
from pyautokit import FileOrganizer, BlockchainMonitor
print("FileOrganizer:", FileOrganizer)
print("BlockchainMonitor:", BlockchainMonitor)
print("✅ PyAutokit installed successfully!")
EOF

# Test CLI commands
pyautokit-security genpass --length 16
pyautokit-crypto --coin EGLD
```

## 📄 Next Steps

After installation:

1. **Read the README**: [README.md](README.md)
2. **Try examples**: `cd examples && python organize_downloads.py --help`
3. **Configure .env**: Copy `.env.example` and customize
4. **Run tests**: `pytest tests/`
5. **Start automating**: Choose a module and start using it!

## 📚 Resources

- **PyPI Package**: https://pypi.org/project/pyautokit/
- **GitHub**: https://github.com/Gzeu/pyautokit
- **Documentation**: [README.md](README.md)
- **Examples**: [examples/](examples/)
- **Contributing**: [CONTRIBUTING.md](CONTRIBUTING.md)

---

**Happy Automating! 🚀**
