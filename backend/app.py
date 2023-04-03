from flask import Flask, request, jsonify, render_template
from flask_mail import Mail, Message

app = Flask(__name__, template_folder='../templates', static_folder='../static')

app.config.update(
	MAIL_SERVER='smtp.gmail.com',
	MAIL_PORT=587,
	MAIL_USE_TLS=True,
	MAIL_USE_SSL=False,
	MAIL_USERNAME='corentin.dupaigne.main.sender',
	MAIL_PASSWORD="""avtmdmudzcxttyji""",
)

mail = Mail(app)

from flask import jsonify


@app.route('/', methods=['GET', 'POST'])
def index():
	message_status = None
	if request.method == 'POST':
		name = request.form['name']
		email = request.form['email']
		message = request.form['message']

		msg = Message(
			subject="Contact Form Submission",
			body=f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}",
			sender=app.config['MAIL_USERNAME'],
			recipients=['xetriboippobu-8742@yopmail.com'],
		)

		html_template = f'''
		<!DOCTYPE html>
		<html>
		<head>
		</head>
		<body style="font-family: Arial, sans-serif; font-size: 16px; line-height: 1.5; color: #333;">
		  <div style="max-width: 600px; margin: 0 auto; padding: 20px; border: 1px solid #e2e2e2; background-color: #ffffff;">
		    <div style="font-size: 24px; font-weight: bold; color: #4a4a4a; margin-bottom: 20px;">
		      Your message has been received
		    </div>
		    <div style="margin-bottom: 30px;">
		      Hi {name},
		      <br><br>
		      Thank you for contacting us. We've received your message and will get back to you shortly.
		      <br><br>
		      Best regards,
		    </div>
		    <div style="font-weight: bold; color: #4a4a4a;">
		      Your Company Name
		    </div>
		  </div>
		</body>
		</html>
		'''

		confirmation_msg = Message(
			subject="Contact Form Submission Received",
			html=html_template,
			sender=app.config['MAIL_USERNAME'],
			recipients=[email],
		)

	try:
		mail.send(msg)
		mail.send(confirmation_msg)
		message_status = 'success'
	except:
		message_status = 'failure'

	return render_template('index.html', message_status=message_status)


if __name__ == '__main__':
	app.run(debug=True)
