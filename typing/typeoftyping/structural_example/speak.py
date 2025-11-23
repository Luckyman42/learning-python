from speakable import Speakable

def speak_loud(speaker : Speakable) -> str:
    return speaker.speak().upper()
