# SocketTrack

Tracking with WebSocket and pywebsockets

## Setup

Install requirements: 

```
pip install -r requirements.txt
```

## What is this?

This is just a simple project to allow one to collect access data for sites. For example, import the js file, invoke the function, and now you can track. 

This script will perform an XHR to grab the client's external IP address, the orgin web server where the request was initiated, the path/resource where this was loaded, and the user-agent. 

This will output the following in terminal (also logged):

```
---NEW CONNECTION---
[+]Connection from:  192.168.2.54
[+]Origin:  http://192.168.2.62:9000
[+]Path:  /files/example.html
[+]User-Agent:  Mozilla/5.0 (iPhone; CPU iPhone OS 14_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.1 Mobile/15E148 Safari/604.1
---END CONNECTION---
```

**Why would I want this?** I don't know. You never know when you'd want to see where traffic is coming from. This is also relatively benign; a single message sent to the server and then the connection is closed. 

## Simple Execution

Once you have the socket server running, anytime/anywhere you want to log requests, simply add the script into the html `<head>`

```
<head>
  <script type = "text/javascript" src="ws.js"></script>
</head>
```

## SSL Notes


It's recommended to use ssl on the SocketTrack endpoint/websocket server. In this case, we're using a reverse proxy via nginx and let's encrypt. 

```
location /sockettrack {
		proxy_pass http://127.0.0.1:8080;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "Upgrade";
        proxy_set_header Host $host;
}
```

Be sure to change the `ws.js` file if moving to SSL!

From: 

```
var ws = new WebSocket("ws://SERVER_URL/sockettrack");
```

To: 

```
var ws = new WebSocket("wss://SERVER_URL/sockettrack");
```

## Disclaimer

*This script is served as-is and is part of an educational project for research purposes. I am not responsible for your actions with this script.*