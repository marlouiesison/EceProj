from google.cloud import speech_v1
from google.cloud.speech_v1 import enums
import io

client = speech_v1.SpeechClient.from_service_account_json('<path-to-credentials-file>.json')

with io.open('<path-to-audio-file>', 'rb') as audio_file:
    content = audio_file.read()

audio = speech_v1.RecognitionAudio(content=content)
config = speech_v1.RecognitionConfig(
    encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
    sample_rate_hertz=16000,
    language_code='en-US')

response = client.recognize(config=config, audio=audio)

for result in response.results:
    print(result.alternatives[0].transcript)