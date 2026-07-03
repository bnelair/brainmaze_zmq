from importlib.metadata import version, PackageNotFoundError

from brainmaze_zmq.abstract import ABExitHandler

try:
    __version__ = version("brainmaze-zmq")
except PackageNotFoundError:
    __version__ = "0.0.0"


from brainmaze_zmq.utils import (
    ping_ip, check_port, is_socket_alive, setup_publisher_socket, setup_subscriber_socket,
    setup_pull_socket, setup_push_socket, setup_reply_socket, setup_request_socket, send_exit_signal
)

__all__ = [
    'ping_ip',
    'check_port',
    'is_socket_alive',
    'setup_publisher_socket',
    'setup_subscriber_socket',
    'setup_pull_socket',
    'setup_reply_socket',
    'setup_request_socket',
    'send_exit_signal',
    'ABExitHandler',
]



