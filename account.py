from flask import Blueprint, render_template, request, session
from database import get_database_connection
from datetime import datetime

account_bp = Blueprint('account', __name__)

@account_bp.route('/')
def index():
    return render_template('index.html')

@account_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        # Get username and password inputs
        username = request.form['username']
        password = request.form['password']

        # Connect to database
        connection = get_database_connection()
        cursor = connection.cursor()

        #SQL Query to check login credentials 
        query = "SELECT * FROM accounts WHERE username = %s AND password = %s"
        cursor.execute(query, (username, password))
        account = cursor.fetchone()

        # If account is found with username and password
        if account:
            # Check if account is approved
            if account[5] == 'Approved':
                # Save account_id in session storage
                session['account_id'] = account[0]
                session['account_type'] = account[4]
                
                if account[4] == 'Normal User':
                    return render_template('dashboard.html', account_type='Normal User')
                elif account[4] == 'Administrator':
                    return render_template('dashboard.html', account_type='Administrator')
            else:
                # If account is not approved, display error
                return render_template('login.html', error='Account not approved')
        else:
            # Else return back to login 
            return render_template('login.html', error='Invalid credentials')
    else:
        return render_template('login.html')
    
@account_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        # Get username and password inputs
        username = request.form['username']
        password = request.form['password']

        # Connect to database
        connection = get_database_connection()
        cursor = connection.cursor()

        # SQL Query to check login credentials and status
        query = "INSERT INTO accounts (username, password, creation_date, account_type, approval_status) VALUES (%s, %s, %s, 'Normal User', 'Pending')"
        # Get current datetime
        current_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        cursor.execute(query, (username, password, current_date))
        connection.commit()
        return render_template('register.html', message='Successful registration')
    else:
        return render_template('register.html')
    
    
