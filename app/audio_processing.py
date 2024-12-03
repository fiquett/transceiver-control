import subprocess
import boto3
from datetime import datetime

def capture_audio(output_file, duration=30):
    """Record audio from the transceiver."""
    try:
        subprocess.run(
            ["arecord", "-D", "hw:0,0", "-f", "cd", "-t", "wav", "-d", str(duration), output_file],
            check=True
        )
        return output_file
    except subprocess.CalledProcessError as e:
        print(f"Audio capture failed: {e}")
        return None


def upload_to_s3(file_path, bucket_name, s3_key):
    """Upload a file to an S3 bucket."""
    s3 = boto3.client('s3')
    try:
        s3.upload_file(file_path, bucket_name, s3_key)
        print(f"Uploaded {file_path} to s3://{bucket_name}/{s3_key}")
        return True
    except Exception as e:
        print(f"Failed to upload to S3: {e}")
        return False

