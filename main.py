from flask import Flask, render_template
import pandas as pd

app = Flask("Website")

# Extract the station name and station ID and send the data in table format to html page
stations = pd.read_csv("data_small/stations.txt", skiprows=17)
stations = stations[["STAID", "STANAME                                 "]]


@app.route("/")
def home():
    return render_template("home.html", data=stations.to_html())

# Show data for specific station and date
@app.route("/api/v1/<station>/<date>")
def about(station, date):
    # Extracting the file
    filename = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    # Extracting the temperature value for a specific date
    temperature = df.loc[df["    DATE"] == date]["   TG"].squeeze() / 10

    value = {"station": station, "date": date, "temperature": temperature}
    return value

# Show all data for a particular station
@app.route("/api/v1/<station>")
def all_data(station):
    filename = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    data = df.to_dict(orient="records")
    return data


# Show yearly data
@app.route("/api/yearly/v1/<station>/<year>")
def year(station, year):
    filename = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20)
    # Converting date from integer to str
    df["    DATE"] = df["    DATE"].astype(str)
    # It works only with str so need not to parse date here
    result = df[df["    DATE"].str.startswith(str(year))].to_dict(orient="records")
    return result

if __name__ == "__main__":
    app.run(debug=True)
