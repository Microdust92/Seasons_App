from flask import Flask, render_template
from datetime import datetime
import random

app = Flask(__name__)

@app.route("/")

def home():
    now = datetime.now()
    current_year = now.year
    current_month = now.strftime("%B")  # "September"
    return render_template("index.html", year=current_year, month=current_month)



@app.route("/icecream")

def icecream():
    cone = ["waffle cone", "wafer cone"]
    flavors = ["Vanilla", "Strawberry", "Chocolate", "Cookies Dough", "Mint"]
    toppings = ["Sprinkles", "Cherry", "Chocolate syrup", "Strawberry syrup", "Caramel", "Chocolate Chip Cookies", "Whipped Cream"," "]

    flavor_choice = random.choice(flavors)
    topping_choice = random.choice(toppings)
    topping_choice2 = random.choice(toppings)
    topping_choice3 = random.choice(toppings)
    cone_choice = random.choice(cone)

    icecream_mix = f"{flavor_choice} Ice cream with {topping_choice} and {topping_choice2} and {topping_choice3} on a {cone_choice}"
    return render_template("subject.html", icecream_mix=icecream_mix)


@app.route("/icecream/result")

def icecream_results():
    return "Final Ice Cream results"
