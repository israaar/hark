import socket
from typing import List


def get_free_port(exclude: List[int]=[]):
    "Find a free port to bind to. Exclude anything from the list provided."
    while True:
        sock = socket.socket()
        sock.bind(('', 0))
        _, port = sock.getsockname()
        sock.close()

        if port not in exclude:
            return port
