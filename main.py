import speech_recognition as sr
import os
import subprocess as sp
import webbrowser
import datetime
import numpy as np
import platform
import pyautogui
# import instabot


#for converting text to speech
def say(text):
    system = platform.system()
    if system == 'Windows':  # Windows
        import pyttsx3
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
    else:
        print("Text-to-speech not supported on this platform.")



def takeCommand():
    # Function to recognize speech input
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        audio = r.listen(source) 
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand what you said.")
            return ""
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
            return ""
        except Exception as e:
            print(f"Some Error Occurred; {e}")
            return ""
        



# Function to write content in Notepad
def writeInNotepad():
    # Function to write content in Notepad based on speech input
    try:
        sp.Popen(["notepad.exe"])  # Open Notepad
        print("Notepad opened. Speak now...")
        while True:
            query = takeCommand()  # Recognize speech input
            if query:  # If speech input is recognized
                pyautogui.typewrite(query)  # Type the recognized text in Notepad
    except Exception as e:
        print("Error opening notepad:", e)




'''
# Function to automate Instagram login
def loginToInstagram(username, password):
    # Function to log in to Instagram
    try:
        bot = instabot.Bot()
        bot.login(username=username, password=password)
        print("Login successful.")
        return bot
    except Exception as e:
        print("Error logging in to Instagram:", e)
        return None

def likeReel(bot):
    # Function to like a reel on Instagram
    try:
        bot.like_reel()
        print("Reel liked.")
    except Exception as e:
        print("Error liking reel:", e)

def scrollDown(bot):
    # Function to scroll down on Instagram
    try:
        bot.scroll()
        print("Scrolled down.")
    except Exception as e:
        print("Error scrolling down:", e)

'''



if __name__ == '__main__':
    print('Welcome to Jarvis A.I')
    say("Jarvis A.I")
    while True:
        print("Listening...")
        query = takeCommand()
        # todo: Add more sites
        sites = [["youtube", "https://www.youtube.com"], ["instagram", "https://www.instagram.com"], ["google", "https://www.google.com"],["gmail", "https://mail.google.com/mail/u/0/#inbox"],["github", "https://github.com/"],["netflix", "https://www.netflix.com/in/"]]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]} sir...")
                webbrowser.open(site[1])
        
        # todo: Adding features
        
        if "the time" in query:
            hour = datetime.datetime.now().strftime("%H")
            min = datetime.datetime.now().strftime("%M")
            say(f"Sir time is {hour} bajke {min} minutes")

        elif "open camera".lower() in query.lower():
            sp.run('start microsoft.windows.camera:', shell=True)

        elif "open calculator".lower() in query.lower():
            sp.Popen(["C:\\Windows\\System32\\calc.exe"]).wait()

        elif "open notepad".lower() in query.lower():
           writeInNotepad()

    
        
        
        elif "open settings".lower() in query.lower():
             sp.Popen(["explorer.exe", "ms-settings:"])

        
        elif "open files".lower() in query.lower():
             file_explorer_path = r"C:\Windows\explorer.exe"
             os.startfile(file_explorer_path)

        
        elif "open cmd".lower() in query.lower():
               os.system('start cmd')


        elif "Jarvis Quit".lower() in query.lower():
            exit()


        else:
            print("Chatting...")