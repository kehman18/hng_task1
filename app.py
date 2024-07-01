from flask import Flask, request, jsonify
import requests

app = Flask(__name__)
DEFAULT_LOCATION = "Osun"
@app.route('/api/hello', methods=['GET'])
def hello():
    visitor_name = request.args.get('visitor_name', 'Guest')
    
    # Use a weather API to get the temperature for the specified location
    weather_api_key = '2d698e63c1207b0f5754b01bbd8c31ca'  # Replace this with your actual API key
    weather_response = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={DEFAULT_LOCATION}&appid={weather_api_key}&units=metric')
    weather_data = weather_response.json()

    if weather_response.status_code == 200 and 'main' in weather_data:
        temperature = weather_data['main']['temp']
    else:
        temperature = 'N/A'

    response = {
        "location": DEFAULT_LOCATION,
        "greeting": f"Hello, {visitor_name}!, the temperature is {temperature} degrees Celsius in {DEFAULT_LOCATION}"
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
