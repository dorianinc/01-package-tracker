from flask import Flask, render_template, url_for, redirect
from .config import Config
from .forms.shipping_form import ShippingForm
from .models import db, Package
from flask_migrate import Migrate


app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
migrate= Migrate(app, db)

@app.route("/")
def index():
    return "<h1>Package Tracker</h1>"

@app.route("/new_package", methods = ['GET', 'POST'])
def new_package():
    form = ShippingForm()

    if form.validate_on_submit():
        data = form.data
        new_package = Package(sender=data["sender"],
                              recipient=data["recipient"],
                              origin=data["origin"],
                              destination=data["destination"],
                              location=data["origin"])
        print(dir(form.data))
        db.session.add(new_package)
        db.session.commit()
        # print(f"new_package 👉 {new_package}")
        return redirect("/")
    return render_template('shipping_request.html', form=form)
