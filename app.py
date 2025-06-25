from flask import Flask , render_template , request , url_for
import requests

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def check_weather():
    weather_data = None

    if request.method == 'POST':
        city = request.form.get("city").strip()
        if city:

            api_key = "82ba7d523da211e52511fed7d573b5e9"
            url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

            response = requests.get(url)

            if response.status_code == 200:
                weather_data = response.json()
            else:
                weather_data = {"error":"City not found"}
    
    return render_template("base.html",weather_data=weather_data)
    


if __name__ == "__main__":
    app.run(debug=True)
