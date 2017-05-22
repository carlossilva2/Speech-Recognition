#version 2.1

import getpass;
import os;
import time;
from random import randint;
import pygame as py;
import smtplib;
from email.mime.text import MIMEText;
import speech_recognition as sr;
import json;
import requests;
from gtts import gTTS;
from pathlib import Path;
from __none__ import none;
import socket;
import sounddevice as sd;
import numpy;
from datetime import date;
import math;
from __google__ import google;

class Last:
    previous = str();
    mus = None;

previous = Last();
#_________________________
#Email Attributes
subject = False;
provider = True;
person = False;
recipient = False;
isMail = True;
#_________________________
recognizer = sr.Recognizer();
microphone = sr.Microphone();
#_________________________

def main(audio):
    none();
    #Random Variables
    mood = randint(0,2);
    song = randint(0,3);
    #Audio Pre-Execution 
    py.mixer.init();
    #Speech commands
    print('--------------------------------------------------------------');
    print('Speech: You said \"{0}\".'.format(audio));
#-----------------------------------------------------------------------------------------------------------------------------------------    
    if 'hi' in audio:
        my_file = Path("Media/TextToVoice/{0}.mp3".format(audio));
        print('Speech: Hello {0}!'.format(getpass.getuser()));
        tts = gTTS(text="Hello {0}".format(getpass.getuser()), lang='en');
        if my_file.exists():
            py.mixer.music.load("Media/TextToVoice/none.mp3".format(audio));
            os.remove("Media/TextToVoice/{0}.mp3".format(audio));
            tts.save("Media/TextToVoice/{0}.mp3".format(audio));
            py.mixer.music.load("Media/TextToVoice/{0}.mp3".format(audio));
        else:
            tts.save("Media/TextToVoice/{0}.mp3".format(audio));
            py.mixer.music.load("Media/TextToVoice/{0}.mp3".format(audio));
        py.mixer.music.play();
        previous.previous = audio;
#-----------------------------------------------------------------------------------------------------------------------------------------
    if 'hello' in audio:
        my_file = Path("Media/TextToVoice/{0}.mp3".format(audio));
        print('Speech: Hello {0}!'.format(getpass.getuser()));
        tts = gTTS(text="Hello {0}".format(getpass.getuser()), lang='en');
        if my_file.exists():
            py.mixer.music.load("Media/TextToVoice/none.mp3".format(audio));
            os.remove("Media/TextToVoice/{0}.mp3".format(audio));
            tts.save("Media/TextToVoice/{0}.mp3".format(audio));
            py.mixer.music.load("Media/TextToVoice/{0}.mp3".format(audio));
        else:
            tts.save("Media/TextToVoice/{0}.mp3".format(audio));
            py.mixer.music.load("Media/TextToVoice/{0}.mp3".format(audio));
        py.mixer.music.play();
        previous.previous = audio;
#-----------------------------------------------------------------------------------------------------------------------------------------
    if 'how are you' in audio:
        my_file = Path("Media/TextToVoice/{0}.mp3".format(audio));
        if mood == 0:
            print('Speech: I\'m good, thanks.');
            tts = gTTS(text="I\'m good, thanks.", lang='en');
        elif mood == 1:
            print('Speech: I\'m Happy {0}!'.format(getpass.getuser()));
            tts = gTTS(text="I\'m Happy {0}!".format(getpass.getuser()), lang='en');
        elif mood == 2:
            print('Speech: I\'m sad {0}!'.format(getpass.getuser()));
            tts = gTTS(text="I\'m sad {0}!".format(getpass.getuser()), lang='en');
        if my_file.exists():
            py.mixer.music.load("Media/TextToVoice/none.mp3".format(audio));
            os.remove("Media/TextToVoice/{0}.mp3".format(audio));
            tts.save("Media/TextToVoice/{0}.mp3".format(audio));
            py.mixer.music.load("Media/TextToVoice/{0}.mp3".format(audio));
        else:
            tts.save("Media/TextToVoice/{0}.mp3".format(audio));
            py.mixer.music.load("Media/TextToVoice/{0}.mp3".format(audio));
        py.mixer.music.play();
        previous.previous = audio;
#-----------------------------------------------------------------------------------------------------------------------------------------
    if 'what\'s your name' in audio:
        my_file = Path("Media/TextToVoice/{0}.mp3".format(audio));
        print('Speech: My name is Speech.');
        tts = gTTS(text="My name is Speech.", lang='en');
        if my_file.exists():
            py.mixer.music.load("Media/TextToVoice/none.mp3".format(audio));
            os.remove("Media/TextToVoice/{0}.mp3".format(audio));
            tts.save("Media/TextToVoice/{0}.mp3".format(audio));
            py.mixer.music.load("Media/TextToVoice/{0}.mp3".format(audio));
        else:
            tts.save("Media/TextToVoice/{0}.mp3".format(audio));
            py.mixer.music.load("Media/TextToVoice/{0}.mp3".format(audio));
        py.mixer.music.play();
        previous.previous = audio;
