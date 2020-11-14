function sTrack() {
            
   if ("WebSocket" in window) {
      var ws = new WebSocket("ws://SERVER_URL/sockettrack");
      // change to wss if using ssl.

      ws.onopen = function() {
         var loc = window.location.pathname
         ws.send(loc);
         ws.close()
      };
   } else {
      return false;
   }
}