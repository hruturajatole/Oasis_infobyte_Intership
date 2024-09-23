import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia

# Initialize the recognizer and TTS engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Function to speak text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to take voice input
def take_command():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

        try:
            print("Recognizing...")
            query = recognizer.recognize_google(audio, language='en-in')
            print(f"You said: {query}")
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            return "None"
        except sr.RequestError:
            print("Sorry, I'm having trouble connecting to the service.")
            return "None"
        
        return query.lower()

# Function to get current time
def tell_time():
    time = datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"The current time is {time}")

# Function to get current date
def tell_date():
    today = datetime.date.today()
    speak(f"Today's date is {today}")

# Main function for voice assistant
def voice_assistant():
    speak("Hello! How can I assist you today?")
    
    while True:
        command = take_command()

        if 'hello' in command:
            speak("Hello! How can I help you?")
        
        elif 'time' in command:
            tell_time()
        
        elif 'date' in command:
            tell_date()

        elif 'who is' in command or 'what is' in command:
            query = command.replace('who is', '').replace('what is', '')
            result = wikipedia.summary(query, sentences=2)
            speak(f"According to Wikipedia: {result}")
        
        elif 'stop' in command:
            speak("Goodbye!")
            break

if __name__ == "__main__":
    voice_assistant()