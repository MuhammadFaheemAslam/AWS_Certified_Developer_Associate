from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    weather_data = None
    if request.method == "POST":
        city = request.form.get("city")
        if city:
            # WTTR.in API endpoint
            url = f"https://wttr.in/{city}?format=j1"
            response = requests.get(url)
            if response.status_code == 200:
                weather_data = response.json()
            else:
                weather_data = {"error": "City not found or API is unavailable"}
    return render_template("index.html", weather_data=weather_data)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
