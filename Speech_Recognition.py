import speech_recognition as sr

# Initialize recognizer
recognizer = sr.Recognizer()

# Load your audio file
audio = 'Power_English_Update.mp3'

from pydub import AudioSegment

# Load an audio file (e.g., MP3)
audio_file = AudioSegment.from_mp3(audio)

# Convert to WAV format
audio_file.export(audio, format='wav')

# Open the audio file
with sr.AudioFile(audio_file) as source:
    # Listen to the audio file
    audio_data = recognizer.record(source)
    
    # Recognize speech using Google Web Speech API
    try:
        text = recognizer.recognize_google(audio_data)
        print("Text: ", text)
    except sr.UnknownValueError:
        print("Google Web Speech API could not understand the audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Web Speech API; {e}")
