#!/bin/bash
# PyAutokit - Automated PyPI Publishing Script
# Usage: ./publish.sh [--test]  # Use --test for TestPyPI

set -e  # Exit on error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Configuration
PACKAGE_NAME="pyautokit"
VERSION="1.0.0"
TEST_PYPI="https://test.pypi.org/legacy/"
PROD_PYPI="https://upload.pypi.org/legacy/"

echo -e "${BLUE}╔════════════════════════════════════════════╗${NC}"
echo -e "${BLUE}║  PyAutokit - PyPI Publisher v1.0          ║${NC}"
echo -e "${BLUE}╚════════════════════════════════════════════╝${NC}"
echo ""

# Determine target repository
if [[ "$1" == "--test" ]]; then
    REPO="testpypi"
    REPO_URL="$TEST_PYPI"
    echo -e "${YELLOW}📦 Target: TestPyPI (test environment)${NC}"
else
    REPO="pypi"
    REPO_URL="$PROD_PYPI"
    echo -e "${GREEN}📦 Target: PyPI (PRODUCTION)${NC}"
fi
echo ""

# ============================================
# STEP 1: Pre-flight Checks
# ============================================
echo -e "${BLUE}[1/8]${NC} Running pre-flight checks..."

# Check if we're in the right directory
if [ ! -f "setup.py" ]; then
    echo -e "${RED}❌ Error: setup.py not found!${NC}"
    echo -e "${YELLOW}Run this script from the project root directory.${NC}"
    exit 1
fi

# Check for uncommitted changes
if [ -n "$(git status --porcelain)" ]; then
    echo -e "${YELLOW}⚠️  Warning: You have uncommitted changes${NC}"
    git status --short
    read -p "Continue anyway? [y/N] " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        echo -e "${RED}Aborted.${NC}"
        exit 1
    fi
fi

# Verify version tag exists
if ! git tag | grep -q "^v${VERSION}$"; then
    echo -e "${YELLOW}⚠️  Git tag v${VERSION} not found${NC}"
    read -p "Create tag v${VERSION} now? [y/N] " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        git tag -a "v${VERSION}" -m "Release v${VERSION}"
        git push origin "v${VERSION}"
        echo -e "${GREEN}✅ Tag created and pushed${NC}"
    fi
fi

echo -e "${GREEN}✅ Pre-flight checks passed${NC}"
echo ""

# ============================================
# STEP 2: Check/Install Build Tools
# ============================================
echo -e "${BLUE}[2/8]${NC} Checking build tools..."

if ! command -v twine &> /dev/null; then
    echo -e "${YELLOW}Installing twine...${NC}"
    pip install --upgrade twine
fi

if ! command -v python -m build &> /dev/null; then
    echo -e "${YELLOW}Installing build...${NC}"
    pip install --upgrade build
fi

echo -e "${GREEN}✅ Build tools ready${NC}"
echo ""

# ============================================
# STEP 3: Clean Previous Builds
# ============================================
echo -e "${BLUE}[3/8]${NC} Cleaning previous builds..."

rm -rf dist/ build/ *.egg-info/ pyautokit.egg-info/
find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
find . -type f -name '*.pyc' -delete 2>/dev/null || true
find . -type d -name '*.egg-info' -exec rm -rf {} + 2>/dev/null || true

echo -e "${GREEN}✅ Cleaned${NC}"
echo ""

# ============================================
# STEP 4: Run Tests (Optional)
# ============================================
echo -e "${BLUE}[4/8]${NC} Running tests..."

if command -v pytest &> /dev/null; then
    if pytest tests/ -v --tb=short; then
        echo -e "${GREEN}✅ All tests passed${NC}"
    else
        echo -e "${RED}❌ Tests failed${NC}"
        read -p "Continue anyway? [y/N] " -n 1 -r
        echo
        if [[ ! $REPLY =~ ^[Yy]$ ]]; then
            echo -e "${RED}Aborted.${NC}"
            exit 1
        fi
    fi
else
    echo -e "${YELLOW}⚠️  pytest not installed - skipping tests${NC}"
fi
echo ""

# ============================================
# STEP 5: Build Package
# ============================================
echo -e "${BLUE}[5/8]${NC} Building package..."

python -m build

if [ $? -eq 0 ]; then
    echo -e "${GREEN}✅ Package built successfully${NC}"
    echo ""
    echo "Built files:"
    ls -lh dist/
    echo ""
else
    echo -e "${RED}❌ Build failed${NC}"
    exit 1
fi

# ============================================
# STEP 6: Validate Package
# ============================================
echo -e "${BLUE}[6/8]${NC} Validating package..."

if twine check dist/*; then
    echo -e "${GREEN}✅ Package validation passed${NC}"
else
    echo -e "${RED}❌ Package validation failed${NC}"
    exit 1
fi
echo ""

# ============================================
# STEP 7: Upload to PyPI
# ============================================
echo -e "${BLUE}[7/8]${NC} Uploading to ${REPO}..."
echo ""
echo -e "${YELLOW}╔════════════════════════════════════════════╗${NC}"
echo -e "${YELLOW}║  AUTHENTICATION REQUIRED                   ║${NC}"
echo -e "${YELLOW}╚════════════════════════════════════════════╝${NC}"
echo ""
echo -e "Username: ${GREEN}__token__${NC}"
echo -e "Password: ${YELLOW}[Your PyPI API token]${NC}"
echo ""

if [[ "$REPO" == "testpypi" ]]; then
    echo -e "${BLUE}Get TestPyPI token:${NC} https://test.pypi.org/manage/account/token/"
    twine upload --repository testpypi dist/*
else
    echo -e "${BLUE}Get PyPI token:${NC} https://pypi.org/manage/account/token/"
    twine upload dist/*
fi

if [ $? -eq 0 ]; then
    echo ""
    echo -e "${GREEN}✅ Upload successful!${NC}"
else
    echo -e "${RED}❌ Upload failed${NC}"
    exit 1
fi
echo ""

# ============================================
# STEP 8: Verify Installation
# ============================================
echo -e "${BLUE}[8/8]${NC} Verifying installation..."
echo ""

if [[ "$REPO" == "testpypi" ]]; then
    echo -e "${YELLOW}Test installation:${NC}"
    echo "pip install --index-url https://test.pypi.org/simple/ \\"
    echo "    --extra-index-url https://pypi.org/simple/ pyautokit"
else
    echo -e "${GREEN}Installation command:${NC}"
    echo "pip install pyautokit"
    echo ""
    echo -e "${GREEN}Package URL:${NC}"
    echo "https://pypi.org/project/pyautokit/${VERSION}/"
fi

echo ""
echo -e "${GREEN}╔════════════════════════════════════════════╗${NC}"
echo -e "${GREEN}║  ✅ PUBLICATION COMPLETE!                  ║${NC}"
echo -e "${GREEN}╚════════════════════════════════════════════╝${NC}"
echo ""
echo -e "${BLUE}Next steps:${NC}"
echo "  1. Test installation: pip install pyautokit"
echo "  2. Verify: pyautokit --version"
echo "  3. Create GitHub Release at:"
echo "     https://github.com/Gzeu/pyautokit/releases/new"
echo ""
echo -e "${GREEN}🎉 Congratulations on your PyPI release!${NC}"
echo ""
