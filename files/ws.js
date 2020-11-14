function sTrack() {
            
   if ("WebSocket" in window) {
      var ws = new WebSocket("ws://ws_server:8080/");

      ws.onopen = function() {
         var loc = window.location.pathname
         ws.send(loc);
         ws.close()
      };
   } else {
      return false;
   }
}