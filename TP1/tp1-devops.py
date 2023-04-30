#!/usr/bin/env python
# coding: utf-8

""""
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

"""

import os
import requests
from fastapi import FastAPI

app = FastAPI()

@app.get("/weather")
async def get_weather(latitude: float, longitude: float):
    api_key = "cdc59befcba406871a36b7f0f2a88f1b"
    url = f'https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        description = data['weather'][0]['description']
        temperature = data['main']['temp'] - 273.15
        return {"weather": f"The weather at the longitude and latitude given is {description} with a {temperature:.2f} degrés Celsius."}
    else:
        return {"error": f"Une erreur s'est produite lors de la récupération des données météorologiques. Code d'erreur : {response.status_code}"}


