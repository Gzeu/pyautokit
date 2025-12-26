# Publishing PyAutokit to PyPI

Complete guide for publishing PyAutokit to the Python Package Index.

## Prerequisites

### 1. Install Build Tools

```bash
pip install --upgrade pip setuptools wheel twine build
```

### 2. Create PyPI Account

- **PyPI**: https://pypi.org/account/register/
- **TestPyPI** (for testing): https://test.pypi.org/account/register/

### 3. Create API Token

1. Go to https://pypi.org/manage/account/token/
2. Create new token with scope "Entire account"
3. Save token securely (starts with `pypi-`)

## Build Package

### Clean Previous Builds

```bash
# Remove old build artifacts
rm -rf build/ dist/ *.egg-info/

# Clean Python cache
find . -type d -name __pycache__ -exec rm -rf {} +
find . -type f -name '*.pyc' -delete
```

### Build Distribution

```bash
# Build source distribution and wheel
python -m build

# This creates:
# - dist/pyautokit-1.0.0.tar.gz (source distribution)
# - dist/pyautokit-1.0.0-py3-none-any.whl (wheel)
```

### Verify Build

```bash
# Check package
twine check dist/*

# Should show:
# Checking dist/pyautokit-1.0.0.tar.gz: PASSED
# Checking dist/pyautokit-1.0.0-py3-none-any.whl: PASSED
```

## Test on TestPyPI

### Upload to TestPyPI

```bash
# Upload to TestPyPI first
twine upload --repository testpypi dist/*

# Enter your TestPyPI API token when prompted
# Username: __token__
# Password: pypi-...
```

### Test Installation

```bash
# Create fresh virtual environment
python -m venv test_env
source test_env/bin/activate  # Windows: test_env\Scripts\activate

# Install from TestPyPI
pip install --index-url https://test.pypi.org/simple/ \
    --extra-index-url https://pypi.org/simple/ \
    pyautokit

# Test commands
pyautokit --version
pyautokit-organizer --help
pyautokit-crypto --coin EGLD

# Test programmatic usage
python -c "from pyautokit import FileOrganizer; print('Success!')"

# Clean up
deactivate
rm -rf test_env
```

## Publish to PyPI

### Upload to PyPI

```bash
# Upload to real PyPI
twine upload dist/*

# Enter your PyPI API token
# Username: __token__
# Password: pypi-...
```

### Verify Publication

```bash
# Check on PyPI
# https://pypi.org/project/pyautokit/

# Test installation
pip install pyautokit

# Verify
pyautokit --version
```

## Using .pypirc (Optional)

Create `~/.pypirc` to store credentials:

```ini
[distutils]
index-servers =
    pypi
    testpypi

[pypi]
username = __token__
password = pypi-YOUR_API_TOKEN_HERE

[testpypi]
repository = https://test.pypi.org/legacy/
username = __token__
password = pypi-YOUR_TESTPYPI_TOKEN_HERE
```

**Important**: Keep `.pypirc` secure (chmod 600)!

```bash
chmod 600 ~/.pypirc
```

With `.pypirc`, you can upload without entering credentials:

```bash
twine upload dist/*  # Uses .pypirc automatically
```

## GitHub Actions Automation

Automatic publishing on release (see `.github/workflows/publish.yml`):

1. Create GitHub release with tag `v1.0.0`
2. GitHub Actions automatically:
   - Runs tests
   - Builds package
   - Publishes to PyPI

### Setup GitHub Secrets

1. Go to repository Settings > Secrets and variables > Actions
2. Add new secret:
   - Name: `PYPI_API_TOKEN`
   - Value: Your PyPI API token

## Version Management

### Update Version

Update version in these files:

1. `setup.py` - `version="1.0.1"`
2. `pyproject.toml` - `version = "1.0.1"`
3. `pyautokit/__init__.py` - `__version__ = "1.0.1"`

### Version Numbering

Follow Semantic Versioning (SemVer):

- **Major** (1.0.0 -> 2.0.0): Breaking changes
- **Minor** (1.0.0 -> 1.1.0): New features, backward compatible
- **Patch** (1.0.0 -> 1.0.1): Bug fixes

## Publishing Checklist

- [ ] Update version number in all files
- [ ] Update CHANGELOG.md
- [ ] Run tests: `pytest`
- [ ] Update README.md if needed
- [ ] Clean build artifacts: `rm -rf dist/ build/`
- [ ] Build package: `python -m build`
- [ ] Check package: `twine check dist/*`
- [ ] Test on TestPyPI first
- [ ] Upload to PyPI: `twine upload dist/*`
- [ ] Create GitHub release
- [ ] Test installation: `pip install pyautokit`
- [ ] Verify commands work

## Common Issues

### Issue: "File already exists"

**Solution**: Increment version number. PyPI doesn't allow re-uploading same version.

### Issue: "Invalid authentication"

**Solution**: 
- Username must be `__token__`
- Password must be full API token (starts with `pypi-`)

### Issue: "Package name already taken"

**Solution**: Choose different package name in `setup.py`.

### Issue: "Dependencies not found"

**Solution**: When testing from TestPyPI, use `--extra-index-url https://pypi.org/simple/` to get dependencies from PyPI.

## Post-Publication

### Update Documentation

1. Update README badges:
   ```markdown
   [![PyPI version](https://badge.fury.io/py/pyautokit.svg)](https://badge.fury.io/py/pyautokit)
   [![Downloads](https://pepy.tech/badge/pyautokit)](https://pepy.tech/project/pyautokit)
   ```

2. Update installation instructions:
   ```bash
   pip install pyautokit
   ```

### Monitor Package

- PyPI stats: https://pypistats.org/packages/pyautokit
- Download trends: https://pepy.tech/project/pyautokit
- Issues: https://github.com/Gzeu/pyautokit/issues

## Quick Reference

```bash
# Complete workflow
rm -rf dist/ build/
python -m build
twine check dist/*
twine upload --repository testpypi dist/*  # Test first
twine upload dist/*  # Production
```

## Resources

- **PyPI**: https://pypi.org/
- **TestPyPI**: https://test.pypi.org/
- **Packaging Guide**: https://packaging.python.org/
- **Twine Docs**: https://twine.readthedocs.io/
- **Setuptools**: https://setuptools.pypa.io/

---

**Ready to publish? Run the checklist and deploy! 🚀**
