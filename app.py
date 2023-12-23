from flask import Flask, render_template, request, redirect
from account import account_bp
from capstone import capstone_bp

app = Flask(__name__)

app.register_blueprint(account_bp)
app.register_blueprint(capstone_bp)

if __name__ == "__main__":
    app.run(debug=True)
