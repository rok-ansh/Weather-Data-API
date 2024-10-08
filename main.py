from flask import Flask, render_template
import pandas as pd

app = Flask("Website")

# Extract the station name and station ID and send the data in table format to html page
stations = pd.read_csv("data_small/stations.txt", skiprows=17)
stations = stations[["STAID","STANAME                                 "]]


@app.route("/")


def home():
    return render_template("home.html", data=stations.to_html())


@app.route("/api/v1/<station>/<date>")
def about(station, date):
    # Extracting the file
    filename = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    # Extracting the temperature value for a specific date
    temperature = df.loc[df["    DATE"] == date]["   TG"].squeeze()/10

    value = {"station": station,
             "date": date,
             "temperature": temperature}
    return value


if __name__ == "__main__":
    app.run(debug=True)
