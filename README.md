# PyUDP-P2P-Chat

A lightweight, terminal-based Peer-to-Peer (P2P) chat application written in Python. It uses UDP Hole Punching to establish direct connections between clients behind NATs (home routers), bypassing the need for a relay server for messages.

## 🚀 Features

* **Direct P2P Messaging:** Chat messages travel directly between peers, ensuring privacy and lower latency.
* **NAT Traversal:** Implements UDP Hole Punching to bypass firewalls and connect users behind standard routers.
* **Central Signaling:** Uses a custom lightweight STUN-like server to discover active peers.
* **Real-time Peer List:** Dynamically fetches and displays online users.
* **Single-Socket Architecture:** Efficiently manages signaling and chatting using a single UDP socket.
* **Multithreaded:** Handles heartbeats, message receiving, and user input simultaneously without blocking.

## 📋 Prerequisites

* **Python 3.x**
* **Network:** An active internet connection.
* **Signaling Server:** A running instance of the STUN signaling server (IP/Port configured in the script).

## ⚙️ Configuration

Before running the script, open the python file (e.g., `client.py`) and edit the configuration section at the top:

```python
# --- CONFIGURATION ---
serverIp = "104.248.18.8"  # IP of your Signaling Server
serverPort = 3478

# USER CONFIGURATION
my_username = "MehmetTaha" # Choose a unique username
my_port = 5454             # Local port to bind to
