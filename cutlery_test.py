from enum import Enum, auto
from queue import Queue
import sys
import threading

from attr import attrs, attrib


class Task(Enum):
    PREPARE_TABLE = auto()
    CLEAR_TABLE = auto()
    SHUTDOWN = auto()


class ThreadBot(threading.Thread):
    def __init__(self):
        super().__init__(target=self.manage_table)
        self.cutlery = Cutlery(knives=0, forks=0)
        self.tasks = Queue()

    def manage_table(self):
        while True:
            task = self.tasks.get()
            if task == Task.PREPARE_TABLE:
                kitchen.give(to=self.cutlery, knives=4, forks=4)
            elif task == Task.CLEAR_TABLE:
                self.cutlery.give(to=kitchen, knives=4, forks=4)
            elif task == Task.SHUTDOWN:
                return


@attrs
class Cutlery:
    knives = attrib(default=0)
    forks = attrib(default=0)

    def give(self, to: "Cutlery", knives=0, forks=0):
        self.change(-knives, -forks)
        to.change(knives, forks)

    def change(self, knives, forks):
        self.knives += knives
        self.forks += forks


if __name__ == "__main__":
    kitchen = Cutlery(knives=100, forks=100)
    bots = [ThreadBot() for i in range(10)]

    for bot in bots:
        for i in range(int(sys.argv[1])):
            bot.tasks.put(Task.PREPARE_TABLE)
            bot.tasks.put(Task.CLEAR_TABLE)
        bot.tasks.put(Task.SHUTDOWN)

    print("Kitchen inventory before service:", kitchen)
    for bot in bots:
        bot.start()

    for bot in bots:
        bot.join()
    print("Kitchen inventory after service:", kitchen)
