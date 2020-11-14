# SocketTrack
 Tracking with WebSocket and pywebsockets


It's recommended to use ssl on the SocketTrack endpoint/websocket server. In this case, we're using a reverse proxy via nginx and let's encrypt. 

```
location /sockettrack/ {
    proxy_pass ​http://127.0.0.1:8080;
    proxy_http_version 1.1;
    proxy_set_header Upgrade $http_upgrade;
    proxy_set_header Connection "Upgrade";
}
```

Be sure to change the `ws.js` file if moving to SSL!

From: 

```
var ws = new WebSocket("ws://SERVER_URL:8080/");
```

To: 

```
var ws = new WebSocket("wss://SERVER_URL:8080/");
```