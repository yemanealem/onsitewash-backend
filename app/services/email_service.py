import smtplib
from email.mime.text import MIMEText
from jinja2 import Environment, FileSystemLoader
import os

TEMPLATE_DIR = "app/templates"

def send_email(to_email: str, subject: str, template_name: str, context: dict):

    env = Environment(loader=FileSystemLoader(TEMPLATE_DIR))
    template = env.get_template(template_name)

    html_content = template.render(context)

    msg = MIMEText(html_content, "html")
    msg["Subject"] = subject
    msg["From"] = os.getenv("EMAIL_FROM")
    msg["To"] = to_email

    with smtplib.SMTP(os.getenv("SMTP_HOST"), 587) as server:
        server.starttls()
        server.login(os.getenv("SMTP_USER"), os.getenv("SMTP_PASS"))
        server.sendmail(msg["From"], to_email, msg.as_string())
