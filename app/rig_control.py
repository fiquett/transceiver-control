import subprocess


def set_frequency(freq):
    """
    Set the operating frequency of the transceiver.

    Args:
        freq (int): Frequency in Hz.

    Returns:
        bool: True if the frequency was set successfully, False otherwise.
    """
    try:
        subprocess.run(["rigctl", "-m", "122", "-r", "/dev/ttyUSB0", "-s", "4800", "F", str(freq)], check=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Failed to set frequency: {e}")
        return False


def set_mode(mode):
    """
    Set the operating mode of the transceiver.

    Args:
        mode (str): Mode to set (e.g., "USB", "LSB", "FM", "AM").

    Returns:
        bool: True if the mode was set successfully, False otherwise.
    """
    try:
        subprocess.run(["rigctl", "-m", "122", "-r", "/dev/ttyUSB0", "-s", "4800", "M", mode, "0"], check=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Failed to set mode: {e}")
        return False


def get_frequency():
    """
    Get the current operating frequency of the transceiver.

    Returns:
        int: Current frequency in Hz, or None if the operation failed.
    """
    try:
        result = subprocess.run(["rigctl", "-m", "122", "-r", "/dev/ttyUSB0", "-s", "4800", "f"],
                                stdout=subprocess.PIPE, text=True, check=True)
        return int(result.stdout.strip())
    except subprocess.CalledProcessError as e:
        print(f"Failed to get frequency: {e}")
        return None


def get_mode():
    """
    Get the current operating mode of the transceiver.

    Returns:
        str: Current mode (e.g., "USB", "LSB"), or None if the operation failed.
    """
    try:
        result = subprocess.run(["rigctl", "-m", "122", "-r", "/dev/ttyUSB0", "-s", "4800", "m"],
                                stdout=subprocess.PIPE, text=True, check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Failed to get mode: {e}")
        return None


def set_power_level(power):
    """
    Set the power level of the transceiver.

    Args:
        power (int): Power level as a percentage (0 to 100).

    Returns:
        bool: True if the power level was set successfully, False otherwise.
    """
    try:
        subprocess.run(["rigctl", "-m", "122", "-r", "/dev/ttyUSB0", "-s", "4800", "P", str(power)], check=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Failed to set power level: {e}")
        return False


def transmit():
    """
    Key the transmitter.

    Returns:
        bool: True if successful, False otherwise.
    """
    try:
        subprocess.run(["rigctl", "-m", "122", "-r", "/dev/ttyUSB0", "-s", "4800", "T", "1"], check=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Failed to key the transmitter: {e}")
        return False


def unkey_transmitter():
    """
    Unkey the transmitter.

    Returns:
        bool: True if successful, False otherwise.
    """
    try:
        subprocess.run(["rigctl", "-m", "122", "-r", "/dev/ttyUSB0", "-s", "4800", "T", "0"], check=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Failed to unkey the transmitter: {e}")
        return False
