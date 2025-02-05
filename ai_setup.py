import speech_recognition as sr
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pyttsx3

# Set up text-to-speech
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Speed of speech

# Set up Spotify API
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id="d8f83031334d4df8bd063be2c965be3e",
    client_secret="29bee26ea6804068804301758b6dc333",
    redirect_uri="http://localhost:8888/callback",
    scope="user-modify-playback-state,user-read-playback-state,user-read-currently-playing"
))

# Initialize Speech Recognizer
recognizer = sr.Recognizer()

def speak(text):
    """ Convert text to speech """
    engine.say(text)
    engine.runAndWait()

def listen():
    """ Capture voice input and convert it to text """
    with sr.Microphone() as source:
        print("Listening for command...")
        recognizer.adjust_for_ambient_noise(source)  # Reduce noise
        try:
            audio = recognizer.listen(source, timeout=5)
            command = recognizer.recognize_google(audio).lower()
            print(f"Recognized: {command}")
            return command
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand that.")
            return None
        except sr.RequestError:
            print("Could not request results.")
            return None

def spotify_control(command):
    """ Control Spotify based on voice command """
    if "skip song" in command:
        sp.next_track()
        speak("Skipping to the next song.")
    
    elif "play" in command:
        song_name = command.replace("play ", "")
        results = sp.search(q=song_name, limit=1)
        if results['tracks']['items']:
            track_uri = results['tracks']['items'][0]['uri']
            sp.start_playback(uris=[track_uri])
            speak(f"Playing {song_name}")
        else:
            speak("Song not found.")

    elif "pause" in command:
        sp.pause_playback()
        speak("Pausing the song.")

    elif "resume" in command:
        sp.start_playback()
        speak("Resuming playback.")

# Main loop
while True:
    command = listen()
    if command:
        spotify_control(command)
    if command == "exit":
       speak("Goodbye!")
       break
