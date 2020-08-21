import asyncio
from concurrent.futures import ThreadPoolExecutor as Executor
import time


async def main():
    loop = asyncio.get_running_loop()
    future = loop.run_in_executor(None, blocking)

    try:
        print(f"{time.ctime()} Hello!")
        await asyncio.sleep(1.0)
        print(f"{time.ctime()} Goodbye!")
    finally:
        await future


def blocking():
    time.sleep(1.5)
    print(f"{time.ctime()} Hello from a thread!")


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bye!")
