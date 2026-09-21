import socket
import threading

import pytest

from netscout import parse_port_range, scan_port


def test_parse_single_port():
    assert parse_port_range("80") == (80, 80)


def test_parse_port_range():
    assert parse_port_range("1-100") == (1, 100)


def test_parse_full_port_range():
    assert parse_port_range("1-65535") == (1, 65535)


def test_invalid_start_port():
    with pytest.raises(ValueError):
        parse_port_range("0-100")


def test_invalid_end_port():
    with pytest.raises(ValueError):
        parse_port_range("100-70000")


def test_reversed_port_range():
    with pytest.raises(ValueError):
        parse_port_range("100-1")


def test_local_open_port():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("127.0.0.1", 0))
    server.listen(1)

    port = server.getsockname()[1]

    thread = threading.Thread(
        target=lambda: server.accept(),
        daemon=True
    )
    thread.start()

    try:
        assert scan_port("127.0.0.1", port) is True
    finally:
        server.close()


def test_closed_port():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("127.0.0.1", 0))

    port = server.getsockname()[1]
    server.close()

    assert scan_port("127.0.0.1", port) is False
