import speech_recognition as sr

# initialize the recognizer
r = sr.Recognizer()

with sr.AudioFile('srtest.wav') as source:
    # listen for the data (load audio to memory)
    audio_data = r.record(source)
    # recognize (convert from speech to text)
    text = r.recognize_google(audio_data)
    print(text)