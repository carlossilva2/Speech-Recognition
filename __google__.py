#version 2.1

from google import search;

def google(speak):
    for url in search(speak, stop=15):
        print(url);