
# Transceiver Control

A secure, Dockerized API for remote transceiver and SDR control with role-based command routing. This system is designed to be transceiver-agnostic, working seamlessly with radios like the Xiegu G90, X6100, X6200, Yaesu FT-857, and other USB-connected devices. It supports both local and cloud deployments for secure command and control.

---

## Features

- **Transceiver-Agnostic**: Compatible with various transceivers, including Xiegu G90, X6100, X6200, and Yaesu FT-857.
- **Remote Control**: Manage frequency, mode, power, VFO, and other settings remotely.
- **Secure Communication**: Token-based authentication with HTTPS support.
- **USB Device Support**: Direct interaction with transceivers using Hamlib over USB or serial connections.
- **Dockerized Deployment**: Easily deployable on any platform supporting Docker.
- **Role-Based Routing**: Assign commands and access levels based on operator roles.
- **Scalable Architecture**: Supports multiple transceivers and operators simultaneously.
- **Flexible Deployment**: Operates locally, in mobile environments (e.g., vehicles, ships), or in the cloud.

---

## Technologies

- **Python 3.9**: Backend logic and API development.
- **Flask**: Lightweight web server for the API.
- **Hamlib**: Industry-standard interface for radio transceivers.
- **Docker**: Containerization for portability and isolation.
- **Nginx** (optional): HTTPS and reverse proxy for production deployments.

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
   git clone https://github.com/your-username/transceiver-control.git
   cd transceiver-control
   ```

2. Build and start the Docker container:
   ```bash
   docker-compose up --build
   ```

3. Access the API on `http://localhost:5000`.

---

## Usage

### API Endpoints

#### General
- `GET /radio/test`: Test the connection and retrieve the current state of the transceiver.
- `GET /radio/status`: Retrieve the status of the transceiver, including frequency, mode, power, and VFO.

#### Frequency Control
- `GET /radio/frequency`: Retrieve the current frequency and mode.
- `POST /radio/frequency`:
  ```json
  {
    "frequency": "14200000"
  }
  ```

#### Power Control
- `GET /radio/power`: Retrieve the current power level.
- `POST /radio/power`:
  ```json
  {
    "power_level": "50"
  }
  ```

#### Mode Control
- `POST /radio/mode`:
  ```json
  {
    "mode": "USB"
  }
  ```

#### VFO Control
- `POST /radio/vfo`:
  ```json
  {
    "vfo": "VFOB"
  }
  ```

#### Custom Commands
- `POST /radio/command`:
  ```json
  {
    "command": "your-command-here"
  }
  ```

---

## Supported Transceivers

The system is tested and compatible with:
- **Xiegu G90**
- **Xiegu X6100**
- **Xiegu X6200**
- **Yaesu FT-857**

For other transceivers, support may vary based on Hamlib backend capabilities.

---

## Development

1. Run the API locally:
   ```bash
   flask run
   ```

2. Test the API using `curl`:
   ```bash
   curl -X GET http://localhost:5000/radio/test
   ```

3. Add new endpoints or functionality in `main.py`.

---

## Deployment

For production, use Docker Compose with an Nginx reverse proxy and HTTPS:
1. Configure an Nginx server block for HTTPS.
2. Start the application:
   ```bash
   docker-compose -f docker-compose.prod.yml up --build
   ```

---

## Contributing

1. Fork the repository.
2. Create a feature branch.
3. Submit a pull request with your changes.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Future Enhancements

- Add support for additional transceivers.
- Implement advanced command queuing and logging.
- Support custom macros for frequently used commands.
- Enable real-time status updates with WebSocket support.
