#!/usr/bin/env python3

import asyncio
import websockets


async def validate(websocket):
    async for message in websocket:
        if message.strip() == "":
            await websocket.send("ERR:EMPTY")
        else:
            await websocket.send(f"OK:{message}")


async def main():
    async with websockets.serve(validate, "localhost", 8765):
        await asyncio.Future()  # Run forever


if __name__ == "__main__":
    asyncio.run(main())
