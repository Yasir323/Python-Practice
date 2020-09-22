from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pathlib import Path
from string import Template
import smtplib

template = Template(Path("mail/template.html").read_text())

message = MIMEMultipart()
message["From"] = "Yasir Jafri"
message["To"] = "yasir.jafri007@gmail.com"
message["Subject"] = "This is a test."
# We don't have a header called body, so, we need to attach it
# message.attach(MIMEText("Body"))
# For sending template use the following 2 lines
body = template.substitute(name="John")
message.attach(MIMEText("Body", "html"))
# Now we need to send this using SMTP server.
message.attach(MIMEImage(Path("mail/mosh.png").read_bytes()))
with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo() # This is a hello messgae, this is a part of SMTP protocol.
    # so, the communication b/w a client and smtp server should
    # start with a hello message.
    smtp.starttls() # TLS = Transport Layer Security
    # With this, all the commands we send to SMTP server will be encrypted.
    smtp.login("yasir.jafri007@gmail.com", "*#*#4636#*#*")
    smtp.send_message(message)
    print("Sent successfully.")
