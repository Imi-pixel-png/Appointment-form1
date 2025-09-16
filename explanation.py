# Import Flask essentials
from flask import Flask, render_template, request   # Flask app, HTML templates, and form data
from flask_mail import Mail, Message                # Flask-Mail extension for sending emails

# Initialize the Flask app
app = Flask(__name__)

# --- Flask-Mail configuration ---
# These settings tell Flask how to connect to Gmail’s SMTP server
app.config['MAIL_SERVER'] = 'smtp.gmail.com'        # Gmail SMTP server
app.config['MAIL_PORT'] = 587                       # Port for TLS (encrypted email)
app.config['MAIL_USE_TLS'] = True                   # Enable TLS encryption
app.config['MAIL_USERNAME'] = 'molouwaolapegba@gmail.com'  # Your Gmail address
app.config['MAIL_PASSWORD'] = 'ezhg iggt ffbp bjkl'        # 16-digit Gmail App Password (not normal password)

# Initialize Flask-Mail with the app
mail = Mail(app)

# --- Routes (URLs the user can visit) ---

# Home route (renders the form page)
@app.route('/')                                    # Main URL (http://127.0.0.1:5000/)
@app.route('/home')                                # Alternative URL (/home)
def home():
    return render_template('form.html')            # Load the HTML form from templates/form.html

# Route that handles the form submission and sends email
@app.route('/send_email', methods=['POST'])        # This route only accepts POST requests (form submits here)
def send_email():
    # --- Get data from the form (matches input "name" attributes in HTML) ---
    from_email = request.form['from_email']        # User’s email entered in the form
    to_email = request.form['to_email']            # Recipient’s email entered in the form
    reason = request.form['reason']                # Reason for appointment
    full_name = request.form['full_name']          # Full name entered in the form

    # --- Create the email message ---
    msg = Message(
        subject=f"Appointment Request from {full_name}",   # Email subject line
        sender=app.conf
