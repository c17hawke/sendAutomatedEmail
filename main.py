import os
from sendDetailedEmail.email import MailAttachment

def sendMail(clientEmail):
    try:
        sender = MailAttachment(clientEmail=clientEmail)
        sender.send()

    except Exception as e:
        raise e

if __name__=="__main__":
    clientEmail = input("input a valid client email ID: ")
    sendMail(clientEmail)
