from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]="postgresql://postgres:603Concord@localhost/height"
db = SQLAlchemy(app)

class Data(db.Model):
    __tablename__="data"
    id=db.Column(db.Integer, primary_key=True)
    email =db.Column(db.String(120), unique=True)
    height= db.Column(db.Integer)

    def __init__(self, email, height):
        self.email= email
        self.height= height


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/success", methods=["POST"])
def success():
    if request.method == "POST":
        email = request.form["email-name"]
        height = request.form["height"]
        print("email: "+email +"\n"+"Height: "+height)
        return render_template("success.html")

if __name__ == "__main__":
    app.debug = True
    app.run()