#-----------------------------------------------------------------------------------------------------------------------------------------
    if 'what\'s my username' in audio:
        my_file = Path("Media/TextToVoice/{0}.mp3".format(audio));
        print('Speech: Your username is {0}.'.format(getpass.getuser()));
        tts = gTTS(text="Your username is {0}.".format(getpass.getuser()), lang='en');
        if my_file.exists():
            py.mixer.music.load("Media/TextToVoice/none.mp3".format(audio));
            os.remove("Media/TextToVoice/{0}.mp3".format(audio));
            tts.save("Media/TextToVoice/{0}.mp3".format(audio));
            py.mixer.music.load("Media/TextToVoice/{0}.mp3".format(audio));
        else:
            tts.save("Media/TextToVoice/{0}.mp3".format(audio));
            py.mixer.music.load("Media/TextToVoice/{0}.mp3".format(audio));
        py.mixer.music.play();
        previous.previous = audio;
#-----------------------------------------------------------------------------------------------------------------------------------------
    if 'what time is it' in audio:
        my_file = Path("Media/TextToVoice/{0}.mp3".format(audio));
        print("Speech: It\'s " + time.strftime("%H:%M:%S"));
        tts = gTTS(text="It\'s "+time.strftime("%H:%M:%S"), lang='en');
        if my_file.exists():
            py.mixer.music.load("Media/TextToVoice/none.mp3".format(audio));
            os.remove("Media/TextToVoice/{0}.mp3".format(audio));
            tts.save("Media/TextToVoice/{0}.mp3".format(audio));
            py.mixer.music.load("Media/TextToVoice/{0}.mp3".format(audio));
        else:
            tts.save("Media/TextToVoice/{0}.mp3".format(audio));
            py.mixer.music.load("Media/TextToVoice/{0}.mp3".format(audio));
        py.mixer.music.play();
        previous.previous = audio;
#-----------------------------------------------------------------------------------------------------------------------------------------
    if 'what day is today' in audio:
        my_file = Path("Media/TextToVoice/{0}.mp3".format(audio));
        print("Speech: Today is " + time.strftime("%d"));
        tts = gTTS(text="Today is the" + time.strftime("%d"), lang='en');
        if my_file.exists():
            py.mixer.music.load("Media/TextToVoice/none.mp3".format(audio));
            os.remove("Media/TextToVoice/{0}.mp3".format(audio));
            tts.save("Media/TextToVoice/{0}.mp3".format(audio));
            py.mixer.music.load("Media/TextToVoice/{0}.mp3".format(audio));
        else:
            tts.save("Media/TextToVoice/{0}.mp3".format(audio));
            py.mixer.music.load("Media/TextToVoice/{0}.mp3".format(audio));
        py.mixer.music.play();
        previous.previous = audio;
#-----------------------------------------------------------------------------------------------------------------------------------------    
    if 'clear' in audio:
        os.system('cls');
        print('Speech: You said \"{0}\".'.format(audio));
        previous.previous = audio;
#-----------------------------------------------------------------------------------------------------------------------------------------    
    if 'open facebook' in audio:
        os.system('start \" \" https://www.facebook.com');
        previous.previous = audio;
#-----------------------------------------------------------------------------------------------------------------------------------------
    if 'open twitter' in audio:
        os.system('start \" \" https://www.twitter.com');
        previous.previous = audio;
#-----------------------------------------------------------------------------------------------------------------------------------------
    if 'open developer' in audio:
        os.system('start \" \" https://www.github.com/carlossilva2');
        previous.previous = audio;
#-----------------------------------------------------------------------------------------------------------------------------------------    
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
#-----------------------------------------------------------------------------------------------------------------------------------------    
    if 'stop music' in audio:
        my_file = Path("Media/TextToVoice/{0}.mp3".format(audio));
        py.mixer.music.stop();
        tts = gTTS(text="Music Stopped", lang='en');
        if my_file.exists():
            py.mixer.music.load("Media/TextToVoice/none.mp3".format(audio));
            os.remove("Media/TextToVoice/{0}.mp3".format(audio));
            tts.save("Media/TextToVoice/{0}.mp3".format(audio));
            py.mixer.music.load("Media/TextToVoice/{0}.mp3".format(audio));
        else:
            tts.save("Media/TextToVoice/{0}.mp3".format(audio));
            py.mixer.music.load("Media/TextToVoice/{0}.mp3".format(audio));
        py.mixer.music.play();
