import zmq

if __name__ == "__main__":
    context = zmq.Context()
    receiver = context.socket(zmq.PULL)  # pylint: disable=no-member
    receiver.connect("tcp://localhost:5557")
    subscriber = context.socket(zmq.SUB)  # pylint: disable=no-member
    subscriber.connect("tcp://localhost:5556")
    subscriber.setsockopt_string(zmq.SUBSCRIBE, "")  # pylint: disable=no-member

    poller = zmq.Poller()
    poller.register(receiver, zmq.POLLIN)
    poller.register(subscriber, zmq.POLLIN)

    while True:
        try:
            socks = dict(poller.poll())
        except KeyboardInterrupt:
            break

        if receiver in socks:
            message = receiver.recv_json()
            print(f"Via PULL: {message}")

        if subscriber in socks:
            message = subscriber.recv_json()
            print(f"Via SUB: {message}")
