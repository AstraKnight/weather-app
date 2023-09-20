# THE FLASK FILE
# *******************************************************
from flask import Flask, render_template, request
from weather import get_current_weather
from waitress import serve


# Making the app a flask app:
app = Flask(__name__)


# Defining a route for the web (home page)
@app.route('/')
@app.route('/index')

def index():
    return render_template('index.html')

@app.route('/weather')
def get_weather():
    city = request.args.get('city')

    # check for empty strings or strings with only spaces or numbers:
    if (not bool(city.strip())) or (city.isdigit()):
        city = "New York"  # default value

    # get weather data from the API
    weather_data = get_current_weather(city)

    # city is not found by API
    if not weather_data['cod'] == 200:
        return render_template("city-not-found.html")

    return render_template(
    "weather.html",
    title=weather_data["name"],
    status=weather_data["weather"][0]["description"].capitalize(),
    temperature=f"{weather_data['main']['temp']:.1f}",
    feels_like=f"{weather_data['main']['feels_like']:.1f}"
    )


# Starting the server (go to localhost:8000 to see the page)
if __name__ == "__main__":
    #app.run(host="0.0.0.0", port=8000)
    serve(app, host="0.0.0.0", port=8000)


