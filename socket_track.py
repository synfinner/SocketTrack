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
        print("---NEW CONNECTION---")
        print("[+]Connection from: ",ip)
        print("[+]Origin: ", websocket.request_headers.get('origin'))
        print("[+]Path: ", path)
        print("[+]User-Agent: ", websocket.request_headers.get('user-agent'))
        print("---END CONNECTION---")
        data = "Host: "+ip+"\tOrigin: "+websocket.request_headers.get('origin')+"\tUser-Agent: "+websocket.request_headers.get('user-agent')+"\tPath: "+path
        logging.info(data)
        instruction = """
alert('Hello, friend.');
document.body.innerHTML = document.body.innerHTML + "This page just got updated.";
"""
        await websocket.send(instruction)
        break
asyncio.get_event_loop().run_until_complete(websockets.serve(tracker, '0.0.0.0', 8080))
asyncio.get_event_loop().run_forever()