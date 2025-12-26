#!/usr/bin/env python3
"""Example: Organize Downloads folder by file type."""

from pathlib import Path
from pyautokit.file_organizer import FileOrganizer
from pyautokit.logger import setup_logger

logger = setup_logger("OrganizeDownloads")


def main():
    """Organize Downloads folder."""
    downloads = Path.home() / "Downloads"
    
    if not downloads.exists():
        logger.error(f"Downloads folder not found: {downloads}")
        return
    
    logger.info(f"Organizing {downloads}")
    
    organizer = FileOrganizer(create_folders=True)
    
    # Organize by category (Documents, Images, Videos, etc.)
    results = organizer.organize_by_category(downloads)
    
    logger.info("Organization complete!")
    for category, count in results.items():
        logger.info(f"  {category}: {count} files")


if __name__ == "__main__":
    main()
