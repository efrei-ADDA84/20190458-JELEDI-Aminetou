#!/usr/bin/env python
# coding: utf-8

'''''
import os
import requests


def get_weather(latitude, longitude):
    api_key = "cdc59befcba406871a36b7f0f2a88f1b"
    url = f'https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        description = data['weather'][0]['description']
        temperature = data['main']['temp'] - 273.15
        return f"The weather at the longitude and latitude given is {description} with a {temperature:.2f} degrés Celsius."
    else:
        return f"Une erreur s'est produite lors de la récupération des données météorologiques. Code d'erreur : {response.status_code}"


print(get_weather(48.8566, 2.3522))
'''
from flask import Flask, request
import os
import requests

app = Flask(__name__)
api_key = os.environ.get("API_KEY")

@app.route('/weather', methods=["GET"])
def get_weather():
    latitude = request.args.get('lat')
    longitude = request.args.get('lon')
    print(latitude)
    print(longitude)

    url = 'https://api.openweathermap.org/data/2.5/weather?lat=' + latitude + '&lon=' +longitude+ '&appid='+api_key
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8081)
    print(app)
    


