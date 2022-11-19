import whisper


model = whisper.load_model('base')

result = model.transcribe("1.mp3")

print(result['text'])
