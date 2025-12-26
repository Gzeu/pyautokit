# Publishing PyAutokit to PyPI

Complete guide for publishing PyAutokit to the Python Package Index (PyPI).

## 📚 Prerequisites

### 1. Install Build Tools

```bash
pip install --upgrade pip setuptools wheel twine build
```

### 2. Create PyPI Account

- **PyPI** (production): https://pypi.org/account/register/
- **TestPyPI** (testing): https://test.pypi.org/account/register/

### 3. Generate API Token

1. Go to https://pypi.org/manage/account/token/
2. Create new API token
3. Scope: "Entire account" or "pyautokit" project
4. Save token securely (you'll only see it once!)

## 🛠️ Build & Test Locally

### 1. Clean Previous Builds

```bash
rm -rf build/ dist/ *.egg-info
```

### 2. Build Distribution

```bash
# Using build (recommended)
python -m build

# Or using setup.py
python setup.py sdist bdist_wheel
```

This creates:
- `dist/pyautokit-1.0.0.tar.gz` (source distribution)
- `dist/pyautokit-1.0.0-py3-none-any.whl` (wheel)

### 3. Check Package

```bash
# Check distribution files
twine check dist/*
```

### 4. Test Installation Locally

```bash
# Install from wheel
pip install dist/pyautokit-1.0.0-py3-none-any.whl

# Test CLI
pyautokit --version
pyautokit-organize --help

# Uninstall
pip uninstall pyautokit -y
```

## 🧪 Test on TestPyPI First

### 1. Upload to TestPyPI

```bash
twine upload --repository testpypi dist/*
```

### 2. Test Installation from TestPyPI

```bash
pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ pyautokit

# Test
pyautokit --version
pyautokit-organize --help

# Uninstall
pip uninstall pyautokit -y
```

## 🚀 Publish to Production PyPI

### 1. Upload to PyPI

```bash
twine upload dist/*
```

### 2. Test Installation

```bash
# Install from PyPI
pip install pyautokit

# Test CLI
pyautokit --version
pyautokit-organize ~/Downloads --dry-run
pyautokit-crypto --coin EGLD

# Install with extras
pip install pyautokit[watch]  # File monitoring
pip install pyautokit[dev]    # Development tools
pip install pyautokit[all]    # Everything
```

## ✅ Checklist Before Publishing

- [ ] All tests passing (`pytest`)
- [ ] Version updated in setup.py, setup.cfg, pyproject.toml
- [ ] README.md is current
- [ ] LICENSE file present
- [ ] Clean build (`rm -rf build/ dist/ *.egg-info`)
- [ ] Build successful (`python -m build`)
- [ ] Package check passes (`twine check dist/*`)
- [ ] Tested on TestPyPI
- [ ] Git tag created (`git tag v1.0.0`)
- [ ] Changes pushed to GitHub

## 🔗 Resources

- **PyPI**: https://pypi.org/
- **TestPyPI**: https://test.pypi.org/
- **Packaging Guide**: https://packaging.python.org/
- **Twine Docs**: https://twine.readthedocs.io/

---

**Ready to publish:**

```bash
python -m build && twine check dist/* && twine upload dist/*
```
