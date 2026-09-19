import socket
import sys


def scan_port(target, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    sock.settimeout(1)

    result = sock.connect_ex((target, port))

    sock.close()

    if result == 0:
        return True

    return False


def main():
    if len(sys.argv) != 3:
        print("Usage: python netscout.py <target> <port>")
        sys.exit(1)

    target = sys.argv[1]
    port = int(sys.argv[2])

    print(f"Target : {target}")
    print(f"Port   : {port}")

    if scan_port(target, port):
        print("State  : OPEN")
    else:
        print("State  : CLOSED")


if __name__ == "__main__":
    main()