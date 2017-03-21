import smtplib
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate

def send_mail(send_from, send_to, subject, text, files=None, server="127.0.0.1", smtp_user="", smtp_pwd="", server_port=587):
	#assert isinstance(send_to, list)

	msg = MIMEMultipart()
	msg['From'] = send_from
	msg['To'] = COMMASPACE.join(send_to)
	msg['Date'] = formatdate(localtime=True)
	msg['Subject'] = subject

	msg.attach(MIMEText(text))

	for f in files or []:
		with open(f, "rb") as fil:
			part = MIMEApplication(
				fil.read(),
				Name=basename(f)
			)
			part['Content-Disposition'] = 'attachment; filename="%s"' % basename(f)
			msg.attach(part)

	# Connection
	smtp = smtplib.SMTP(server, 587)
	smtp.starttls()
	smtp.ehlo()
	smtp.login(smtp_user, smtp_pwd)

	#Send
	smtp.sendmail(send_from, send_to, msg.as_string())
	smtp.close()