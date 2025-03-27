from brainmaze_zmq.abstract import ABExitHandler

try:
    from setuptools_scm import get_version
    __version__ = get_version()
except LookupError:
    __version__ = 'dev'  # Fallback version, adjust as appropriate


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



