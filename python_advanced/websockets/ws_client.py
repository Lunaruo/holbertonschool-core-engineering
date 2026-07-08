#!/usr/bin/env python3

import asyncio
import os
import websockets


async def connect_and_send(uri, message):
    async with websockets.connect(uri) as websocket:
        await websocket.send(message)
        response = await websocket.recv()
        return response


async def main():
    uri = os.getenv("WS_URI", "ws://localhost:8765")
    response = await connect_and_send(uri, "Hello WebSocket")
    print(response, end="")


if __name__ == "__main__":
    asyncio.run(main())
