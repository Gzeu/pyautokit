"""File organization and categorization utility."""

import argparse
import shutil
from pathlib import Path
from typing import Dict, List
from enum import Enum
from .logger import setup_logger
from .utils import get_file_extension, get_file_creation_date, get_all_files
from .config import Config

logger = setup_logger("FileOrganizer", level=Config.LOG_LEVEL)


class SortMethod(Enum):
    """File sorting methods."""
    EXTENSION = "extension"
    DATE = "date"
    SIZE = "size"


class FileOrganizer:
    """Organize and categorize files in directories."""

    FILE_CATEGORIES: Dict[str, List[str]] = {
        "Documents": ["pdf", "doc", "docx", "txt", "xlsx", "xls", "ppt"],
        "Images": ["jpg", "jpeg", "png", "gif", "bmp", "svg", "webp"],
        "Videos": ["mp4", "avi", "mov", "mkv", "flv", "wmv"],
        "Audio": ["mp3", "wav", "flac", "m4a", "aac", "wma"],
        "Archives": ["zip", "rar", "7z", "tar", "gz"],
        "Code": ["py", "js", "ts", "java", "cpp", "c", "go", "rs"],
        "Data": ["json", "csv", "xml", "sql"],
    }

    def __init__(self, create_folders: bool = True):
        """Initialize organizer."""
        self.create_folders = create_folders

    def categorize_file(self, file_path: Path) -> str:
        """Determine category for file."""
        ext = get_file_extension(file_path)
        for category, extensions in self.FILE_CATEGORIES.items():
            if ext in extensions:
                return category
        return "Other"

    def organize_by_extension(self, directory: Path) -> Dict[str, int]:
        """Organize files by extension."""
        directory = Path(directory)
        results = {}

        for file_path in get_all_files(directory):
            ext = get_file_extension(file_path)
            folder = directory / ext.upper()

            if self.create_folders:
                folder.mkdir(exist_ok=True)
                try:
                    shutil.move(str(file_path), str(folder / file_path.name))
                    results[ext] = results.get(ext, 0) + 1
                    logger.info(f"Moved {file_path.name} to {ext.upper()}/")
                except Exception as e:
                    logger.error(f"Failed to move {file_path.name}: {e}")

        return results

    def organize_by_date(self, directory: Path) -> Dict[str, int]:
        """Organize files by date (YYYY-MM-DD)."""
        directory = Path(directory)
        results = {}

        for file_path in get_all_files(directory):
            date = get_file_creation_date(file_path)
            folder = directory / date

            if self.create_folders:
                folder.mkdir(exist_ok=True)
                try:
                    shutil.move(str(file_path), str(folder / file_path.name))
                    results[date] = results.get(date, 0) + 1
                except Exception as e:
                    logger.error(f"Failed to move {file_path.name}: {e}")

        return results

    def organize_by_category(self, directory: Path) -> Dict[str, int]:
        """Organize files by category (Documents, Images, etc)."""
        directory = Path(directory)
        results = {}

        for file_path in get_all_files(directory):
            category = self.categorize_file(file_path)
            folder = directory / category

            if self.create_folders:
                folder.mkdir(exist_ok=True)
                try:
                    shutil.move(str(file_path), str(folder / file_path.name))
                    results[category] = results.get(category, 0) + 1
                except Exception as e:
                    logger.error(f"Failed to move {file_path.name}: {e}")

        return results


def main() -> None:
    """CLI for file organizer."""
    parser = argparse.ArgumentParser(
        description="Organize files in directory"
    )
    parser.add_argument(
        "directory",
        type=str,
        help="Directory to organize"
    )
    parser.add_argument(
        "--method",
        choices=["extension", "date", "category"],
        default="extension",
        help="Organization method"
    )
    parser.add_argument(
        "--no-create",
        action="store_true",
        help="Don't create folders"
    )

    args = parser.parse_args()
    directory = Path(args.directory)

    if not directory.is_dir():
        logger.error(f"Directory not found: {directory}")
        return

    organizer = FileOrganizer(create_folders=not args.no_create)

    if args.method == "extension":
        results = organizer.organize_by_extension(directory)
    elif args.method == "date":
        results = organizer.organize_by_date(directory)
    else:
        results = organizer.organize_by_category(directory)

    logger.info(f"Organization complete: {results}")


if __name__ == "__main__":
    main()