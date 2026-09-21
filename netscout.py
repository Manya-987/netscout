"""
NetScout - A lightweight TCP network scanner.

This module provides basic TCP port scanning functionality
using Python sockets.
"""

import argparse
import socket


def scan_port(target, port):
    """
    Attempt to establish a TCP connection to a specific port.

    Args:
        target: Target IP address or hostname.
        port: TCP port number to scan.

    Returns:
        True if the port is open, otherwise False.
    """
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)

    result = sock.connect_ex((target, port))

    sock.close()

    return result == 0


def scan_ports(target, start_port, end_port):
    """
    Scan a range of TCP ports on the target.

    Args:
        target: Target IP address or hostname.
        start_port: First port in the range.
        end_port: Last port in the range.

    Returns:
        A list containing the open ports.
    """
    open_ports = []

    for port in range(start_port, end_port + 1):
        if scan_port(target, port):
            open_ports.append(port)
            print(f"Port {port} is open")

    return open_ports


def parse_port_range(port_range):
    """
    Parse a single port or a port range.

    Examples:
        "80" -> (80, 80)
        "1-100" -> (1, 100)

    Args:
        port_range: Port or port range supplied by the user.

    Returns:
        A tuple containing the start and end ports.

    Raises:
        ValueError: If the port input is invalid.
    """
    if "-" in port_range:
        parts = port_range.split("-", 1)

        if len(parts) != 2:
            raise ValueError("Invalid port range.")

        start_port = int(parts[0])
        end_port = int(parts[1])
    else:
        start_port = int(port_range)
        end_port = start_port

    if not (1 <= start_port <= 65535):
        raise ValueError("Start port must be between 1 and 65535.")

    if not (1 <= end_port <= 65535):
        raise ValueError("End port must be between 1 and 65535.")

    if start_port > end_port:
        raise ValueError("Start port cannot be greater than end port.")

    return start_port, end_port


def create_parser():
    """
    Create the command-line argument parser.

    Returns:
        Configured ArgumentParser object.
    """
    parser = argparse.ArgumentParser(
        description="NetScout - A lightweight TCP network scanner."
    )

    parser.add_argument(
        "target",
        help="Target IP address or hostname."
    )

    parser.add_argument(
        "-p",
        "--ports",
        required=True,
        help="Port or port range to scan. Example: 80 or 1-100."
    )

    return parser


def main():
    """
    Main program entry point.
    """
    parser = create_parser()
    args = parser.parse_args()

    try:
        start_port, end_port = parse_port_range(args.ports)
    except ValueError as error:
        parser.error(str(error))

    print()
    print("NetScout - TCP Network Scanner")
    print("--------------------------------")
    print(f"Target : {args.target}")
    print(f"Ports  : {start_port}-{end_port}")
    print()

    open_ports = scan_ports(
        args.target,
        start_port,
        end_port
    )

    print()
    print("--------------------------------")

    if open_ports:
        print(f"Scan complete. Found {len(open_ports)} open port(s).")
    else:
        print("Scan complete. No open ports found.")


if __name__ == "__main__":
    main()