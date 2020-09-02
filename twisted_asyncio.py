from time import ctime

from twisted.internet import asyncioreactor

asyncioreactor.install()
from twisted.internet import reactor, defer, task


async def main():
    for i in range(5):
        print(f"{ctime()} Hello {i}")
        await task.deferLater(reactor, 1, lambda: None)


if __name__ == "__main__":
    defer.ensureDeferred(main())
    reactor.run()  # pylint: disable=no-member
