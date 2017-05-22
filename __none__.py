#version 2.1

from gtts import gTTS;
from pathlib import Path;
import os;

def none():
    my_file = Path("Media/TextToVoice/none.mp3");
    tts = gTTS(text="Null", lang='en');
    if my_file.exists():
        os.remove("Media/TextToVoice/none.mp3");
        tts.save("Media/TextToVoice/none.mp3");
    else:
        tts.save("Media/TextToVoice/none.mp3");