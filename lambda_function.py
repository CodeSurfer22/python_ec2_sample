import os
import json
import requests

def lambda_handler(event, context):
    # Get the city name from the event (default to Bangkok if not provided)
    city_name = event.get('city_name', 'Bangkok')

    # Get the API key from environment variables
    api_key = os.environ.get('API_KEY')
    if not api_key:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': 'API_KEY environment variable not set'})
        }

    # Construct the API URL
    base_url = "https://api.openweathermap.org/data/2.5/weather?q="
    full_url = f"{base_url}{city_name}&appid={api_key}"

    # Make the API request
    response = requests.get(full_url)
    if response.status_code != 200:
        return {
            'statusCode': response.status_code,
            'body': json.dumps({'error': 'Failed to fetch weather data'})
        }

    # Return the response data
    return {
        'statusCode': 200,
        'body': response.json()
    }
