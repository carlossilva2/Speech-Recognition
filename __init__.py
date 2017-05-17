from commands import main;
import speech_recognition as sr;
from getpass import getuser;
from __misc__ import commands;

recognizer = sr.Recognizer();
microphone = sr.Microphone();
isLoop = True;
isSpeech = True;
wakeUp = True;

commands();

while isLoop:
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source);
        audio = recognizer.listen(source);
    try:
        audio = str(recognizer.recognize_google(audio)).lower();
        
        main(audio);

        if 'goodbye' in audio:
            isLoop = False;
            isSpeech = False;

        if 'bye' in audio:
            isLoop = False;
            isSpeech = False;

        if isSpeech:
            #if wakeUp:
              #  if 'dispatch' in audio:
               #     wakeUp = False;
                #    print('Speech: Listening {0}...'.format(getuser()));
            #wakeUp = True;
            input('Speech: Press ENTER to wake me up!');

    except sr.UnknownValueError:
        print(sr.UnknownValueError);
        continue;

print('Speech: Goodbye {0}.'.format(getuser()));