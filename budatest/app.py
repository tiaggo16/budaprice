from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import pandas as pd
import csv


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db = SQLAlchemy(app)


class ProductModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    brand = db.Column(db.String(100))


@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")


@app.route("/data", methods=["GET", "POST"])
def data():
    if request.method == "POST":
        f = request.form["csvfile"]
        data = []
        with open(f) as file:
            csvile = csv.reader(file)
            for row in csvile:
                data.append(row)
        data = pd.DataFrame(data)
        return render_template(
            "data.html", data=data.to_html(header=False, index=False)
        )


if __name__ == "__main__":
    app.run(debug=True)
