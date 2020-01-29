# make sure ES is up and running
import requests
response = requests.get('http://localhost:9200')
print(response.content)