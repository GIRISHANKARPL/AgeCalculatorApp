from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    age = None
    if request.method == "POST":
        birth_date = request.form.get("birthdate")
        if birth_date:
            birth_year = int(birth_date.split("-")[0])
            current_year = datetime.now().year
            age = current_year - birth_year
    return render_template("index.html", age=age)

if __name__ == "__main__":
    app.run(debug=True)
