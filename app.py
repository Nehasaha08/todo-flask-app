from flask import Flask, render_template, request, redirect, url_for, flash
from formm import registration
app = Flask(__name__)
app.secret_key="my-secret-key"
@app.route("/", methods=["POST" ,"GET"])
def form():
    form=registration()
    if form.validate_on_submit():
             name=form.name.data
             email=form.email.data
             flash(f"{name} have sucesfully registered")
             return redirect(url_for("succes"))
    return render_template("form.html", form=form)
@app.route("/succes")
def succes():
    return render_template("succes.html")
app.run(debug=True)
