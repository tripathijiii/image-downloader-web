import smtplib,ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import shutil
import os

def sendmail(reciever_email,file_name):
    smtp_server = "smtp.gmail.com"
    port = 587
    sender_email="shashwatesht.development@gmail.com"
    password = "9002748769"
    msg = MIMEMultipart()
    msg['from'] = sender_email
    msg['to'] = reciever_email
    msg['Subject'] = "Image Downloader"
    body = """ Thank you for choosing us your images has been downloaded and attached here with
        
            and yes it works  """
    msg.attach(MIMEText(body,'plain'))
    shutil.make_archive("downloadedimages_archive","zip",file_name)
    filename = "downloadedimages_archive.zip"
    attachment = open(filename,"rb")
    p=MIMEBase('application','octet-stream')
    p.set_payload((attachment).read())
    encoders.encode_base64(p)
    p.add_header('Content-Disposition',"atachment; filename = %s"% filename)
    msg.attach(p)

    server=smtplib.SMTP(smtp_server,port)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(sender_email,password)
    
    server.sendmail(sender_email,reciever_email,msg.as_string())
    server.quit()
    attachment.close()
    shutil.rmtree(file_name)
    os.remove(filename)
