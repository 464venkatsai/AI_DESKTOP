# This module is used to deliver speech
import pyttsx3
import datetime
import mysql.connector
import speech_recognition as sr
import wikipedia as wp
import webbrowser as wb
import os 
import random
from bs4 import BeautifulSoup
import requests
# This is the inbuilt API of the microsoft for taking the speech 
engine=pyttsx3.init('sapi5')
# Simply capturing the voices in the list 
voices=engine.getProperty('voices')
# Setting male voice as the assistant voice 
engine.setProperty('voice',voices[0].id)

def speak(audio):
# Say is the function in engine which is used to say what we need
    engine.say(audio)
    engine.runAndWait()
    
def wish_me():
# Creating a function that wish a person
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak('Good morning')
    elif hour>=12 and hour<=18:
        speak('Good afternoon')
    else:
        speak('good evening')
    speak('I am 4 6 4 , I am here to help you')

def takeCommand():
    # This takes the microphone input from the user and returns string output
    recorder=sr.Recognizer() # This class is used to recognize the voice 
    with sr.Microphone() as source:
        print('Listening ...')
        # We can use energy_threshold to increase or decrease the sound of surroundings
        # press ctrl and click on the listen to get more details
        recorder.energy_threshold=430
        recorder.pause_threshold=1 # This is the attribute in the recognizer . This helps not to complete the whole phrase in 0.8 seconds which is default value
        audio = recorder.listen(source) # The sound captured by the source is stored in the audio

    try :
        print('Recognizing...')
        query = recorder.recognize_google(audio,language='en-in') # This function prints the result2 which is not required so i commented it out
        print(f'user said : {query}')
        
    except Exception as e :
        # print(e)
        speak('Say again please...')
        return None
    return query

# This avoids executing directly 
if __name__=='__main__':
    speak('hello')
    wish_me()
    while True:
        query=f'{takeCommand()}'
        if 'wikipedia' in query:
            speak('searching wikipedia...')
            query=query.replace('wikipedia','')
            result=wp.summary(query,sentences=2) # summary is used to search the result in the wikipedia
            print('According to wikipedia : ',result)
            speak('According to wikipedia :')
            speak(result)
        if 'open' in query and 'youtube' in query : wb.open('youtube.com')

        if 'open' in query and 'google' in query : wb.open('google.com')

        if 'open' in query and 'stackoverflow' in query : wb.open('stackoverflow.com')

        if 'open' in query and 'spotify' in query : wb.open('spotify.com')

        if 'quit' in query:
            if 'you' and ('well' or 'good') in query : speak('I am glad I helped you')
            speak('Thanks for your time')
            break

        if 'want' and 'typing speed' in query:
            speak('Shall i open typing test.com in microsoft edge')
            ans=takeCommand()
            if 'yes' in ans : wb.open('typingtest.com')

            else : speak('what can i do for you ?')

        if 'want' and 'problem' in query:
            if 'coding' in query:
                speak('continue your coding journey in codewars')
                wb.open('codewars.com')

        if 'time' in query:
            current_time=datetime.datetime.now().strftime('%H:%M:%S')
            speak(f'current time is {current_time}')

        if 'generate' and 'random' and 'numbers' in query:
            # This is used to generate random values to the give times
            print('the random numbers generated are : \n ',[random.randint(0,100) for i in range([i for i in query.split(' ') if i.isdigit()==True])])

        if 'find' and 'folder' in  query:
            print('The file will be checked in :',os.getcwd(),'as default else ')
            path = input('Enter the path that you required :')
            def display_folders(path):
                # This contains  the folder that are present in the current working directory
                folder = os.listdir(path)
                try:
                    for i in folder:
                            if os.path.isfile(i)==True : pass
                            else:
                                    print(i)
                                    # Again sending the path to same fucntion
                                    display_folders(path+f'/{i}')
                except:
                    print('The path is wrong')
            display_folders(path)

        if 'create' and 'folder' in query :
            path = input('Enter the name of the folder :')
            # Creating a single directory 
            os.mkdir(os.path.join(os.getcwd(),path))

        if 'read' and 'folder' in query :
            file = input('Enter the name of the folder :')
            # Reading the file using with statement
            with open('file.py','r') as file:
                file_content = file.read()
                print(file_content)

        if 'delete' and 'folder':
            file = input('Enter the name of the folder :')
            # os.path.join(os.getcwd(),file) is a optimzed path 
            os.remove(os.path.join(os.getcwd(),file))
            print(f'The {file} is deleted successfully')


        if 'database' in query:
            import mysql.connector
            # Establishing connection by using the mysql.connector.connect method 
            # my user is root password is 1234
            # Local host is host 
            # database is mydb
            connection = mysql.connector.connect(user='root',password='password', host='127.0.0.1', database='mydb')
            # Making a cursor to operate
            mycursor = connection.cursor()
            # Executing the SQL commands using execute function
            mycursor.execute('show database;')
        
        if 'HTML' and 'website':
            # Importing BS4 module  to extract the HTML
            # This is a direct one liner that take 6 line to write
            print(BeautifulSoup(requests.get(input('Enter url of the website')).content,'html.parser').prettify())
        
