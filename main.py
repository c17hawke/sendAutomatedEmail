import os
from sendDetailedEmail.email import MailAttachment

def sendMail(clientEmail):
    try:
        sender = MailAttachment(clientEmail=clientEmail)
        sender.send()

    except Exception as e:
        raise e

if __name__=="__main__":
    # clientEmail = "chatbot.c17hawke@gmail.com"
    clientEmails = ["chetanhebbur@gmail.com", "rishavghosh321@gmail.com", "vinothgt007@gmail.com"] 
    for email_ in clientEmails:
        print(f"sending email to {email_}")
        sendMail(email_)