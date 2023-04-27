from flask import Flask, render_template, url_for, redirect
from .config import Config
from .forms.shipping_form import ShippingForm

app = Flask(__name__)
app.config.from_object(Config)

@app.route("/")
def index():
    return "<h1>Package Tracker</h1>"

@app.route("/new_package", methods = ['GET', 'POST'])
def new_package():
    form = ShippingForm()
    
    if form.validate_on_submit():
        new_package = {
            "id": 0,
            "recipient": form.data["recipient"],
            "origin": form.data["origin"],
            "destination": form.data["destination"],
            "express": form.data["express"]
        }
        print(f"new_package 👉 {new_package}")
        return redirect("/")
    return render_template('shipping_request.html', form=form)
