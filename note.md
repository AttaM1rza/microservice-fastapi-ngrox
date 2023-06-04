# setup for the first use
First run the Fast Api service on the server.
```
python3 main.py
```
Open up a new server cmd window.

install on the server ngrok ([more info](https://ngrok.com/download))
```
curl -s https://ngrok-agent.s3.amazonaws.com/ngrok.asc | sudo tee /etc/apt/trusted.gpg.d/ngrok.asc >/dev/null && echo "deb https://ngrok-agent.s3.amazonaws.com buster main" | sudo tee /etc/apt/sources.list.d/ngrok.list && sudo apt update && sudo apt install ngrok
```
add your token [login](https://dashboard.ngrok.com/get-started/setup)
```
ngrok config add-authtoken <token>
```
after that run (PS: port is defined in settings.ini as `SERVICE_PORT`)
```
ngrok http <port>  
```
Now copy the url and paste it on the client side. the url should look like this ` https://487c-2001-19f0-5-4c43-5400-4ff-fe76-5d1b.ngrok-free.app`
