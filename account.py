from flask import Blueprint, render_template, request
from database import get_database_connection

account_bp = Blueprint('account', __name__)

@account_bp.route('/')
def index():
    return render_template('index.html');

@account_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        pass
    else:
        return render_template('register.html');

@account_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        # Get username and password inputs
        username = request.form['username']
        password = request.form['password']

        # Connect to database
        connection = get_database_connection()
        cursor = connection.cursor()

        #SQL Query to check login credentials and status
        query = "SELECT * FROM accounts WHERE username = %s AND password = %s AND approval_status = 'approved'"
        cursor.execute(query, (username, password))
        account = cursor.fetchone()

        if account:
            # If credentials and status are valid
            return "Success"
        else:
            # Else return back to login 
            return render_template('login.html', error='Invalid credentials')

    else:
        return render_template('login.html')