import smtplib
from email.mime.text import MIMEText
from jinja2 import Environment, FileSystemLoader
import os

TEMPLATE_DIR = "app/templates"

def send_email(customer_email: str, subject: str, template_name: str, context: dict):

    env = Environment(loader=FileSystemLoader(TEMPLATE_DIR))
    template = env.get_template(template_name)

    html_content = template.render(context)

    msg = MIMEText(html_content, "html")
    msg["Subject"] = subject

    owner_email = os.getenv("EMAIL_FROM") 
    msg["From"] = owner_email

    recipient = os.getenv("EMAIL_TO")      
    msg["To"] = recipient

    smtp_host = os.getenv("SMTP_HOST")
    smtp_user = os.getenv("SMTP_USER")
    smtp_pass = os.getenv("SMTP_PASS")

    with smtplib.SMTP(smtp_host, 587) as server:
        server.starttls()
        server.login(smtp_user, smtp_pass)

        # send to owner inbox
        server.sendmail(owner_email, recipient, msg.as_string())
