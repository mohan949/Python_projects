

# import speech_recognition as sr # type: ignore
# import webbrowser
# import pyttsx3


# recognizer = sr.Recognizer()
# engine = pyttsx3.init()

# print("speech_recognition module imported successfully")


# def speak(text):
#     engine.say(text)
#     engine.runAndWait()



# if __name__ == "__main__":
#     speak("Initializing Jarvis....")
#     while True:
#         # Listen for the wake word "Jarvis"
#         # obtain audio from the microphone
#         r = sr.Recognizer()
#         with sr.Microphone() as source:
#                 print("Listening...")
#                 audio = r.recognize_sphinx(source)


#         print("recognizing...")
#         try:
#         #  print('Jarvis thinks you said " ' + r.recognize_google(audio))
#          command = r.recognize_sphinx(audio)
#          print(command)
#         except Exception as e:
#             print("Error; {0}".format(e))
            
import speech_recognition as sr  # type: ignore
import webbrowser
import pyttsx3
import musicLibrary

recognizer = sr.Recognizer()
engine = pyttsx3.init()

print("speech_recognition module imported successfully")

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommmand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
        speak("Opening Google")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
        speak("Opening Youtube")
    elif "open github" in c.lower():
        webbrowser.open("XXXXXXXXXXXXXXXXXXXXXX")
        speak("Opening Github")
    elif c.lower().startswith("play"):
        # Extract the website name from the command
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)
        speak(f"Playing {song}")  
    elif "news"    
    else:
        speak("Sorry, I did not understand that. Please try again.")


if __name__ == "__main__":
    speak("Initializing Jarvis....")
    while True:
        # Listen for the wake word "Jarvis"
        with sr.Microphone() as source:
            print("Listening...")
            audio = recognizer.listen(source)  # Capture audio from the microphone

        print("Recognizing...")
        try:
            # Recognize speech change agent here down
            command = recognizer.recognize_google(audio)
            print(f"Jarvis thinks you said: {command}")
            # if 'jarvis' in command.lower():
            #     speak('Hello, I am Jarvis. How can I assist you?')
            # else:
            #     speak('Sorry, I did not understand that. Please try again.')

            processCommmand(command)
        except sr.UnknownValueError:
            speak("Sorry, Error ")
        except sr.RequestError as e:
            print(f"Could not request results from the speech recognition service; {e}")
        except Exception as e:
            print(f"Error: {e}")
 
        # n = input("Do you want to continue? (y/n): ")
        speak('say exit to Stop')
        if 'exit' in command.lower():
            break

            