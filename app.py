from flask import Flask, request, jsonify, Response
import requests
import json
from collections import OrderedDict

app = Flask(__name__)
DEFAULT_LOCATION = "Osun"

@app.route('/api/hello', methods=['GET'])
def hello():
    visitor_name = request.args.get('visitor_name', 'Guest')
    ip_address = request.remote_addr

    weather_api_key = '2d698e63c1207b0f5754b01bbd8c31ca' 
    weather_response = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={DEFAULT_LOCATION}&appid={weather_api_key}&units=metric')
    weather_data = weather_response.json()

    if weather_response.status_code == 200 and 'main' in weather_data:
        temperature = weather_data['main']['temp']
    else:
        temperature = 'N/A'

    response = OrderedDict([
        ("client_ip", ip_address),
        ("location", DEFAULT_LOCATION),
        ("greeting", f'Hello, {visitor_name}!, the temperature is {temperature} degrees Celsius in {DEFAULT_LOCATION}')
    ])

    json_response = json.dumps(response)

    return Response(json_response, content_type='application/json')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
