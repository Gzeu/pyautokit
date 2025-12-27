# PyPI Publishing Guide for PyAutokit

Complete guide to publish PyAutokit to PyPI (Python Package Index).

## 📋 Prerequisites

- ✅ Python 3.9+
- ✅ Git installed
- ✅ GitHub account (you have this)
- ✅ PyPI account (we'll create this)

---

## 🔐 STEP 1: Create PyPI Account

### A. Create Production PyPI Account

1. **Go to PyPI**: https://pypi.org/account/register/

2. **Fill in details**:
   - Username: `Gzeu` (or your preferred username)
   - Email: Your email
   - Password: Strong password
   - Full name: George Pricop

3. **Verify email**:
   - Check your inbox
   - Click verification link
   - Account activated! ✅

### B. Create TestPyPI Account (Optional but Recommended)

**TestPyPI** = Test environment, safe to experiment

1. **Go to TestPyPI**: https://test.pypi.org/account/register/
2. Same steps as above
3. This is your sandbox for testing

---

## 🔑 STEP 2: Generate API Token

### Why API Token?
- ✅ More secure than password
- ✅ Can be revoked anytime
- ✅ Scoped to specific projects
- ✅ Required for automated publishing

### A. Production PyPI Token

1. **Login to PyPI**: https://pypi.org/

2. **Go to Account Settings**:
   - Click your username (top right)
   - Select "Account settings"

3. **Create API Token**:
   - Scroll to "API tokens" section
   - Click **"Add API token"**

4. **Configure Token**:
   - **Token name**: `pyautokit-publisher` (or any name)
   - **Scope**: 
     - For first publish: Select **"Entire account"**
     - After first publish: Select **"Project: pyautokit"**
   - Click **"Create token"**

5. **COPY TOKEN IMMEDIATELY** ⚠️
   ```
   pypi-AgEIcHlwaS5vcmcC...very-long-string...xyz123
   ```
   - This shows **ONLY ONCE**!
   - Save it securely (password manager)
   - You'll need this for publishing

### B. TestPyPI Token (Optional)

1. **Login to TestPyPI**: https://test.pypi.org/
2. Same steps as above
3. Save token separately (different from production)

---

## 🚀 STEP 3: Publish Using Automated Script

### Option A: Publish to Production PyPI (RECOMMENDED)

```bash
# Navigate to project
cd ~/pyautokit  # or your path

# Make script executable
chmod +x publish.sh

# Run publisher
./publish.sh

# When prompted:
# Username: __token__
# Password: [paste your pypi-... token]
```

### Option B: Test on TestPyPI First (SAFER)

```bash
# Test first on TestPyPI
./publish.sh --test

# When prompted:
# Username: __token__
# Password: [paste your test.pypi token]

# If successful, publish to production:
./publish.sh
```

---

## 📝 STEP 4: Manual Publishing (Alternative)

If you prefer manual control:

### Install Tools
```bash
pip install --upgrade pip setuptools wheel build twine
```

### Clean & Build
```bash
# Clean previous builds
rm -rf dist/ build/ *.egg-info/

# Build package
python -m build

# Verify
ls -lh dist/
# Should show:
#   pyautokit-1.0.0-py3-none-any.whl
#   pyautokit-1.0.0.tar.gz
```

### Validate
```bash
twine check dist/*

# Should output:
# Checking dist/pyautokit-1.0.0-py3-none-any.whl: PASSED
# Checking dist/pyautokit-1.0.0.tar.gz: PASSED
```

### Upload to TestPyPI (Optional)
```bash
twine upload --repository testpypi dist/*

# Username: __token__
# Password: [TestPyPI token]
```

### Upload to Production PyPI
```bash
twine upload dist/*

# Username: __token__
# Password: [PyPI token]

# Success! Package published at:
# https://pypi.org/project/pyautokit/1.0.0/
```

---

## ✅ STEP 5: Verify Publication

### Test Installation
```bash
# Wait 1-2 minutes for PyPI indexing

# Install from PyPI
pip install pyautokit

# Verify version
pyautokit --version
# Output: PyAutokit 1.0.0

# Test commands
pyautokit-organizer --help
pyautokit-crypto --coin EGLD
pyautokit-security genpass --length 20

# Test imports
python -c "from pyautokit import FileOrganizer; print('✅ Success!')"
```

### Check PyPI Page
Visit: https://pypi.org/project/pyautokit/

Should show:
- ✅ Package name: pyautokit
- ✅ Version: 1.0.0
- ✅ Description from README.md
- ✅ Installation command
- ✅ Project links

---

## 🎯 STEP 6: Post-Publication

### Create GitHub Release

1. **Go to**: https://github.com/Gzeu/pyautokit/releases/new

2. **Fill in**:
   - **Tag**: `v1.0.0`
   - **Title**: `PyAutokit v1.0.0 - First PyPI Release`
   - **Description**: See template below

3. **Release Description Template**:
```markdown
# 🎉 PyAutokit v1.0.0 - First PyPI Release

## Installation

\`\`\`bash
pip install pyautokit
\`\`\`

## What's New

✅ **11 Complete Modules** with CLI
✅ **File Organizer** - Organize files by category/date/extension
✅ **Web Scraper** - BeautifulSoup & Playwright support
✅ **Email Automation** - SMTP with templates
✅ **Backup Manager** - Versioned backups with compression
✅ **Security Utils** - Encryption, hashing, password generation
✅ **Blockchain Monitor** - Real-time crypto prices (EGLD, BTC, ETH)
✅ **GitHub Utils** - Repository and issue management
✅ **Playwright Browser** - Screenshots, PDF, testing
✅ **80%+ Test Coverage** on 4 core modules

## Quick Start

\`\`\`bash
# Basic usage
pip install pyautokit
pyautokit-organizer ~/Downloads --dry-run
pyautokit-crypto --coin EGLD

# With browser automation
pip install 'pyautokit[browser]'
playwright install
pyautokit-browser screenshot https://example.com -o page.png
\`\`\`

## Links

- 📦 PyPI: https://pypi.org/project/pyautokit/
- 📖 Documentation: https://github.com/Gzeu/pyautokit
- 💡 Examples: https://github.com/Gzeu/pyautokit/tree/main/examples
- 🐛 Issues: https://github.com/Gzeu/pyautokit/issues
```

### Update README Badge (Optional)

Add PyPI badge to README.md:
```markdown
[![PyPI version](https://badge.fury.io/py/pyautokit.svg)](https://pypi.org/project/pyautokit/)
[![Downloads](https://pepy.tech/badge/pyautokit)](https://pepy.tech/project/pyautokit)
```

---

## 🔒 Security Best Practices

### Protect Your API Token

✅ **DO**:
- Save token in password manager
- Use scoped tokens (project-specific)
- Revoke tokens when not needed
- Use different tokens for test/production

❌ **DON'T**:
- Commit tokens to Git
- Share tokens publicly
- Use same token everywhere
- Leave unused tokens active

### Store Token Securely (Optional)

Create `~/.pypirc` (Unix) or `%USERPROFILE%\.pypirc` (Windows):

```ini
[distutils]
index-servers =
    pypi
    testpypi

[pypi]
username = __token__
password = pypi-AgEIcHlwaS5vcmcC...your-token...

[testpypi]
repository = https://test.pypi.org/legacy/
username = __token__
password = pypi-AgEIcHlwaS5vcmcC...your-test-token...
```

**Important**: Add to `.gitignore`:
```bash
echo "~/.pypirc" >> .gitignore
```

---

## 🐛 Troubleshooting

### Error: "Invalid or non-existent authentication"

**Cause**: Wrong username or token

**Solution**:
- Username MUST be exactly: `__token__`
- Password = Full token (starts with `pypi-`)
- Copy token correctly (no spaces)

### Error: "File already exists"

**Cause**: Version 1.0.0 already published

**Solution**:
1. Update version in `setup.py` and `pyproject.toml`:
   ```python
   version="1.0.1"  # or 1.1.0
   ```
2. Create new git tag:
   ```bash
   git tag v1.0.1
   git push origin v1.0.1
   ```
3. Rebuild and upload again

### Error: "The user '...' isn't allowed to upload"

**Cause**: Token scope issue

**Solution**:
1. For FIRST upload: Use "Entire account" scope
2. After first upload: Create project-specific token
3. Update token in script/config

### Error: "Package name not available"

**Cause**: Someone else owns `pyautokit`

**Solution**:
1. Try alternative name: `pyautokit-gzeu`
2. Update name in `setup.py` and `pyproject.toml`
3. Rebuild package

### Error: "Metadata validation failed"

**Cause**: Invalid setup.py metadata

**Solution**:
```bash
# Check what's wrong
twine check dist/*

# Fix errors in setup.py
# Common issues:
# - Invalid classifier
# - Missing required field
# - Invalid version format
```

---

## 📊 Version Management

### Semantic Versioning

Follow: `MAJOR.MINOR.PATCH`

- **MAJOR** (1.x.x): Breaking changes
- **MINOR** (x.1.x): New features (backward compatible)
- **PATCH** (x.x.1): Bug fixes

### Publishing New Version

```bash
# 1. Update version
vim setup.py         # Change version="1.0.1"
vim pyproject.toml   # Change version = "1.0.1"

# 2. Commit changes
git add setup.py pyproject.toml
git commit -m "chore: Bump version to 1.0.1"
git push

# 3. Create tag
git tag -a v1.0.1 -m "Release v1.0.1"
git push origin v1.0.1

# 4. Publish
./publish.sh
```

---

## 🎯 Checklist

Before publishing:

- [ ] PyPI account created
- [ ] API token generated and saved
- [ ] All tests passing
- [ ] Version number updated
- [ ] Git tag created
- [ ] No uncommitted changes
- [ ] README.md complete
- [ ] LICENSE file present

After publishing:

- [ ] Package installs successfully
- [ ] CLI commands work
- [ ] Module imports work
- [ ] GitHub release created
- [ ] PyPI page looks good
- [ ] Documentation updated

---

## 📞 Support

**Need Help?**

- PyPI Help: https://pypi.org/help/
- Packaging Guide: https://packaging.python.org/
- Twine Docs: https://twine.readthedocs.io/
- Issues: https://github.com/Gzeu/pyautokit/issues

---

## 🎉 You're Ready!

Follow the steps above and you'll have PyAutokit published on PyPI in ~10 minutes!

**Quick Start**: Run `./publish.sh` and follow the prompts! 🚀
