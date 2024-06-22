import requests

def nepali_date(request):
    try:
        # Make a GET request to the external API
        response = requests.get('https://nepali-datetime.amitgaru.me/date')
        
        # Check if the request was successful
        if response.status_code == 200:
            data = response.json()
            # Extract the date from the API response
            current_date = data.get('data')
            return {'nepali_date': current_date}
        else:
            return {'nepali_date': 'Error fetching date'}
    except requests.exceptions.RequestException as e:
        return {'nepali_date': f'Error: {str(e)}'}
