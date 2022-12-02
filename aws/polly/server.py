import io
from flask import Flask, send_from_directory, request, send_file
import boto3

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return send_from_directory('.', 'index.html')

    else:
        client = boto3.client('polly', region_name='us-east-1')
        response = client.synthesize_speech(
            Engine='standard',
            LanguageCode='en-US',
            OutputFormat='mp3',
            SampleRate='16000',
            Text=request.json['polly-text'],
            VoiceId='Joanna'
        )

        return send_file(
            io.BytesIO(response['AudioStream'].read()),
            mimetype='audio/mp3',
            download_name='test'
        )
