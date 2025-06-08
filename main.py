import subprocess
import wolframalpha
import pyttsx3
import json
import random
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import sys
import pyjokes
import feedparser
import smtplib
import ctypes
import time
import requests
import shutil
from twilio.rest import Client
from clint.textui import progress
from ecapture import ecapture as ec
from bs4 import BeautifulSoup
from urllib.request import urlopen
from selenium import webdriver

engine = pyttsx3.init('sapi5')
# getter method(gets the current value
# of engine property)
voices = engine.getProperty('voices')
# setter method .[0]=male voice and
# [1]=female voice in set Property.
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    # r = sr.Recognizer()
    # ai = r.recognize_google(audio)
    # print(f"you said: {ai} \n")
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        print("ai:""hey buddy! good morning !")
        speak("hey buddy! good morning !")

    elif hour >= 12 and hour < 18:
        print("ai:""hey buddy! good afternoon !")
        speak("hey buddy !good afternoon !")

    else:
        print("ai:""Good Evening buddy !")
        speak("Good Evening buddy !")

    assname = ("raappo  10 point o")

    print("ai:""I am your Assistant Raappo")
    speak("I am your Assistant Raappo")
    print("ai:", assname)
    speak(assname)


def username():
    print("ai:""What should i call you buddy")
    speak("What should i call you buddy")

    uname = takeCommand()
    speak("Welcome Mister")
    speak(uname)
    columns = shutil.get_terminal_size().columns
    if uname == "None":
        print("#####################".center(columns))
        print("ai:""Welcome User.".center(columns))
        print("#####################".center(columns))
    else:
        print("#####################".center(columns))
        print("ai:""Welcome Mr.", uname.center(columns))
        print("#####################".center(columns))

    print("ai:""How can i Help you, Sir")
    speak("How can i Help you, Sir")


# this method is for taking the commands
# and recognizing the command from the
# speech_Recognition module we will use
# the recongizer method for recognizing
def takeCommand():
    r = sr.Recognizer()
    # from the speech_Recognition module
    # we will use the Microphone module
    # for listening the command
    with sr.Microphone() as source:
        columns = shutil.get_terminal_size().columns
        print("#######################################################################".center(columns))
        print("Listening...")
        # seconds of non-speaking audio before
        # a phrase is considered complete
        r.pause_threshold = 0.5
        # r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        print("ai:""Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print("ai:"f"you said: {query} \n")

    except Exception as e:
        print(e)
        print("ai:""Unable to Recognize your voice.")
        return "None"

    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()

    # Enable low security in gmail
    server.login('your email id', 'your email password')
    server.sendmail('your email id', to, content)
    server.close()


def Hello():
    # This function is for when the assistant
    # is called it will say hello and then
    # take query
    speak("hello sir I am your desktop assistant. /n Tell me how may I help you")
    print("ai:""hello sir I am your desktop assistant. /n Tell me how may I help you")


