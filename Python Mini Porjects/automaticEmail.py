import pandas as pd
import smtplib 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from_adrs = "ENETER_SENDERS_MAILID"

data = pd.read_csv("abc.csv")
to_addr = data['email'].tolist()
name = data['name'].tolist()

l=len(name)
email = ""
password = ""

for i in range(l):
    msg = MIMEMultipart()
    msg['From'] = from_adrs
    msg['To'] = to_addr
    msg['Subject'] = 'Just to Check'

    body=name[i]+'Enter your content here'

    msg.attach(MIMEText(body, 'plain'))

    mail = smtplib.SMTP('smpt.gmail.com', 587)
    mail.ehlo()
    mail.starttls()
    mail.login(email, password)
    text= msg.as_string()
    mail.sendmail(from_adrs, to_addr[i], text)
    mail.quit()

    