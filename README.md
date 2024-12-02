# Transceiver Control

A secure, Dockerized API for remote transceiver and SDR control with role-based command routing. This system is designed to work with radios, SDRs, and similar devices connected via USB or other interfaces. It supports local and cloud deployments for secure command and control.

---

## Features
- **Transceiver Control**: Manage frequency, mode, and other settings remotely.
- **Secure Communication**: Token-based authentication and HTTPS-ready.
- **USB Device Support**: Interact with radios and other USB-connected devices directly from the Docker container.
- **Dockerized Deployment**: Easily deployable on any platform.
- **Scalable**: Supports multiple transceivers and operators.
- **Flexible Deployment**: Operates locally, in the cloud, or in mobile environments (e.g., vehicles, ships).

---

## Technologies
- **Python 3.9**: Backend logic and API development.
- **Flask**: Lightweight web server for the API.
- **Hamlib**: Interface with transceivers.
- **Docker**: Containerization for portability.
- **Nginx** (optional): HTTPS and reverse proxy.

---

## Installation

### Prerequisites
1. **Docker**: Install Docker and Docker Compose. [Get Docker](https://docs.docker.com/get-docker/)
2. **Git**: Clone this repository.
3. **Environment**: Create a `.env` file with a secure token.
4. **USB Devices**: Ensure your USB devices (e.g., CAT cables) are connected and recognized by the host system.

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/fiquett/transceiver-control.git
   cd transceiver-control