if __name__ == '__main__':
    clear = lambda: os.system('cls')

    # This Function will clean any
    # command before execution of this python file
    clear()
    wishMe()
    username()

    while True:

        query = takeCommand().lower()

        # All the commands said by user will be
        # stored here in 'query' and will be
        # converted to lower case for easily
        # recognition of command
        if 'wikipedia' in query:
            print("ai:"'Searching Wikipedia...')
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            print("ai:""According to Wikipedia")
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            print("ai:""Here you go to Youtube\n")
            speak("Here you go to Youtube\n")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            print("ai:""Here you go to Google\n")
            speak("Here you go to Google\n")
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            print("ai:""Here you go to Stack Over flow.Happy coding")
            speak("Here you go to Stack Over flow.Happy coding")
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query or "play song" in query:
            print("ai:""Here you go with music")
            speak("Here you go with music")
            # music_dir = "G:\\Song"
            music_dir = "C:\\Users\\RAAPPO\\Music"
            songs = os.listdir(music_dir)
            print(songs)
            random = os.startfile(os.path.join(music_dir, songs[1]))

        elif 'time' in query:
            time = str(datetime.datetime.now())
            print(time)
            hour = time[11:13]
            min = time[14:16]
            print("ai:""The time is " + hour + "Hours and" + min + "Minutes")
            speak("The time is " + hour + "Hours and" + min + "Minutes")

        elif 'email ' in query:
            try:
                print("ai:""What should I say?")
                speak("What should I say?")

                content = takeCommand()
                to = "Receiver email address"
                sendEmail(to, content)
                print("ai:""Email has been sent !")
                speak("Email has been sent !")

            except Exception as e:
                print(e)
                print("ai:""I am not able to send this email")
                speak("I am not able to send this email")


        elif 'send a mail' in query:
            try:
                print("ai:""What should I say?")
                speak("What should I say?")
                content = takeCommand()
                print("ai:""whome should i send")
                speak("whome should i send")
                to = input()
                sendEmail(to, content)
                print("ai:""Email has been sent !")
                speak("Email has been sent !")

            except Exception as e:
                print(e)
                print("ai:""I am not able to send this email")
                speak("I am not able to send this email")

        elif 'how are you' in query:
            print("ai:""I am fine, Thank you")
            speak("I am fine, Thank you")
            print("ai:""How are you, Sir")
            speak("How are you, Sir")

        elif 'fine' in query or "good" in query:
            print("ai:""It's good to know that your fine")
            speak("It's good to know that your fine")

        elif "change my name to" in query:
            query = query.replace("change my name to", "")
            assname = query

        elif "change name" in query:
            print("ai:""What would you like to call me, buddy ")
            speak("What would you like to call me, buddy ")
            assname = takeCommand()
            print("ai:""Thanks for naming me")
            speak("Thanks for naming me")

        elif "what's your name" in query or "What is your name" in query:
            print("ai:""My friends call me",assname)
            speak("My friends call me")
            speak(assname)

        elif 'exit' in query:
            print("ai:""Thanks for giving me your time")
            speak("Thanks for giving me your time")
            exit()

        elif "who made you" in query or "who created you" in query:
            print("ai:""I have been created by raappo aka aditya.")
            speak("I have been created by raappo aka aditya.")

        elif 'joke' in query:
            print("ai:", pyjokes.get_joke())
            speak(pyjokes.get_joke())

        elif "calculate" in query:

            app_id = "Wolframalpha api id"
            client = wolframalpha.Client(app_id)
            indx = query.lower().split().index('calculate')
            query = query.split()[indx + 1:]
            res = client.query(' '.join(query))
            answer = next(res.results).text
            print("The answer is " + answer)
            speak("The answer is " + answer)

        elif 'search' in query or 'play' in query:

            query = query.replace("search", "")
            query = query.replace("play", "")
            webbrowser.open(query)

        elif "who i am" in query:
            print("ai:""If you are talking to me now then definitely you are human.")
            speak("If you are talking to me now then definitely you are human.")

        elif "why you came to world" in query:
            print("ai:""Thanks to raappo. further It's a secret")
            speak("Thanks to raappo. further It's a secret")

        elif 'power point presentation' in query:
            print("ai:""opening Power Point presentation")
            speak("opening Power Point presentation")
            power = r"C:\Program Files\Microsoft Office\root\Office16\POWERPNT.EXE"
            os.startfile(power)

        elif 'is love' in query:
            print("ai:""It is 7th sense that destroy all other senses")
            speak("It is 7th sense that destroy all other senses")

        elif "who are you" in query:
            print("ai:" "I am your virtual assistant created by raappo")
            speak("I am your virtual assistant created by raappo")

        elif 'reason for you' in query:
            print("ai:""I was created as a Minor project by Mister raappo ")
            speak("I was created as a Minor project by Mister raappo ")

        elif 'change background' in query:
            ctypes.windll.user32.SystemParametersInfoW(20,
                                                       0,
                                                       "Location of wallpaper",
                                                       0)
            print("ai:""Background changed successfully")
            speak("Background changed successfully")


        elif 'open bluestack' in query:
            appli = r"C:\\ProgramData\\BlueStacks\\Client\\Bluestacks.exe"
            os.startfile(appli)

        elif 'news' in query:

            try:
                jsonObj = urlopen(
                    '''https://newsapi.org / v1 / articles?source = the-times-of-india&sortBy = top&apiKey =\\times of India Api key\\''')
                data = json.load(jsonObj)
                i = 1

                print("ai:"'here are some top news from the times of india')
                speak('here are some top news from the times of india')

                print('''=============== TIMES OF INDIA ============''' + '\n')

                for item in data['articles']:
                    print(str(i) + '. ' + item['title'] + '\n')
                    print(item['description'] + '\n')
                    speak(str(i) + '. ' + item['title'] + '\n')
                    i += 1
            except Exception as e:

                print(str(e))


        elif 'lock window' in query:
            print("ai:""locking the device")
            speak("locking the device")

            ctypes.windll.user32.LockWorkStation()

        elif 'shutdown system' in query:
            print("ai:""Hold On a Sec ! Your system is on its way to shut down")
            speak("Hold On a Sec ! Your system is on its way to shut down")
            subprocess.call('shutdown / p /f')

        elif 'empty recycle bin' in query:
            winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
            print("ai:""Recycle Bin Recycled")
            speak("Recycle Bin Recycled")


        elif "don't listen" in query or "stop listening" in query:
            print("ai:""for how much time you want to stop jarvis from listening commands")
            speak("for how much time you want to stop jarvis from listening commands")
            a = int(takeCommand())
            time.sleep(a)
            print(a)

        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            print("ai:""User asked to Locate")
            speak("User asked to Locate")
            speak(location)
            webbrowser.open("https://https://www.google.com/ maps / " + location + "")

        elif "camera" in query or "take a photo" in query:
            ec.capture(0, "raappo Camera ", "img.jpg")

        elif "restart" in query:
            subprocess.call(["shutdown", "/r"])

        elif "hibernate" in query or "sleep" in query:
            print("ai:""Hibernating")
            speak("Hibernating")
            subprocess.call("shutdown / h")

        elif "log off" in query or "sign out" in query:
            print("ai:""Make sure all the application are closed before sign-out")
            speak("Make sure all the application are closed before sign-out")
            time.sleep(5)
            subprocess.call(["shutdown", "/l"])

        elif "write a note" in query:
            print("ai:""What should i write, sir")
            speak("What should i write, sir")
            note = takeCommand()
            file = open('jarvis.txt', 'w')
            print("ai:"" Should i include date and time")
            speak(" Should i include date and time")
            snfm = takeCommand()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.datetime.now().strftime("% H:% M:% S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)

        elif "show note" in query:
            print("ai:""Showing Notes")
            speak("Showing Notes")
            file = open("jarvis.txt", "r")
            print(file.read())
            speak(file.read(6))

        elif "update assistant" in query:
            print("ai:""After downloading file please replace this file with the downloaded one")
            speak("After downloading file please replace this file with the downloaded one")
            url = '# url after uploading file'
            r = requests.get(url, stream=True)

            with open("Voice.py", "wb") as Pypdf:

                total_length = int(r.headers.get('content-length'))

                for ch in progress.bar(r.iter_content(chunk_size=2391975),
                                       expected_size=(total_length / 1024) + 1):
                    if ch:
                        Pypdf.write(ch)

        # NPPR9-FWDCX-D2C8J-H872K-2YT43
        elif "raappo" in query:

            wishMe()
            print("ai:""RAAPPO 1 point o in your service Mister")
            speak("RAAPPO 1 point o in your service Mister")
            speak(assname)

        elif "weather" in query:

            # Google Open weather website
            # to get API of Open weather
            api_key = "Api key"
            base_url = "http://api.openweathermap.org / data / 2.5 / weather?"
            print("City name : ")
            speak(" City name ")
            city_name = takeCommand()
            complete_url = base_url + "appid =" + api_key + "&q =" + city_name
            response = requests.get(complete_url)
            x = response.json()

            if x["code"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                current_pressure = y["pressure"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                print(" Temperature (in kelvin unit) = " + str(
                    current_temperature) + "\n atmospheric pressure (in hPa unit) =" + str(
                    current_pressure) + "\n humidity (in percentage) = " + str(
                    current_humidiy) + "\n description = " + str(weather_description))

            else:
                print("ai:"" City Not Found ")
                speak(" City Not Found ")

        elif "send message " in query:
            # You need to create an account on Twilio to use this service
            account_sid = 'Account Sid key'
            auth_token = 'Auth token'
            client = Client(account_sid, auth_token)

            message = client.messages \
                .create(
                body=takeCommand(),
                from_='Sender No',
                to='Receiver No'
            )

            print(message.sid)

        elif "wikipedia" in query:
            webbrowser.open("wikipedia.com")

        elif "Good Morning" in query:
            print("ai:""A warm" + query)
            speak("A warm" + query)
            print("ai:""How are you Mister", assname)
            speak("How are you Mister")
            speak(assname)

        # most asked question from google Assistant
        elif "will you be my gf" in query or "will you be my bf" in query:
            print("ai:""I'm not sure about, may be you should give me some time")
            speak("I'm not sure about, may be you should give me some time")

        elif "how are you" in query:
            print("ai:""I'm fine, glad you me that")
            speak("I'm fine, glad you me that")

        elif "i love you" in query:
            print("ai:""It's hard to understand")
            speak("It's hard to understand")

        elif "what is" in query or "who is" in query:

            # Use the same API key
            # that we have generated earlier
            client = wolframalpha.Client("API_ID")
            res = client.query(query)

            try:
                print(next(res.results).text)
                speak(next(res.results).text)
            except StopIteration:
                print("No results")


def search_web(input):
    driver = webdriver.Firefox()
    driver.implicitly_wait(1)
    driver.maximize_window()

    if 'youtube' in input.lower():

        assistant_speaks("Opening in youtube")
        indx = input.lower().split().index('youtube')
        query = input.split()[indx + 1:]
        driver.get("http://www.youtube.com/results?search_query =" + '+'.join(query))
        return

    elif 'wikipedia' in input.lower():

        assistant_speaks("Opening Wikipedia")
        indx = input.lower().split().index('wikipedia')
        query = input.split()[indx + 1:]
        driver.get("https://en.wikipedia.org/wiki/" + '_'.join(query))
        return

    else:

        if 'google' in input:

            indx = input.lower().split().index('google')
            query = input.split()[indx + 1:]
            driver.get("https://www.google.com/search?q =" + '+'.join(query))

        elif 'search' in input:

            indx = input.lower().split().index('google')
            query = input.split()[indx + 1:]
            driver.get("https://www.google.com/search?q =" + '+'.join(query))

        else:

            driver.get("https://www.google.com/search?q =" + '+'.join(input.split()))

        return


# function used to open application
# present inside the system.
def open_application(input):
    if "chrome" in input:
        assistant_speaks("Google Chrome")
        os.startfile('C:\Program Files (x86)\Google\Chrome\Application\chrome.exe')
        return

    elif "firefox" in input or "mozilla" in input:
        assistant_speaks("Opening Mozilla Firefox")
        os.startfile('C:\Program Files\Mozilla Firefox\\firefox.exe')
        return

    elif "word" in input:
        assistant_speaks("Opening Microsoft Word")
        os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office 2013\\Word 2013.lnk')
        return

    elif "excel" in input:
        assistant_speaks("Opening Microsoft Excel")
        os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office 2013\\Excel 2013.lnk')
        return

    else:

        assistant_speaks("Application not available")
        return
