import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email = "HasturDev@gmail.com"
receiver_email = "HasturDev@gmail.com"
password = input("Type your password and press enter:")

message = MIMEMultipart("alternative")
message["Subject"] = "multipart test"
message["From"] = sender_email
message["To"] = receiver_email

# Create the plain-text and HTML version of your message
text = """\
Hi,
Thank you for adding yourself to the Email List
I will attempt to update the email list and bring more to it like better HTML"""
html = """\
<html>
  <body>
    <p>Hi,<br>
       Thank you for subscribing to the email list<br>
       <a href="https://realpython.com/python-send-email/">The base tutorial that I used is here</a> 
       Learning more constantly that will allow me to better myself and my code.
    </p>
  </body>
</html>
"""

# Turn these into plain/html MIMEText objects
part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")

# Add HTML/plain-text parts to MIMEMultipart message
# The email client will try to render the last part first
message.attach(part1)
message.attach(part2)

# Create secure connection with server and send email
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(
        sender_email, receiver_email, message.as_string()
    )