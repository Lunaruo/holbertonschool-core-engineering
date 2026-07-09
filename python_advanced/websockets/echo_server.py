#!/usr/bin/env python3

import asyncio
import websockets
from websockets.exceptions import ConnectionClosed


async def connection_handler(websocket):
    try:
        async for message in websocket:
            await websocket.send(message)
    except ConnectionClosed:
        pass


async def main():
    async with websockets.serve(connection_handler, "localhost", 8765):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
