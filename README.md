# SocketTrack

Tracking with WebSocket, XHR, and pywebsockets

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
[+]Screen Dimmensions:  1792 x 1120
---END CONNECTION---
```

- **Connection** - External IP address of visitor
- **Origin** - Web server where the script executed
- **Path** - File that was executed from
- **User-Agent** - Obviously the user-agent. 
- **Screen Dimmensions** - Screen data provided by `screen.height` and `screen.width`

**Why would I want this?** I don't know. You never know when you'd want to see where traffic is coming from. This is also relatively benign; a single message sent to the server and then the connection is closed. Unless you decided to play with [executing more JavaScript](https://github.com/synfinner/SocketTrack#additional-javascript-execution)

## Simple Execution

Once you have the socket server running, anytime/anywhere you want to log requests, simply add the script into the html `<head>`

```
<head>
  <script type = "text/javascript" src="ws.js"></script>
</head>
```

## Additional JavaScript Execution

One of the other features of this script is that it has an `eval()` statement which will get dynamically updated based on a websocket server message. This allows one to inject whatever JavaScript that they want from the server.  

In this repository, the `command.txt` file just throws an alert and a DOM body update. There are, of course, several other things that can be done with such control. This is nice becasue now we don't have to deal with manually editing the server code, killing the process, and starting the server again just to push new commands.

## Use case

On a site I control, I added `ws.js` to the head section of the site's main template file. This causes the websocket tracking to be executed on any page that a user visits. This provides background tracking of user site interaction without intrusive nature. There are a few reasons that this can be useful. Simply tracking users is one example.

As a pentester, I've often come across the need to find targets to pivot to that are user-controlled sytems. After compromising a site, a pentester could load this script on an intranet site and find users to target. 

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