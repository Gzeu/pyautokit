"""PyAutokit - Python Automation Toolkit."""

__version__ = "1.0.0"
__author__ = "George"

from .logger import setup_logger
from .config import Config

__all__ = ["setup_logger", "Config"]