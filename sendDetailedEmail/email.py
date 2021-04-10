import smtplib
import os
from email.message import EmailMessage
from getCredentials.read import ConfigReader

CURRENT_FOLDER = "sendDetailedEmail"

HTML_TEMPLATE_NAME = "Template_corona_info.html"
HTML_TEMPLATE_PATH = os.path.join(CURRENT_FOLDER, HTML_TEMPLATE_NAME)

AUTH_DATA = ConfigReader()
eMAIL = AUTH_DATA.read_config()['eMAILsender']
ePASSKEY = AUTH_DATA.read_config()["ePASSKEY"]

class MailAttachment:

    def __init__(self, clientEmail=None):
        self.clientEmail = clientEmail

    def send(self):
        msg = EmailMessage()
        msg["Subject"] = "Detailed information about Covid-19"
        msg["From"] = eMAIL
        msg["To"] = self.clientEmail
        
        msg.set_content("Hi,\n\tPlease find the attachment below. \nRegards,\nSunny")

        with open(HTML_TEMPLATE_PATH, "r") as f:
            html_content = f.read()

        msg.add_alternative(html_content, subtype="html")

        pdf_files = ["FAQ1.pdf"]
        for file_ in pdf_files:
            path = os.path.join(CURRENT_FOLDER, file_)
            with open(path, "rb") as f:
                file_data = f.read()
                file_name = file_

            msg.add_attachment(file_data, maintype="application", 
            subtype="octet-stream", filename=file_name)

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(eMAIL, ePASSKEY)
            print("log in successfull!! \nsending email")
            smtp.send_message(msg)
            print("email Sent")