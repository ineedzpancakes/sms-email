import datetime
import smtplib
from email.message import EmailMessage
import datetime

def time_in_range(start, end, x):
    if start <= end:
        return start <= x <= end
    else:
        return start <= x or x <= end

def email_alert(subject, body, to):
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = subject
    msg['to'] = to
    user = "something@gmail.com" # email goes here (you're going to have to allow access)
    msg['from'] = user
    password = "password" # password goes here
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user, password)
    server.send_message(msg)
    server.quit

if __name__ == '__main__':\
    # DISCLAIMER: I'm using an infinite loop to keep sending everyday. You can edit this to your liking.
    while True:
        # I'm using this as HOUR, MINUTE, SECOND, MICROSECOND;
        # don't ask me how to set a specific date, not even I know. 
        # Just look at the datetime documentaion.
        start = datetime.time(2,0,0,0)
        end = datetime.time(2,0,0,1000)
        if (time_in_range(start, end, datetime.datetime.now().time())): 
            email_alert("subject", "message", "email to")
            print("sent at: " + str(datetime.datetime.now()))
