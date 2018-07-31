import smtplib
from email.mime.text import MIMEText
import csv

smtp_ssl_host = 'smtp.gmail.com'  # smtp.mail.yahoo.com
smtp_ssl_port = 465
username = 'linuxautobot@gmail.com'
password = '1235@69'
sender = 'www.google.com'
#targets = ['abc@gmail.com']



html = """\
<html>
  <head></head>
  <body>
    <p>Hello,<br>
    	1<br>
      2<br>
      3<br>
Waiting for your Optimistic reply.<br><br>

--<br><br>

Thanks & Regards,<br>
linuxautobot<br>
<h3>GNU Pvt Ltd</h3>
<img src="https://s3.ap-south-1.amazonaws.com/sign.png">

    </p>
  </body>
</html>
"""


with open('b.csv') as csvfile:
    readCSV = csv.reader(csvfile)
    for row in readCSV:
            AppNAame = row[1:2]
            targets =  row[6:7]
            str1 = ''.join(AppNAame)
            print str1
            msg = MIMEText(html,'html')
            msg['Subject'] = 'App Online - '+ str1
            print msg ['Subject']
            msg['From'] = sender
            msg['To'] = ', '.join(targets)
            server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
            server.login(username, password)
            server.sendmail(sender, targets, msg.as_string())
            server.quit()



