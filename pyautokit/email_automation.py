"""Email automation with template support."""

import argparse
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from pathlib import Path
from typing import List, Optional, Dict
from string import Template
from .logger import setup_logger
from .config import Config
from .utils import load_json

logger = setup_logger("EmailAutomation", level=Config.LOG_LEVEL)


class EmailClient:
    """Email automation client with SMTP."""

    def __init__(
        self,
        smtp_server: str = Config.EMAIL_SMTP_SERVER,
        smtp_port: int = Config.EMAIL_SMTP_PORT,
        sender: str = Config.EMAIL_SENDER,
        password: str = Config.EMAIL_PASSWORD,
        use_tls: bool = Config.EMAIL_USE_TLS
    ):
        """Initialize email client.
        
        Args:
            smtp_server: SMTP server address
            smtp_port: SMTP port
            sender: Sender email address
            password: Email password or app password
            use_tls: Use TLS encryption
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.sender = sender
        self.password = password
        self.use_tls = use_tls

    def _create_message(
        self,
        to: str,
        subject: str,
        body: str,
        html: bool = False,
        attachments: Optional[List[Path]] = None
    ) -> MIMEMultipart:
        """Create email message.
        
        Args:
            to: Recipient email
            subject: Email subject
            body: Email body
            html: Body is HTML
            attachments: List of file paths to attach
            
        Returns:
            MIMEMultipart message object
        """
        msg = MIMEMultipart()
        msg["From"] = self.sender
        msg["To"] = to
        msg["Subject"] = subject

        msg.attach(MIMEText(body, "html" if html else "plain"))

        if attachments:
            for file_path in attachments:
                if not file_path.exists():
                    logger.warning(f"Attachment not found: {file_path}")
                    continue
                
                with open(file_path, "rb") as f:
                    part = MIMEBase("application", "octet-stream")
                    part.set_payload(f.read())
                
                encoders.encode_base64(part)
                part.add_header(
                    "Content-Disposition",
                    f"attachment; filename={file_path.name}"
                )
                msg.attach(part)
        
        return msg

    def send_email(
        self,
        to: str,
        subject: str,
        body: str,
        html: bool = False,
        attachments: Optional[List[Path]] = None
    ) -> bool:
        """Send single email.
        
        Args:
            to: Recipient email
            subject: Email subject
            body: Email body
            html: Body is HTML
            attachments: List of attachments
            
        Returns:
            True if sent successfully
        """
        try:
            msg = self._create_message(to, subject, body, html, attachments)
            
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                if self.use_tls:
                    server.starttls()
                server.login(self.sender, self.password)
                server.send_message(msg)
            
            logger.info(f"Email sent to {to}")
            return True
        except Exception as e:
            logger.error(f"Failed to send email to {to}: {e}")
            return False

    def send_bulk_emails(
        self,
        recipients: List[str],
        subject: str,
        body: str,
        html: bool = False
    ) -> Dict[str, int]:
        """Send bulk emails.
        
        Args:
            recipients: List of recipient emails
            subject: Email subject
            body: Email body
            html: Body is HTML
            
        Returns:
            Dict with success/failure counts
        """
        results = {"success": 0, "failed": 0}
        
        for recipient in recipients:
            if self.send_email(recipient, subject, body, html):
                results["success"] += 1
            else:
                results["failed"] += 1
        
        logger.info(f"Bulk email complete: {results}")
        return results

    def send_templated_emails(
        self,
        recipients_data: List[Dict[str, str]],
        subject_template: str,
        body_template: str,
        html: bool = False
    ) -> Dict[str, int]:
        """Send templated emails with personalization.
        
        Args:
            recipients_data: List of dicts with 'email' and template variables
            subject_template: Subject template with $variable placeholders
            body_template: Body template with $variable placeholders
            html: Body is HTML
            
        Returns:
            Dict with success/failure counts
        """
        results = {"success": 0, "failed": 0}
        
        subject_tmpl = Template(subject_template)
        body_tmpl = Template(body_template)
        
        for data in recipients_data:
            email = data.get("email")
            if not email:
                logger.warning("Recipient data missing email field")
                results["failed"] += 1
                continue
            
            try:
                subject = subject_tmpl.safe_substitute(data)
                body = body_tmpl.safe_substitute(data)
                
                if self.send_email(email, subject, body, html):
                    results["success"] += 1
                else:
                    results["failed"] += 1
            except Exception as e:
                logger.error(f"Template error for {email}: {e}")
                results["failed"] += 1
        
        return results


def main() -> None:
    """CLI for email automation."""
    parser = argparse.ArgumentParser(description="Email automation utility")
    parser.add_argument("--to", required=True, help="Recipient email")
    parser.add_argument("--subject", required=True, help="Email subject")
    parser.add_argument("--body", required=True, help="Email body or file path")
    parser.add_argument("--html", action="store_true", help="Body is HTML")
    parser.add_argument(
        "--attach",
        action="append",
        help="Attachment file path"
    )
    
    args = parser.parse_args()
    
    # Load body from file if it's a path
    body = args.body
    body_path = Path(args.body)
    if body_path.exists():
        body = body_path.read_text()
    
    attachments = [Path(a) for a in args.attach] if args.attach else None
    
    client = EmailClient()
    client.send_email(
        to=args.to,
        subject=args.subject,
        body=body,
        html=args.html,
        attachments=attachments
    )


if __name__ == "__main__":
    main()