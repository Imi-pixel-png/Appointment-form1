from flask import Flask, render_template, request
from flask_mail import Mail, Message

app = Flask(__name__)

# Flask-Mail configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'molouwaolapegba@gmail.com'  
app.config['MAIL_PASSWORD'] = 'ezhg iggt ffbp bjkl'      

mail = Mail(app)

# Home route (form page)
@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')

# Handle form submission and send email
@app.route('/send_email', methods=['POST'])
def send_email():
    # Get data from form
    from_email = request.form['from_email']
    to_email = request.form['to_email']
    reason = request.form['reason']
    full_name = request.form['full_name']
    gender = request.form['gender']
    therapy_type = request.form['therapy_type']
    phone = request.form['phone']


    # Create the email
    msg = Message(
        subject=f"Appointment Request from {full_name}",
        sender=app.config['MAIL_USERNAME'], 
        recipients=[to_email]
    )

    # Add details to email body
    msg.body = f"""
    You have a new appointment request.

    Name: {full_name}
    Email: {from_email}
    Reason: {reason}
    Gender: {gender}
    Therapy Type: {therapy_type}
    Phone Number: {phone}
    """

    # Set reply-to so recipient can reply directly to the user's email
    msg.reply_to = from_email

    # Send email
    mail.send(msg)

    return render_template("sent.html")

if __name__ == "__main__":
    app.run(debug=True)
