import itertools
import time

import zmq

context = zmq.Context()
pusher = context.socket(zmq.PUSH)  # pylint: disable=no-member
pusher.bind("tcp://*:5557")

publisher = context.socket(zmq.PUB)  # pylint: disable=no-member
publisher.bind("tcp://*:5556")

for i in itertools.count():
    time.sleep(1)
    pusher.send_json(i)
    publisher.send_json(i)
