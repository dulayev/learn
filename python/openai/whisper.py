from openai import OpenAI
client = OpenAI()

audio_file = open("/Users/aleksey/Downloads/rust-12.mp3", "rb")

transcript = client.audio.transcriptions.create(
  model="whisper-1",
  file=audio_file,
  response_format="text"
)

with open("/Users/aleksey/Downloads/rust-12.txt", "w") as f:
    print(transcript, file=f)