#-----------------------------------------------------------------------------------------------------------------------------------------    
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
#-----------------------------------------------------------------------------------------------------------------------------------------    
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
#-----------------------------------------------------------------------------------------------------------------------------------------
    if 'music' in audio:
        if 'detail first' in audio:
            print('Song Name: Beat X');
            print('Artist: dB');
            print('Album: [Beat]erapia');
            print('Year: 2012'),
            print('Style: ');
            previous.previous = audio;
        if 'detail ii' in audio:
            print('Song Name: Master of Puppets');
            print('Artist: Metallica');
            print('Album: Master of Puppets');
            print('Year: 1986'),
            print('Style: Thrash Metal');
            previous.previous = audio;
        if 'detail 3rd' in audio:
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
#-----------------------------------------------------------------------------------------------------------------------------------------  
# Email sender Not Working YET, cannot pass security 
    #if 'email' in audio:
    #    provider = True;
     #   isMail = True;
     #   while isMail:
     #       with microphone as source:
     #           recognizer.adjust_for_ambient_noise(source);
     #           listen = recognizer.listen(source);
     #       print('Welcome to email Sender {0}!'.format(getpass.getuser()));
     #       try:
     #           #with open(textfile.txt) as fp:
     #           msg = MIMEText(open("textfile.txt").read());
#                if provider:
#                    print('Speech: Please say your E-Mail Address!');
 #                   listen = str(recognizer.recognize_google(listen)).lower();
  #                  if 'at' in listen:
   #                     listen.replace("at","@");
    #                if 'dot' in listen:
     #                   listen.replace("dot",".");
      #              listen.replace(" ","");
       #             msg['From'] = listen;
        #            #msg['From']="cmiguelrsilva@gmail.com";
         #           print('Speech: From E-Mail Address -> {0}'.format(listen));
          #          provider = False;
          #          person = True;
          #          listen = "";
          #      if person:
          #          print('Speech: Please say the other Person\'s E-Mail Address!');                    
          #          listen = str(recognizer.recognize_google(listen)).lower();
          #          if 'at' in listen:
          #              listen.replace(" at ","@");
          #          if 'dot' in listen:
          #              listen.replace("dot",".");
          #          listen.replace(" ","");                  
          #          msg['To'] = listen;
          #          #msg['To'] = "carlos.silva@studentpartner.com";
          #          print('Speech: To E-Mail Address -> {0}'.format(listen));
          #          person = False;
          #          subject = True;
          #          listen = "";
          #      if subject:
          #          print('Speech: Please say the E-mail\'s Subject/Content');
          #          listen = str(recognizer.recognize_google(audio)).lower();
          #          msg['Subject'] = listen;
          #          #msg['Subject'] = "Hi! This email was sent by Speech! Great Hacking";
          #          print('Speech: E-Mail Subject/Content -> {0}'.format(listen));
          #          subject = False;
          #          listen = "";
          #      s = smtplib.SMTP('http://smtp.gmail.com',25)
          #      s.send_message(msg);
          #      s.quit();
          #      isMail = False;
          #  except sr.UnknownValueError:
          #      print(sr.UnknownValueError);
#-----------------------------------------------------------------------------------------------------------------------------------------
    if 'gps' in audio:
        my_file = Path("Media/TextToVoice/{0}.mp3".format(audio));
        send_url = 'http://freegeoip.net/json';
        r = requests.get(send_url);
        j = json.loads(r.text);
        lat = j['latitude'];
        lon = j['longitude'];
        print("Speech: Latitude->{0}".format(lat));
        print("Speech: Longitude->{0}".format(lon));
        tts = gTTS(text="Latitude:{}. Longitude:{}".format(lat,lon), lang='en');
        if my_file.exists():
            py.mixer.music.load("Media/TextToVoice/none.mp3".format(audio));
            os.remove("Media/TextToVoice/{0}.mp3".format(audio));
            tts.save("Media/TextToVoice/{0}.mp3".format(audio));
            py.mixer.music.load("Media/TextToVoice/{0}.mp3".format(audio));
        else:
            tts.save("Media/TextToVoice/{0}.mp3".format(audio));
            py.mixer.music.load("Media/TextToVoice/{0}.mp3".format(audio));
        py.mixer.music.play();     
