"""PyAutokit - Python Automation Toolkit.

A comprehensive collection of automation utilities for everyday tasks.
Each module provides both CLI and programmatic interfaces.

Modules:
    - file_organizer: Organize files by extension, date, category, or size
    - web_scraper: Ethical web scraping with rate limiting
    - email_automation: SMTP email automation with templates
    - backup_manager: Backup management with compression and versioning
    - log_analyzer: Parse and analyze log files
    - api_client: Generic REST API client with retry logic
    - data_processor: CSV/JSON conversion and data transformation
    - task_scheduler: Cron-like task scheduling
    - security_utils: Encryption, hashing, and password generation
    - blockchain_monitor: Cryptocurrency price monitoring

Examples:
    >>> from pyautokit.file_organizer import FileOrganizer
    >>> organizer = FileOrganizer()
    >>> results = organizer.organize_by_category("/path/to/folder")
    
    >>> from pyautokit.blockchain_monitor import BlockchainMonitor
    >>> monitor = BlockchainMonitor()
    >>> price = monitor.get_price("EGLD")

CLI Usage:
    $ python -m pyautokit.file_organizer ~/Downloads --method category
    $ python -m pyautokit.blockchain_monitor --coin EGLD
    $ pyautokit-organizer ~/Downloads --dry-run
    $ pyautokit-crypto --coin BTC
"""

__version__ = "1.0.0"
__author__ = "George Pricop"
__email__ = "contact@georgepricop.com"
__license__ = "MIT"

# Import main classes for easy access
from .file_organizer import FileOrganizer, SortMethod
from .web_scraper import WebScraper
from .email_automation import EmailClient
from .backup_manager import BackupManager
from .log_analyzer import LogAnalyzer
from .api_client import APIClient
from .data_processor import DataProcessor
from .task_scheduler import TaskScheduler
from .security_utils import SecurityUtils
from .blockchain_monitor import BlockchainMonitor

__all__ = [
    "FileOrganizer",
    "SortMethod",
    "WebScraper",
    "EmailClient",
    "BackupManager",
    "LogAnalyzer",
    "APIClient",
    "DataProcessor",
    "TaskScheduler",
    "SecurityUtils",
    "BlockchainMonitor",
]
