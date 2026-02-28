import smtplib
from email.mime.text import MIMEText
import os

def send_email(to_email: str, subject: str, body: str):
    msg = MIMEText(body, "html")
    msg["Subject"] = subject
    msg["From"] = os.getenv("EMAIL_FROM")
    msg["To"] = to_email

    with smtplib.SMTP(os.getenv("SMTP_HOST"), 587) as server:
        server.starttls()
        server.login(os.getenv("SMTP_USER"), os.getenv("SMTP_PASS"))
        server.sendmail(msg["From"], to_email, msg.as_string())
