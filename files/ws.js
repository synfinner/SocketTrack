function sTrack() {

   if ("WebSocket" in window) {
      var xhr = new XMLHttpRequest();
      xhr.open('GET', 'https://icanhazip.com');
      xhr.send();
      xhr.onload = function () {
         if (xhr.status >= 200 && xhr.status < 300) {
            // Runs when the request is successful
            var IP = xhr.responseText; // Set ip to the response.
            var ws = new WebSocket("ws://SERVER:8080/sockettrack");
            ws.onopen = function() {
               // send ip and paath to server
               ws.send(JSON.stringify({ip:IP,loc:window.location.pathname}));
               // close the web socket 
               ws.close()
            };
         } else {
            return false;
         }
      };
   } else {
      return false
   }
};

sTrack()
