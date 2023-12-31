from flask import Flask, session, request, render_template
from account import account_bp
from capstone import capstone_bp

app = Flask(__name__)
app.secret_key = 'dop_assg'

app.register_blueprint(account_bp)
app.register_blueprint(capstone_bp)

if __name__ == "__main__":
    app.run(debug=True)
