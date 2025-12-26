"""Security utilities for encryption and hashing."""

import argparse
import hashlib
import secrets
from pathlib import Path
from typing import Optional
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64
from .logger import setup_logger
from .config import Config

logger = setup_logger("SecurityUtils", level=Config.LOG_LEVEL)


class SecurityUtils:
    """Security utilities for encryption and hashing."""

    @staticmethod
    def generate_key() -> bytes:
        """Generate Fernet encryption key.
        
        Returns:
            Encryption key bytes
        """
        return Fernet.generate_key()

    @staticmethod
    def generate_key_from_password(
        password: str,
        salt: Optional[bytes] = None
    ) -> tuple[bytes, bytes]:
        """Generate encryption key from password.
        
        Args:
            password: Password string
            salt: Optional salt bytes
            
        Returns:
            Tuple of (key, salt)
        """
        if salt is None:
            salt = secrets.token_bytes(16)
        
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
        )
        key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
        return key, salt

    @staticmethod
    def encrypt_text(
        text: str,
        key: bytes
    ) -> bytes:
        """Encrypt text with key.
        
        Args:
            text: Text to encrypt
            key: Encryption key
            
        Returns:
            Encrypted bytes
        """
        f = Fernet(key)
        return f.encrypt(text.encode())

    @staticmethod
    def decrypt_text(
        encrypted: bytes,
        key: bytes
    ) -> str:
        """Decrypt encrypted text.
        
        Args:
            encrypted: Encrypted bytes
            key: Decryption key
            
        Returns:
            Decrypted text
        """
        f = Fernet(key)
        return f.decrypt(encrypted).decode()

    @staticmethod
    def encrypt_file(
        file_path: Path,
        key: bytes,
        output_path: Optional[Path] = None
    ) -> Path:
        """Encrypt file.
        
        Args:
            file_path: File to encrypt
            key: Encryption key
            output_path: Output file path (default: file_path.enc)
            
        Returns:
            Path to encrypted file
        """
        if output_path is None:
            output_path = file_path.with_suffix(file_path.suffix + ".enc")
        
        with open(file_path, "rb") as f:
            data = f.read()
        
        f = Fernet(key)
        encrypted = f.encrypt(data)
        
        with open(output_path, "wb") as f:
            f.write(encrypted)
        
        logger.info(f"Encrypted {file_path} to {output_path}")
        return output_path

    @staticmethod
    def decrypt_file(
        encrypted_path: Path,
        key: bytes,
        output_path: Optional[Path] = None
    ) -> Path:
        """Decrypt file.
        
        Args:
            encrypted_path: Encrypted file path
            key: Decryption key
            output_path: Output file path
            
        Returns:
            Path to decrypted file
        """
        if output_path is None:
            output_path = encrypted_path.with_suffix("")
            if output_path.suffix == ".enc":
                output_path = output_path.with_suffix("")
        
        with open(encrypted_path, "rb") as f:
            encrypted = f.read()
        
        f = Fernet(key)
        data = f.decrypt(encrypted)
        
        with open(output_path, "wb") as f:
            f.write(data)
        
        logger.info(f"Decrypted {encrypted_path} to {output_path}")
        return output_path

    @staticmethod
    def hash_text(
        text: str,
        algorithm: str = "sha256"
    ) -> str:
        """Hash text with algorithm.
        
        Args:
            text: Text to hash
            algorithm: Hash algorithm (md5, sha1, sha256, sha512)
            
        Returns:
            Hex digest string
        """
        hash_func = hashlib.new(algorithm)
        hash_func.update(text.encode())
        return hash_func.hexdigest()

    @staticmethod
    def generate_token(
        length: int = 32
    ) -> str:
        """Generate random secure token.
        
        Args:
            length: Token length in bytes
            
        Returns:
            Hex token string
        """
        return secrets.token_hex(length)

    @staticmethod
    def generate_password(
        length: int = 16,
        include_symbols: bool = True
    ) -> str:
        """Generate random secure password.
        
        Args:
            length: Password length
            include_symbols: Include special symbols
            
        Returns:
            Random password
        """
        import string
        
        chars = string.ascii_letters + string.digits
        if include_symbols:
            chars += string.punctuation
        
        return "".join(secrets.choice(chars) for _ in range(length))


def main() -> None:
    """CLI for security utils."""
    parser = argparse.ArgumentParser(description="Security utilities")
    subparsers = parser.add_subparsers(dest="command", required=True)
    
    # Generate key
    gen_key = subparsers.add_parser("genkey", help="Generate encryption key")
    gen_key.add_argument("--output", "-o", help="Output key file")
    
    # Encrypt file
    encrypt = subparsers.add_parser("encrypt", help="Encrypt file")
    encrypt.add_argument("file", help="File to encrypt")
    encrypt.add_argument("--key", required=True, help="Key file")
    encrypt.add_argument("--output", "-o", help="Output file")
    
    # Decrypt file
    decrypt = subparsers.add_parser("decrypt", help="Decrypt file")
    decrypt.add_argument("file", help="File to decrypt")
    decrypt.add_argument("--key", required=True, help="Key file")
    decrypt.add_argument("--output", "-o", help="Output file")
    
    # Hash text
    hash_cmd = subparsers.add_parser("hash", help="Hash text")
    hash_cmd.add_argument("text", help="Text to hash")
    hash_cmd.add_argument(
        "--algorithm",
        default="sha256",
        choices=["md5", "sha1", "sha256", "sha512"]
    )
    
    # Generate password
    genpass = subparsers.add_parser("genpass", help="Generate password")
    genpass.add_argument("--length", type=int, default=16)
    genpass.add_argument("--no-symbols", action="store_true")
    
    args = parser.parse_args()
    utils = SecurityUtils()
    
    if args.command == "genkey":
        key = utils.generate_key()
        if args.output:
            Path(args.output).write_bytes(key)
            logger.info(f"Key saved to {args.output}")
        else:
            print(key.decode())
    
    elif args.command == "encrypt":
        key = Path(args.key).read_bytes()
        output = Path(args.output) if args.output else None
        utils.encrypt_file(Path(args.file), key, output)
    
    elif args.command == "decrypt":
        key = Path(args.key).read_bytes()
        output = Path(args.output) if args.output else None
        utils.decrypt_file(Path(args.file), key, output)
    
    elif args.command == "hash":
        result = utils.hash_text(args.text, args.algorithm)
        print(f"{args.algorithm.upper()}: {result}")
    
    elif args.command == "genpass":
        password = utils.generate_password(
            args.length,
            not args.no_symbols
        )
        print(password)


if __name__ == "__main__":
    main()