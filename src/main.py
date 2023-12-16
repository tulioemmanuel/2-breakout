import asyncio
import pygame
from breakout import Breakout


async def main():
    breakout = Breakout()
    while breakout.running:
        breakout.mainloop()
        await asyncio.sleep(0)
    breakout.cleanup()

if __name__ == "__main__":
    asyncio.run(main())
