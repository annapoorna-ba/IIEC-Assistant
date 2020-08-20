import os
import pyttsx3
import speech_recognition as sr
import pyaudio
prog_dict={("calculator","calci"):"calc",("notepad","editor"):"notepad",("paint","mspaint"):"mspaint",("prompt","cmd"):"cmd",("chrome","browser"):"chrome",('excel','msexcel','spreadsheets'):"EXCEL"}
srr=sr.Recognizer()
print("Welcome to IIEC-Assistant")
pyttsx3.speak("Hello user I can help you to open software programs!!!")
def voice_input():
    while True:
        try:
            with sr.Microphone() as source:
                srr.adjust_for_ambient_noise(source,duration=0.5)
                audio = srr.listen(source)
                text=srr.recognize_google(audio)
                text=text.lower()
                return text
        except sr.UnknownValueError:
            print("could not understand audio")
        except sr.RequestError as e:
            print("Could not request results {0}".format(e))

def software_opener(user_input):
    for word in user_input:
        for pgms in prog_dict:
            if word in pgms:
                cmd=prog_dict[pgms]
                print("opening",cmd)
                os.system(cmd)
                return
    print("App not found")

while True:
    print("Which software you want to open?")
    user_input = voice_input().split()  
    software_opener(user_input)
    ch=input("Do you want to continue ?[y/n]:")
    if ch.lower()=="n":
        break
