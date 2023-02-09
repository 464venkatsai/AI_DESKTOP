# This module is used to deliver speech
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia as wp
import webbrowser as wb
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
        if 'open' in query and 'youtube' in query:
            wb.open('youtube.com')
        if 'open' in query and 'google' in query:
            wb.open('google.com')
        if 'open' in query and 'stackoverflow' in query:
            wb.open('stackoverflow.com')
        if 'open' in query and 'spotify' in query:
            wb.open('spotify.com')
        if 'quit' in query:
            if 'you' and ('well' or 'good') in query:
                speak('I am glad I helped you')
            speak('Thanks for your time')
            break
        if 'want' and 'typing speed' in query:
            speak('Shall i open typing test.com in microsoft edge')
            ans=takeCommand()
            if 'yes' in ans :
                wb.open('typingtest.com')
            else:
                speak('what can i do for you ?')
        if 'want' and 'problem' in query:
            if 'coding' in query:
                speak('continue your coding journey in codewars')
                wb.open('codewars.com')
        if 'time' in query:
            current_time=datetime.datetime.now().strftime('%H:%M:%S')
            speak(f'current time is {current_time}')

