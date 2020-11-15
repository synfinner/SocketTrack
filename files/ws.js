function sTrack() {

// Set up our HTTP request
var xhr = new XMLHttpRequest();

// Setup our listener to process completed requests
xhr.onload = function () {
   if ("WebSocket" in window) {

      // Process our return data
      if (xhr.status >= 200 && xhr.status < 300) {
         // Runs when the request is successful
         var IP = xhr.responseText;
         var ws = new WebSocket("ws://SERVER_IP:8080");
         ws.onopen = function() {
            ws.send(JSON.stringify({ip:IP,loc:window.location.pathname}));
            ws.close()
         };
      } else {
         return false;
      }
   } else {
      return false;
   }

};
xhr.open('GET', 'https://icanhazip.com');
xhr.send();
}
sTrack()
