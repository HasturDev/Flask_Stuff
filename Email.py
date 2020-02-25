import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from forms import ContactForm


def Email_response(n):
    # required data for email
    sender_email = "hasturDev@gmail.com"
    receiver_email = n
    password = ""

    message = MIMEMultipart("alternative")
    message["Subject"] = "multipart test"
    message["From"] = sender_email
    message["To"] = receiver_email

    # Message for emails that only accept plain text
    text = """\
    Hi,
    Thank you for adding yourself to the Email List
    I will attempt to update the email list and bring more to it like better HTML"""

    # Message for Emails that accept html
    html = """\
    <html>
    <body>
    <p>Hi,<br>
    HUZZAH! I can't believe it.... This worked? THIS WORKED!<br>
    <a href="https://realpython.com/python-send-email/">The base tutorial that I used is here</a> <br>
    <a href="https://github.com/lecherouscthulhu">Mah Github</a> <br>
    <a href="https://www.linkedin.com/in/ian-mizer-039843155/"> Linkedin</a> <br>
    Something else will be here I'm sure..... Like buddy jesus <br>
    <img src="https://i.kym-cdn.com/entries/icons/mobile/000/003/384/christ.jpg"> <br>
    Good now that I have a basic grasp of this email stuff its time to throw it all away<br>
    then i can roll over to the real dream of not beleiving in technology and taking up my station as a flat earther<br>
    This will be a sad day, but take heart. I will either take them down from the inside<br>
    or fail miserably and become their greatest tech support<br>
    In the event of the second thing, I would like to thank you and our new mentally deficient earther overlords<br>
    This is the end of the automated message...... Goodbye
    </p>
    </body>
    </html>
    """

    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    message.attach(part1)
    message.attach(part2)

    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )