#!/usr/bin/env python3

import asyncio
import websockets
import logging

logging.basicConfig(format='%(asctime)s - %(message)s',filename='socket_track.log', encoding='utf-8', level=logging.INFO)

async def tracker(websocket, path):
    async for message in websocket:
        print("---NEW CONNECTION---")
        print("[+]Connection from: ",websocket.remote_address[0])
        print("[+]Origin: ", message.rstrip())
        print("[+]User-Agent: ", websocket.request_headers.get('user-agent'))
        print("---END CONNECTION---")
        data = "Host: "+websocket.remote_address[0]+"\tUser-Agent: "+websocket.request_headers.get('user-agent')+"\tPath: "+message.rstrip()
        logging.info(data)
        break
asyncio.get_event_loop().run_until_complete(websockets.serve(tracker, '0.0.0.0', 8080))
asyncio.get_event_loop().run_forever()