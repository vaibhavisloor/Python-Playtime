import smtplib

mail = "sender@gmail.com"
passw = "" #Get this from Google app passwords

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user = mail , password=passw)
connection.sendmail(from_addr=mail, to_addrs="receiver@gmail.com",msg="Subject:Trying SMTP\n\nSent from smtplib")
connection.close()