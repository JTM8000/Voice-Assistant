import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

# Initialize speech recognizer and text-to-speech engine
r = sr.Recognizer()
engine = pyttsx3.init()

# Function to speak text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to recognize speech
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

        try:
            text = r.recognize_google(audio)
            print(f"You said: {text}")
            return text.lower()
        except sr.UnknownValueError:
            speak("Sorry, I didn't understand. Can you please repeat?")
        except sr.RequestError as e:
            speak(f"Sorry, there was an error: {e}")

# Function to set reminders
def set_reminder():
    speak("What would you like me to remind you about?")
    text = listen()
    if text:
        speak(f"Reminder set for {text}")
        # TODO: Use a library like schedule to schedule a reminder for a future time

# Function to create to-do list
def create_todo():
    speak("What would you like to add to your to-do list?")
    text = listen()
    if text:
        with open("todo.txt", "a") as f:
            f.write(f"- {text}\n")
        speak(f"{text} added to your to-do list")

# Function to search the web
def search_web():
    speak("What would you like to search for?")
    text = listen()
    if text:
        url = f"https://www.google.com/search?q={text}"
        webbrowser.open(url)
        speak(f"Here are the results for {text} on Google")

# Main loop
speak("Hi, how can I help you today?")
while True:
    text = listen()
    if text:
        if "reminder" in text:
            set_reminder()
        elif "to-do list" in text:
            create_todo()
        elif "search" in text:
            search_web()
        elif "stop" in text:
            speak("Goodbye!")
            break
