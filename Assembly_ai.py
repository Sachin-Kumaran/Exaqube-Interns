import assemblyai as aai
import time

start = time.time()

aai.settings.api_key = "your api key here" # use your api key

transcriber = aai.Transcriber()

config = aai.TranscriptionConfig(speaker_labels=True)
audio=r"path of audio file" #use the path of audio file in your file manager
result = transcriber.transcribe(audio, config)


chat_history = {}

for utterance in result.utterances:
    spk = f"Speaker_{utterance.speaker}"
    text = utterance.text

    if spk not in chat_history:
        chat_history[spk] = []

    chat_history[spk].append(text)

# Print conversation history
for speaker, messages in chat_history.items():
    print(f"\n{speaker}:")
    for msg in messages:
        print(" -", msg)

end = time.time()
time_taken_ms = (end - start)
print("Time taken: {:.2f} sec".format(time_taken_ms))
