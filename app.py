from flask import Flask, render_template, request
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
    
    flavors = {
        "Vanilla":         "#F7E9CF",
        "Strawberry":      "#FF6B8A", 
        "Chocolate":       "#5C3D2E", 
        "Cookie Dough":   "#DCC7A1", 
        "Mint":            "#BFE8CF", 
        }
    
    toppings = {
        "Sprinkles":          "#FFBE0B"   , 
        "Cherry":             "#D90429"   , 
        "Chocolate syrup":    "#3E2723"  , 
        "Strawberry syrup":   "#E63946"  , 
        "Caramel":                 "#C77D36" , 
        "Chocolate Chip Cookies":  "#7B5E3B" , 
        "Whipped Cream":           "#FFFFFF" ,
        "None":                    "transparent",
        }                      
    
    
    cones = {
        "waffle cone":   "#C68642", 
        "wafer cone":    "#D6B484",
        }
    
    
    # flavor_choice = random.choice(flavors)
    # topping_choice = random.choice(toppings)
    # topping_choice2 = random.choice(toppings)
    # topping_choice3 = random.choice(toppings)
    # cone_choice = random.choice(cone)
    
    select_flavor = request.args.get("flavor") or random.choice(list(flavors.keys()))
    select_cone   = request.args.get("cone") or random.choice(list(cones.keys()))
    select_toppings = request.args.getlist("toppings") or random.sample(list(toppings.keys()), k=min (3, len(toppings)))

    view_toppings = [t for t in select_toppings if t != "None"]

    colors = {
        "scoop":   flavors.get(select_flavor, "#DDD"),
        "cone":    cones.get(select_cone, "#B5651D"),
        "toppings": [toppings.get(t, "transparent") for t in select_toppings],
          }

    if len(view_toppings) > 1:
        topping_text = ", ".join(view_toppings[:-1]) + f" and {view_toppings[-1]}"
    elif view_toppings:
        topping_text = view_toppings[0]
    else:
        topping_text = "no toppings"
    

    mix_text = f"{select_flavor} with {topping_text} on a {select_cone}"

    timeline = [
    "Ancient Persia: flavored snow desserts",
    "17th c. Italy: sorbetto popularized",
    "1843: hand-crank ice cream freezer patent",
    "1904: waffle cone at World’s Fair (popularized)",
    "1930s: soft-serve era begins",]


    return render_template("subject.html", colors=colors, select_flavor=select_flavor, select_cone=select_cone,select_toppings=select_toppings, flavors=flavors, toppings=toppings, cones=cones, icecream_mix=mix_text, timeline=timeline )


@app.route("/icecream/result")

def icecream_results():
    return "Final Ice Cream results"
