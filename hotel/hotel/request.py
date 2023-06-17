import requests
api_key = 'my-api-key'
headers = {'X-API-Key': api_key}
response = requests.get('http://127.0.0.1:8000/room_count_by_category/', headers=headers)
print(response)