#----------------------------------------------------------------------------------------------------------------------------------------- 
    if 'ip' in audio:
        my_file = Path("Media/TextToVoice/{0}.mp3".format(audio));
        socket.gethostbyname(socket.gethostname());
        print("Speech: IP: "+socket.gethostbyname(socket.gethostname()));
        tts = gTTS(text="IP: "+socket.gethostbyname(socket.gethostname()), lang='en');
        if my_file.exists():
            py.mixer.music.load("Media/TextToVoice/none.mp3".format(audio));
            os.remove("Media/TextToVoice/{0}.mp3".format(audio));
            tts.save("Media/TextToVoice/{0}.mp3".format(audio));
            py.mixer.music.load("Media/TextToVoice/{0}.mp3".format(audio));
        else:
            tts.save("Media/TextToVoice/{0}.mp3".format(audio));
            py.mixer.music.load("Media/TextToVoice/{0}.mp3".format(audio));
        py.mixer.music.play();
#----------------------------------------------------------------------------------------------------------------------------------------- 
    if 'record' in audio:
        my_file = Path("Media/TextToVoice/start.mp3");
        myarray = numpy.array([]);
        duration = 10;
        fs = 48000; 
        print("Speech: You can start talking in 5 seconds {0}.".format(getpass.getuser()));
        tts = gTTS(text="You can start talking in 5 seconds {0}.".format(getpass.getuser()), lang='en');
        if my_file.exists():
            py.mixer.music.load("Media/TextToVoice/none.mp3");
            os.remove("Media/TextToVoice/start.mp3");
            tts.save("Media/TextToVoice/start.mp3");
            py.mixer.music.load("Media/TextToVoice/start.mp3");
        else:
            tts.save("Media/TextToVoice/start.mp3");
            py.mixer.music.load("Media/TextToVoice/start.mp3");
        py.mixer.music.play();
        time.sleep(5);
        print("Speech: Recording!"); 
        myarray = sd.rec(int(duration * fs), samplerate=fs, channels=2);
        sd.default.samplerate = fs;
        sd.default.channels = 2;
        sd.wait();
        print("Speech: Your record is ready {0}. Playing it in 5 seconds.".format(getpass.getuser()));
        tts = gTTS(text="Your record is ready {0}. Playing it in 5 seconds.".format(getpass.getuser()), lang='en');
        my_file2 = Path("Media/TextToVoice/stop.mp3");
        if my_file2.exists():
            py.mixer.music.load("Media/TextToVoice/none.mp3");
            os.remove("Media/TextToVoice/stop.mp3");
            tts.save("Media/TextToVoice/stop.mp3");
            py.mixer.music.load("Media/TextToVoice/stop.mp3");
        else:
            tts.save("Media/TextToVoice/stop.mp3");
            py.mixer.music.load("Media/TextToVoice/stop.mp3");
        py.mixer.music.play();
        time.sleep(5);
        sd.play(myarray, fs);
#----------------------------------------------------------------------------------------------------------------------------------------- 
    if 'how old are you' in audio:
        age = date.today()-date(2017,5,15);
        years = age.days/365;
        print("Speech: I\'m {} days old, which is {} years.".format(age.days,years));       
        my_file = Path("Media/TextToVoice/{0}.mp3".format(audio));
        tts = gTTS(text="I\'m {} days old, which is {} years.".format(age.days, years), lang='en');
        if my_file.exists():
            py.mixer.music.load("Media/TextToVoice/none.mp3".format(audio));
            os.remove("Media/TextToVoice/{0}.mp3".format(audio));
            tts.save("Media/TextToVoice/{0}.mp3".format(audio));
            py.mixer.music.load("Media/TextToVoice/{0}.mp3".format(audio));
        else:
            tts.save("Media/TextToVoice/{0}.mp3".format(audio));
            py.mixer.music.load("Media/TextToVoice/{0}.mp3".format(audio));
        py.mixer.music.play();     
#-----------------------------------------------------------------------------------------------------------------------------------------
    if 'google search' in audio:
        speak = str(audio);
        speak.replace("google search",".");
        print(speak);
        my_file = Path("Media/TextToVoice/results.mp3");
        print("Speech: Here are 15 results of {}, {}.".format(speak,getpass.getuser()));
        tts = gTTS(text="Here are 15 results of {}, {}.".format(speak,getpass.getuser()), lang='en');
        if my_file.exists():
            py.mixer.music.load("Media/TextToVoice/none.mp3");
            os.remove("Media/TextToVoice/results.mp3");
            tts.save("Media/TextToVoice/results.mp3");
            py.mixer.music.load("Media/TextToVoice/results.mp3");
        else:
            tts.save("Media/TextToVoice/results.mp3");
            py.mixer.music.load("Media/TextToVoice/results.mp3");        
        google(speak);   
        py.mixer.music.play();       
#-----------------------------------------------------------------------------------------------------------------------------------------
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