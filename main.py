from flask import Flask, render_template

app = Flask("Website")


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/api/v1/<station>/<date>")
def about(station, date):
    temperature = 23
    value = {"station": station,
             "date": date,
             "temperature": temperature}
    return value


if __name__ == "__main__":
    app.run(debug=True)
