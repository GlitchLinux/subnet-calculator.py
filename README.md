# CLI Subnet Calculator

A simple command-line tool written in Python that calculates subnets based on a given IPv4 address and subnet prefix. This tool is designed for network engineers, students, or anyone interested in understanding subnetting.

## Features

- Calculate subnets for a given IPv4 address and prefix.
- Display detailed information for each subnet, including:
  - Network ID
  - First and last usable IP addresses
  - Broadcast address
- Input validation for IPv4 addresses and subnet prefixes.
- User-friendly command-line interface.

## Installation

1. Ensure you have Python 3.x installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. Clone the repository or download the script file:

   ```bash
   git clone https://github.com/GlitchLinux/subnet-calculator.py.git
   cd subnet-calculator.py
   python subnet-calculator.py


EXAMPLE OUTPUT:

Subnetting 192.168.0.0 with a /26 results in:

ID               First / Last                         Broadcast     
----------------------------------------------------------------------
192.168.0.0    | 192.168.0.1     -   192.168.0.62   | 192.168.0.63   |
192.168.0.64   | 192.168.0.65    -   192.168.0.126  | 192.168.0.127  |
192.168.0.128  | 192.168.0.129   -   192.168.0.190  | 192.168.0.191  |
192.168.0.192  | 192.168.0.193   -   192.168.0.254  | 192.168.0.255  |

Subnet Mask: 255.255.255.192
