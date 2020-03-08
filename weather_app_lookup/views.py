from django.shortcuts import render

# This is a comment to test git add
def home(request):
    import json
    import requests

    # api_requests = requests.get('http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=20002&distance=7&API_KEY=77EB95EF-92E8-4117-9C1F-AAD1B6A33C1A')
    api_request = requests.get('https://data.police.uk/api/stops-no-location?force=cleveland&date=2017-01')

    try:
        api = json.loads(api_request.content)
    except Exception as e:
        api = "Error.... Try agin!"

    return render(request, 'home.html', {'api': api})

def about(request):
    return render(request, 'about.html', {})