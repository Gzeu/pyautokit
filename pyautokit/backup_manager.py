"""Backup management with compression and versioning."""

import argparse
import shutil
import zipfile
import tarfile
from pathlib import Path
from datetime import datetime
from typing import List, Optional
from .logger import setup_logger
from .config import Config
from .utils import format_bytes, get_file_hash

logger = setup_logger("BackupManager", level=Config.LOG_LEVEL)


class BackupManager:
    """Manage backups with compression and versioning."""

    def __init__(
        self,
        backup_dir: Path = Config.BACKUPS_DIR,
        compression: str = Config.BACKUP_COMPRESSION,
        keep_versions: int = Config.BACKUP_KEEP_VERSIONS
    ):
        """Initialize backup manager.
        
        Args:
            backup_dir: Directory to store backups
            compression: Compression type (zip, tar, tar.gz)
            keep_versions: Number of backup versions to keep
        """
        self.backup_dir = Path(backup_dir)
        self.backup_dir.mkdir(parents=True, exist_ok=True)
        self.compression = compression
        self.keep_versions = keep_versions

    def _get_timestamp(self) -> str:
        """Get formatted timestamp for backup naming."""
        return datetime.now().strftime("%Y%m%d_%H%M%S")

    def _create_zip_backup(
        self,
        source: Path,
        backup_path: Path
    ) -> None:
        """Create ZIP backup.
        
        Args:
            source: Source directory or file
            backup_path: Backup file path
        """
        with zipfile.ZipFile(backup_path, "w", zipfile.ZIP_DEFLATED) as zipf:
            if source.is_file():
                zipf.write(source, source.name)
            else:
                for file_path in source.rglob("*"):
                    if file_path.is_file():
                        arcname = file_path.relative_to(source.parent)
                        zipf.write(file_path, arcname)

    def _create_tar_backup(
        self,
        source: Path,
        backup_path: Path,
        compression: Optional[str] = None
    ) -> None:
        """Create TAR backup.
        
        Args:
            source: Source directory or file
            backup_path: Backup file path
            compression: Compression mode (gz, bz2, xz)
        """
        mode = f"w:{compression}" if compression else "w"
        with tarfile.open(backup_path, mode) as tar:
            tar.add(source, arcname=source.name)

    def create_backup(
        self,
        source: Path,
        name: Optional[str] = None
    ) -> Optional[Path]:
        """Create backup of source.
        
        Args:
            source: Source path to backup
            name: Custom backup name (default: source name)
            
        Returns:
            Path to created backup or None on failure
        """
        source = Path(source)
        if not source.exists():
            logger.error(f"Source not found: {source}")
            return None

        if name is None:
            name = source.name
        
        timestamp = self._get_timestamp()
        
        if self.compression == "zip":
            backup_path = self.backup_dir / f"{name}_{timestamp}.zip"
            self._create_zip_backup(source, backup_path)
        elif self.compression == "tar":
            backup_path = self.backup_dir / f"{name}_{timestamp}.tar"
            self._create_tar_backup(source, backup_path)
        elif self.compression == "tar.gz":
            backup_path = self.backup_dir / f"{name}_{timestamp}.tar.gz"
            self._create_tar_backup(source, backup_path, "gz")
        else:
            # No compression - direct copy
            backup_path = self.backup_dir / f"{name}_{timestamp}"
            if source.is_file():
                shutil.copy2(source, backup_path)
            else:
                shutil.copytree(source, backup_path)

        size = format_bytes(backup_path.stat().st_size)
        logger.info(f"Backup created: {backup_path.name} ({size})")
        
        self._cleanup_old_backups(name)
        return backup_path

    def _cleanup_old_backups(self, name: str) -> None:
        """Remove old backup versions.
        
        Args:
            name: Backup name prefix
        """
        pattern = f"{name}_*"
        backups = sorted(
            self.backup_dir.glob(pattern),
            key=lambda p: p.stat().st_mtime,
            reverse=True
        )
        
        for old_backup in backups[self.keep_versions:]:
            old_backup.unlink()
            logger.info(f"Removed old backup: {old_backup.name}")

    def list_backups(self, name: Optional[str] = None) -> List[Dict]:
        """List available backups.
        
        Args:
            name: Filter by backup name
            
        Returns:
            List of backup info dicts
        """
        pattern = f"{name}_*" if name else "*"
        backups = []
        
        for backup_path in sorted(self.backup_dir.glob(pattern)):
            stat = backup_path.stat()
            backups.append({
                "name": backup_path.name,
                "path": str(backup_path),
                "size": format_bytes(stat.st_size),
                "created": datetime.fromtimestamp(stat.st_mtime).isoformat(),
            })
        
        return backups

    def restore_backup(
        self,
        backup_path: Path,
        destination: Path
    ) -> bool:
        """Restore backup to destination.
        
        Args:
            backup_path: Backup file path
            destination: Restore destination
            
        Returns:
            True if successful
        """
        backup_path = Path(backup_path)
        destination = Path(destination)
        
        if not backup_path.exists():
            logger.error(f"Backup not found: {backup_path}")
            return False

        try:
            if backup_path.suffix == ".zip":
                with zipfile.ZipFile(backup_path, "r") as zipf:
                    zipf.extractall(destination)
            elif ".tar" in backup_path.suffixes:
                with tarfile.open(backup_path, "r:*") as tar:
                    tar.extractall(destination)
            else:
                if backup_path.is_file():
                    shutil.copy2(backup_path, destination)
                else:
                    shutil.copytree(backup_path, destination)
            
            logger.info(f"Restored backup to {destination}")
            return True
        except Exception as e:
            logger.error(f"Failed to restore backup: {e}")
            return False


def main() -> None:
    """CLI for backup manager."""
    parser = argparse.ArgumentParser(description="Backup management utility")
    subparsers = parser.add_subparsers(dest="command", required=True)
    
    # Create backup
    create_parser = subparsers.add_parser("create", help="Create backup")
    create_parser.add_argument("source", help="Source path")
    create_parser.add_argument("--name", help="Custom backup name")
    create_parser.add_argument(
        "--compression",
        choices=["zip", "tar", "tar.gz", "none"],
        default=Config.BACKUP_COMPRESSION
    )
    
    # List backups
    list_parser = subparsers.add_parser("list", help="List backups")
    list_parser.add_argument("--name", help="Filter by name")
    
    # Restore backup
    restore_parser = subparsers.add_parser("restore", help="Restore backup")
    restore_parser.add_argument("backup", help="Backup file path")
    restore_parser.add_argument("destination", help="Restore destination")
    
    args = parser.parse_args()
    manager = BackupManager()
    
    if args.command == "create":
        manager.compression = args.compression
        manager.create_backup(Path(args.source), args.name)
    elif args.command == "list":
        backups = manager.list_backups(args.name)
        for backup in backups:
            print(f"{backup['name']} - {backup['size']} - {backup['created']}")
    elif args.command == "restore":
        manager.restore_backup(Path(args.backup), Path(args.destination))


if __name__ == "__main__":
    main()