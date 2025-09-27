from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route("/")

def home():
    now = datetime.now()
    current_year = now.year
    current_month = now.strftime("%B")  # "September"
    return render_template("index.html", year=current_year, month=current_month)
