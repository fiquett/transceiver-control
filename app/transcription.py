import boto3

def transcribe_audio(s3_bucket, s3_key, job_name):
    """Start a transcription job using Amazon Transcribe."""
    transcribe = boto3.client('transcribe')
    audio_uri = f"s3://{s3_bucket}/{s3_key}"
    try:
        response = transcribe.start_transcription_job(
            TranscriptionJobName=job_name,
            Media={'MediaFileUri': audio_uri},
            MediaFormat='wav',
            LanguageCode='en-US',
            OutputBucketName=s3_bucket
        )
        print(f"Transcription job started: {response}")
        return response
    except Exception as e:
        print(f"Failed to start transcription: {e}")
        return None
