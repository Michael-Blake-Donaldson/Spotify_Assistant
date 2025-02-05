# Voice-Controlled Spotify AI 🎵🎙️

## Features

- **Always Listening** – No need to activate it manually. Just say your command!
- **Spotify Playback Controls** – Skip, pause, resume, and play songs or playlists.
- **Volume Control** – Increase or decrease volume using voice.
- **Playlist Support** – Play a specific Spotify playlist.
- **Shuffle Mode** – Toggle shuffle on/off.
- **Now Playing Info** – Ask what's currently playing.
- **Exit Command** – Say "exit" to stop the program.

## Technologies & Libraries Used

- **Python 3** – Core programming language
- **Spotipy** – Python wrapper for the Spotify Web API
- **SpeechRecognition** – Converts voice input to text
- **Pyttsx3** – Converts text to speech
- **pyaudio** – Enables microphone input
- **Threading** – Keeps the assistant running in the background

## Installation Guide

### 1. Install Required Libraries
```bash
pip install spotipy speechrecognition pyttsx3 pyaudio
```

### 2. Set Up Spotify API

1. Go to [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/).
2. Create an app and get your **Client ID** and **Client Secret**.
3. Modify the `client_id` and `client_secret` in the code.

### 3. Run the Script
```bash
python voice_spotify_ai.py
```

## Usage Instructions

### Basic Commands

| Command | Function |
|---------|----------|
| "skip song" | Skips to the next track |
| "play [song name]" | Plays a specific song |
| "play playlist [playlist name]" | Plays a specific playlist |
| "pause" | Pauses the playback |
| "resume" | Resumes playback |
| "volume up" | Increases volume by 10% |
| "volume down" | Decreases volume by 10% |
| "shuffle on" | Enables shuffle mode |
| "shuffle off" | Disables shuffle mode |
| "what's playing" | Announces the current song |
| "exit" | Stops the program |

## Security Note

🚨 **Never expose your Spotify API keys in public repositories!** 🚨

To keep your credentials safe, use environment variables:

### Windows (CMD)
```bash
set SPOTIFY_CLIENT_ID=your_client_id
set SPOTIFY_CLIENT_SECRET=your_client_secret
```

### Mac/Linux (Bash)
```bash
export SPOTIFY_CLIENT_ID=your_client_id
export SPOTIFY_CLIENT_SECRET=your_client_secret
```

## Future Enhancements

- **Wake Word Activation** ("Hey AI") instead of always listening
- **GUI Integration** for visual feedback
- **More Spotify Controls** like looping or queueing songs

## License

This project is **open-source** and free to use!

## Support & Feedback

Feel free to submit issues or contribute to the project. 🚀

