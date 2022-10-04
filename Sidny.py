Sure, I Do Need You. (SIDNY)
import pyttsx3 #importing text-to-speech package
import datetime #importing date and time package
import speech_recognition as sr #importing google speech recognition services as 'sr' for convenience 
import wikipedia #importing wikipedia package
import webbrowser #importing the browser package
import os #importiing os library
# import yagmail #importing smtp gmail client library

engine = pyttsx3.init('sapi5') #inintializing sapi5 
voices= engine.getProperty('voices') #getting details of the current voice
engine.setProperty('voice', voices[0].id) #selecting the current voice

def speak(audio): #defining a speak function
    engine.say(audio) #adding utterance to speak 
    engine.runAndWait() #to make the speech audible

def greet(): #defining a greet function
    hour = int(datetime.datetime.now().hour)
    if hour>=3 and hour<12:
        speak("Good Morning!")

    elif hour >=12 and hour<18:
        speak("Good Afternoon!")  

    else:
        speak('Good Evening!')

    speak("Sidny at your service sir!") 

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1   
        audio = r.listen(source)
    
    try:
        print('Interpreting...')
        query = r.recognize_google(audio, language='en-in')
        print(f'user response: {query}\n')

    except Exception as e:
        # print(e)
        print('No voice detected.')
        return"None"
    return query

# sender_email =  "s****a@gmail.com"
# receiver_email = []
# subject = ''
# sender_password = input(f'Enter password for {sender_email}:n') 

if __name__ == "__main__":
    greet()
    while True:

        query = takeCommand().lower()
        #  logic based execution via query

        if 'wikipedia' in query:
            speak("Searching wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak('According to wikipedia')
            print(results)
            speak(results)

        elif 'search' in query:
            webbrowser.open('google.com') 
            speak("Accessing google homepage sir.")

        elif 'college dashboard' in query:
            webbrowser.open('lms.sssihl.edu.in')
            speak("Here are your undergraduate courses sir.") 

        elif 'courses' in query:
            webbrowser.open('udemy.com')
            speak("Accessing your udemy courses sir.") 

        elif 'weather' in query:
            webbrowser.open('https://www.google.com/search?rlz=1C1JZAP_enIN916&sxsrf=ALeKk00UwcPJ0XPHeya5FR32Hb5GO6m5Ng%3A1598536025653&ei=WblHX_jCJ9Dez7sP5rO14Ac&q=weather+right+now&oq=weather+right+now&gs_lcp=CgZwc3ktYWIQAzIKCAAQsQMQRhCAAjICCAAyAggAMgIIADICCAAyAggAMgIIADICCAAyAggAMgIIADoHCAAQRxCwAzoHCCMQ6gIQJzoECCMQJzoKCAAQsQMQgwEQQzoECAAQQzoNCAAQsQMQgwEQFBCHAjoFCAAQkQI6CggAELEDEBQQhwI6AgguOggIABCxAxCDAToFCAAQsQM6CAguEMcBEK8BOgQIABAKOg8IABCxAxAUEIcCEEYQgAJQ2VxYtHhg2XloAnAAeACAAX-IAZwNkgEEMTAuN5gBAKABAaoBB2d3cy13aXqwAQrAAQE&sclient=psy-ab&ved=0ahUKEwi40-DfwrvrAhVQ73MBHeZZDXwQ4dUDCA0&uact=5')
            speak("Accessing your request sir!")

        elif 'youtube' in query:
            webbrowser.open('youtube.com') 
            speak("Opening youtube sir.") 

        elif 'google meet' in query:
            webbrowser.open('meet.google.com') 
            speak("Sure sir, here it is.")   
        
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, it is {strTime}")

        elif 'books' in query:
            codePath = "D:\\BSc. 3rd semester resources"
            os.startfile(codePath)
            speak("Listing your digital books sir.")

        elif 'spotify' in query:
            codePath = "C:\\Users\\SaiAnkith\\AppData\\Roaming\\Spotify\\Spotify.exe"
            os.startfile(codePath)
            speak("Yes sir.")

        elif 'physics classroom' in query:
            webbrowser.open('meet.google.com/gjk-efgt-zru')
            speak("Sure sir, here it is.")    

        elif 'chemistry classroom' in query:
            # webbrowser.open('meet.google.com/vue-qzmu-bpo')
            speak("Sure sir, here it is.")

        elif 'math one classroom' in query:
            webbrowser.open('meet.google.com/vue-qzmu-bpo')
            speak("Sure sir, here it is.")

        elif 'math two classroom' in query:
            webbrowser.open('meet.google.com/vue-qzmu-bpo')
            speak("Sure sir, here it is.")  

        elif 'molecular spectroscopy' in query:
            webbrowser.open('https://lms.sssihl.edu.in/course/view.php?id=86')
            speak("Sure sir, here it is.")  
    
    
        '''elif 'send email' in query:
            try:
                yag = yagmail.SMTP(user = 's***a@gmail.com', password = sender_password)
                content = [
                   'write content, add paths to images/videos/content']

                yag.send(receiver_emails, subject, contents)

            except Exception as e:
                print(f"Error sending the email.")  
                speak("Sorry sir the email couldn't be sent.")'''
        break


