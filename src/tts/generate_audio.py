import pyttsx3
import os

# Initialize TTS engine once
engine = pyttsx3.init()

# Optional: tweak voice properties
engine.setProperty('rate', 170)   # speed (default ~200)
engine.setProperty('volume', 1.0) # 0.0 to 1.0

# Optional: choose voice (0 = male, 1 = female on many systems)
voices = engine.getProperty('voices')
if len(voices) > 1:
    engine.setProperty('voice', voices[1].id)


def generate_audio(text, output_path):
    """
    Convert text to speech and save as audio file
    """
    # Ensure folder exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Generate audio
    engine.save_to_file(text, output_path)
    engine.runAndWait()

    print(f"🔊 Audio saved to {output_path}")