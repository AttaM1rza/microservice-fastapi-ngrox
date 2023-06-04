import requests
from config import settings


SERVER_IP_ADDRESS = settings["SERVER"]["SERVER_HOST"]
SERVER_PORT = settings["SERVER"]["SERVICE_PORT"]
ngrok_url = settings["NGROK"]["url"]
response = requests.get(ngrok_url)
print(response.json())
