import getpass;
import os;
import time;
from random import randint;
import pygame as py;

class Last:
    previous = str();
    mus = None;

previous = Last();

def main(audio):
    #Random Variables
    mood = randint(0,2);
    song = randint(0,3);
    #Audio Pre-Execution 
    py.mixer.init();
    #Speech commands
    print('--------------------------------------------------------------');
    print('Speech: You said \"{0}\".'.format(audio));
    
    if 'hi' in audio:
        print('Speech: Hello {0}!'.format(getpass.getuser()));
        previous.previous = audio;

    if 'hello' in audio:
        print('Speech: Hello {0}!'.format(getpass.getuser()));
        previous.previous = audio;

    if 'how are you' in audio:
        if mood == 0:
            print('Speech: I\'m good, thanks.');
        elif mood == 1:
            print('Speech: I\'m Happy {0}!'.format(getpass.getuser()));
        elif mood == 2:
            print('Speech: I\'m sad {0}!'.format(getpass.getuser()));
        previous.previous = audio;

    if 'what\'s your name' in audio:
        print('Speech: My name is Speech.');
        previous.previous = audio;

    if 'what\'s my username' in audio:
        print('Speech: Your username is {0}.'.format(getpass.getuser()));
        previous.previous = audio;

    if 'what time is it' in audio:
        print("Speech: It\'s " + time.strftime("%H:%M:%S"));
        previous.previous = audio;

    if 'what day is today' in audio:
        print("Speech: Today is " + time.strftime("%d"));
        previous.previous = audio;
    
    if 'clear' in audio:
        os.system('cls');
        print('Speech: You said \"{0}\".'.format(audio));
        previous.previous = audio;
    
    if 'open facebook' in audio:
        os.system('start \" \" https://www.facebook.com');
        previous.previous = audio;

    if 'open twitter' in audio:
        os.system('start \" \" https://www.twitter.com');
        previous.previous = audio;

    if 'open developer' in audio:
        os.system('start \" \" https://www.github.com/carlossilva2');
        previous.previous = audio;
    
    if 'play music' in audio:
        previous.previous = audio;
        if song == 0:
            py.mixer.music.load("Media/Master.mp3");
            print('Speech: Currently playing {0}.'.format("Master of Puppets"));
            previous.mus = 0;
        elif song == 1:
            py.mixer.music.load("Media/Beat X.mp3");
            print('Speech: Currently playing {0}.'.format("Beat X"));
            previous.mus = 1;
        elif song == 2:
            py.mixer.music.load("Media/BFG.mp3");
            print('Speech: Currently playing {0}.'.format("BFG - Division"));
            previous.mus = 2;
        elif song == 3:
            py.mixer.music.load("Media/Voodoo.mp3");
            print('Speech: Currently playing {0}.'.format("Voodoo People"));
            previous.mus = 3;
        py.mixer.music.play();
    
    if 'stop music' in audio:
        py.mixer.music.stop();
    
    if 'previous song' in audio:
        if previous.mus == 0:
            py.mixer.music.load("Media/Voodoo.mp3");
            print('Speech: Currently playing {0}.'.format("Voodoo People"));
            previous.mus = 3;
        elif previous.mus == 1:
            py.mixer.music.load("Media/Master.mp3");
            print('Speech: Currently playing {0}.'.format("Master of Puppets"));
            previous.mus = 0;
        elif previous.mus == 2:
            py.mixer.music.load("Media/Beat X.mp3");
            print('Speech: Currently playing {0}.'.format("Beat X"));
            previous.mus = 1;
        elif previous.mus == 3:
            py.mixer.music.load("Media/BFG.mp3");
            print('Speech: Currently playing {0}.'.format("BFG - Division"));
            previous.mus = 2;
        py.mixer.music.play();
    
    if 'next song' in audio:
        if previous.mus == 0:
            py.mixer.music.load("Media/Beat X.mp3");
            previous.mus = 1;
        elif previous.mus == 1:
            py.mixer.music.load("Media/BFG.mp3");
            previous.mus = 2;
        elif previous.mus == 2:
            py.mixer.music.load("Media/Voodoo.mp3");
            previous.mus = 3;
        elif previous.mus == 3:
            py.mixer.music.load("Media/Master.mp3");
            previous.mus = 0;
        py.mixer.music.play();

    if 'music list' in audio:
        if 'detail first' in audio:
            print('Song Name: Beat X');
            print('Artist: dB');
            print('Album: [Beat]erapia');
            print('Year: 2012'),
            print('Style: ');
            previous.previous = audio;
        if 'detail second' in audio:
            print('Song Name: Master of Puppets');
            print('Artist: Metallica');
            print('Album: Master of Puppets');
            print('Year: 1986'),
            print('Style: Thrash Metal');
            previous.previous = audio;
        if 'detail third' in audio:
            print('Song Name: Voodoo People');
            print('Artist: The Prodigy');
            print('Album: Music For The Jilted Generation');
            print('Year: 1994'),
            print('Style: Electronic');
            previous.previous = audio;
        if 'detail fourth' in audio:
            print('Song Name: BFG - Division');
            print('Artist: Mick Gordon');
            print('Album: DOOM');
            print('Year: 2016'),
            print('Style: Doom Metal');
            previous.previous = audio;

    if 'repeat' in audio:
        mood = randint(0,2);
        print('Speech: Your Last Command \"{0}\"'.format(previous.previous));
        if 'hi' in previous.previous:
            print('Speech: Hello {0}!'.format(getpass.getuser()));
        if 'hello' in previous.previous:
            print('Speech: Hello {0}!'.format(getpass.getuser()));
        if 'how are you' in previous.previous:
            if mood == 0:
                print('Speech: I\'m good, thanks.');
            elif mood == 1:
                print('Speech: I\'m Happy {0}!'.format(getpass.getuser()));
            elif mood == 2:
                print('Speech: I\'m sad {0}!'.format(getpass.getuser()));
        if 'what\'s your name' in previous.previous:
            print('Speech: My name is Speech.');
        if 'what\'s my username' in previous.previous:
            print('Speech: Your username is {0}.'.format(getpass.getuser()));
        if 'what time is it' in previous.previous:
            print("Speech: It\'s " + time.strftime("%H:%M:%S"));
        if 'what day is today' in previous.previous:
            print("Speech: Today is " + time.strftime("%d"));
        if 'clear' in previous.previous:
            os.system('cls');
            print('Speech: You said \"{0}\".'.format(previous.previous));   
        if 'open facebook' in previous.previous:
            os.system('start \" \" https://www.facebook.com');
        if 'open twitter' in previous.previous:
            os.system('start \" \" https://www.twitter.com');
        if 'open developer' in previous.previous:
            os.system('start \" \" https://www.github.com/carlossilva2');