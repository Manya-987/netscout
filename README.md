# NetScout

A lightweight TCP network scanner written in Python.

NetScout is a command-line security tool designed to demonstrate the fundamentals of TCP port scanning, socket programming, input validation, and automated testing.

## Features

- TCP connect-based port scanning
- Scan a single port
- Scan a range of ports
- IPv4 hostname/IP resolution through Python sockets
- Command-line interface using `argparse`
- Port range validation
- Automated unit tests with `pytest`
- Lightweight implementation using Python standard-library networking

## Project Structure

```text
netscout/
├── netscout.py
├── tests/
│   ├── __init__.py
│   └── test_netscout.py
├── .gitignore
├── LICENSE
└── README.md