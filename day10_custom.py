from smtplib import SMTP, SMTPAuthenticationError, SMTPException
from smtplib import SMTP
import smtplib

host = "smtp.gmail.com"
port = 587
username = #email
password = #password
from_email = username
to_list = ["karakurttaylan46@gmail.com"]
email_conn = smtplib.SMTP(host, port)
email_conn.ehlo()
email_conn.starttls()
'''Google doesn't allow to login normal ways.
So Try this solution
--Hi, it's googles fault
log in to your test gmail account,
then go to https://accounts.google.com/DisplayUnlockCaptcha
and disable protection + disable this
https://www.google.com/settings/security/lesssecureapps -
this will make it less secure so use test account
'''
email_conn.login(username, password)
# Don't use Turkish letters. smtplib doesn't allow it
email_conn.sendmail(from_email, to_list, "Python ile mail gonderme")
email_conn.quit()
#With wrong password imported Error Exception would give us error message
pass_wrong = SMTP(host, port)
pass_wrong.ehlo()
pass_wrong.starttls()
try:
    pass_wrong.login(username, "wrongy")
    pass_wrong.sendmail(from_email, to_list, "Python ile mail gonderme")
except SMTPAuthenticationError:
    print("Could not login")
except:
    print("an error occurred")
