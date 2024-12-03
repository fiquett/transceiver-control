import subprocess
import os
import logging
from flask import Flask, request, jsonify

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Rigctl configuration
RIG_MODEL = "1022"
BAUD_RATE = "38400"
DEVICE = "/dev/ttyUSB0"
TIMEOUT = "1000"

def execute_rigctl_command(command):
    """Execute a rigctl command and return the cleaned result."""
    full_command = f"rigctl -m {RIG_MODEL} -r {DEVICE} -s {BAUD_RATE} -t {TIMEOUT} {command}"
    try:
        logging.debug(f"Executing: {full_command}")
        result = subprocess.run(
            full_command,
            shell=True,
            text=True,
            capture_output=True,
            env=os.environ,
            errors="replace"
        )
        stdout = result.stdout.strip()
        stderr = result.stderr.strip()
        logging.debug(f"Raw command result: stdout={stdout}, stderr={stderr}")

        if result.returncode == 0:
            cleaned_output = stdout.splitlines()[0] if stdout else "Success"  # Take first valid line
            logging.debug(f"Cleaned command output: {cleaned_output}")
            return cleaned_output
        else:
            logging.error(f"Rigctl error: {stderr}")
            return None
    except Exception as e:
        logging.error(f"Exception while running rigctl command: {e}")
        return None


@app.route('/radio/status', methods=['GET'])
def get_status():
    """Get the radio's status."""
    try:
        frequency = execute_rigctl_command("f") or "Unknown"
        mode = execute_rigctl_command("m") or "Unknown"
        power = execute_rigctl_command("l RFPOWER") or "Unknown"
        vfo = execute_rigctl_command("v") or "Unknown"
        return jsonify({
            "frequency": frequency,
            "mode": mode,
            "power": power,
            "vfo": vfo
        }), 200
    except Exception as e:
        logging.error(f"Exception occurred while getting status: {e}")
        return jsonify({"error": "Internal server error"}), 500

@app.route('/radio/frequency', methods=['GET'])
def get_frequency():
    """Get the current frequency and mode."""
    try:
        frequency = execute_rigctl_command("f")
        mode = execute_rigctl_command("m")
        if frequency and mode:
            return jsonify({"frequency": frequency, "mode": mode}), 200
        return jsonify({"error": "Failed to get frequency or mode"}), 500
    except Exception as e:
        logging.error(f"Exception occurred: {e}")
        return jsonify({"error": "Internal server error"}), 500

@app.route('/radio/frequency', methods=['POST'])
def set_frequency():
    """Set the radio frequency."""
    try:
        data = request.get_json()
        frequency = data.get("frequency")
        if not frequency:
            return jsonify({"error": "Frequency is required"}), 400
        result = execute_rigctl_command(f"F {frequency}")
        if result:
            return jsonify({"message": f"Frequency set to {frequency}"}), 200
        return jsonify({"error": "Failed to set frequency"}), 500
    except Exception as e:
        logging.error(f"Exception occurred: {e}")
        return jsonify({"error": "Internal server error"}), 500

@app.route('/radio/mode', methods=['POST'])
def set_mode():
    """Set the radio mode."""
    try:
        data = request.get_json()
        mode = data.get("mode")
        if not mode:
            return jsonify({"error": "Mode is required"}), 400
        result = execute_rigctl_command(f"M {mode}")
        if result:
            return jsonify({"message": f"Mode set to {mode}"}), 200
        return jsonify({"error": "Failed to set mode"}), 500
    except Exception as e:
        logging.error(f"Exception occurred: {e}")
        return jsonify({"error": "Internal server error"}), 500

@app.route('/radio/power', methods=['GET'])
def get_power():
    """Get the current RF power level."""
    try:
        power = execute_rigctl_command("l RFPOWER")
        if power:
            return jsonify({"power_level": power}), 200
        return jsonify({"error": "Unable to retrieve power level"}), 500
    except Exception as e:
        logging.error(f"Exception occurred while getting power: {e}")
        return jsonify({"error": "Internal server error"}), 500

@app.route('/radio/vfo', methods=['POST'])
def set_vfo():
    """Set the active VFO."""
    try:
        data = request.get_json()
        vfo = data.get('vfo')
        if not vfo:
            return jsonify({"error": "VFO is required"}), 400
        result = execute_rigctl_command(f"V {vfo}")
        if result and "error" not in result.lower():
            return jsonify({"message": f"Switched to {vfo}"}), 200
        return jsonify({"error": f"Failed to switch to VFO: {vfo}"}), 500
    except Exception as e:
        logging.error(f"Exception occurred while setting VFO: {e}")
        return jsonify({"error": "Internal server error"}), 500

@app.route('/radio/test', methods=['GET'])
def test_radio():
    """Perform a basic test of the radio."""
    try:
        frequency = execute_rigctl_command("f") or "Unknown"
        mode = execute_rigctl_command("m") or "Unknown"
        power = execute_rigctl_command("l RFPOWER") or "Unknown"
        vfo = execute_rigctl_command("v") or "Unknown"
        return jsonify({
            "frequency": frequency,
            "mode": mode,
            "power": power,
            "vfo": vfo
        }), 200
    except Exception as e:
        logging.error(f"Exception occurred during radio test: {e}")
        return jsonify({"error": "Internal server error"}), 500

@app.route('/radio/command', methods=['POST'])
def custom_command():
    """Send a custom rigctl command."""
    try:
        data = request.get_json()
        command = data.get('command')
        if not command:
            return jsonify({"error": "Command is required"}), 400
        result = execute_rigctl_command(command)
        if result is not None:
            return jsonify({"result": result}), 200
        return jsonify({"error": "Command execution failed"}), 500
    except Exception as e:
        logging.error(f"Exception occurred: {e}")
        return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
