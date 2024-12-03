import subprocess
import threading

beacon_running = False

def start_beacon():
    """
    Start an emergency beacon mode.
    Transmits a predefined message in a loop.
    """
    global beacon_running
    beacon_running = True

    def beacon_loop():
        try:
            while beacon_running:
                subprocess.run(
                    ["rigctl", "-m", "122", "-r", "/dev/ttyUSB0", "-s", "4800", "T", "1"],
                    check=True
                )  # Start transmission
                subprocess.run(["echo", "EMERGENCY BEACON: NEED ASSISTANCE"])
                subprocess.run(
                    ["rigctl", "-m", "122", "-r", "/dev/ttyUSB0", "-s", "4800", "T", "0"],
                    check=True
                )  # Stop transmission
                subprocess.run(["sleep", "10"], check=True)  # Wait before next loop
        except subprocess.CalledProcessError as e:
            print(f"Error in beacon loop: {e}")
        finally:
            beacon_running = False

    threading.Thread(target=beacon_loop).start()


def stop_beacon():
    """
    Stop the emergency beacon mode.
    """
    global beacon_running
    beacon_running = False
    print("Beacon mode stopped.")
