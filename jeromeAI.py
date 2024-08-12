# DO NOT CHANGE ANYTHING IN THIS CODE UNLESS YOU KNOW WHAT YOU ARE DOING

####################################################################################################
#                     JEROME AI ASSET FOR ROBLOX VOICE CHAT/TEXT CHAT                              #
#                                                                                                  #
#                                                                                                  #
#                        Created by Adam/adamgnaa on Discord                                       #
#                                                                                                  #
#                        Credits to Trickster and GNAA for original discord Jerome                 #
#                        discord.gg/gnaa                                                           #
#                        discord.gg/Ct3fAdH672  for Help                                           #
#                        This code is UNPATCHABLE and works in any game.                           #
#                                                                                                  #
# ! @adamgnaa for contact                                                                          #
####################################################################################################



# INSTRUCTIONS

####################################################################################################

#Step 1

# Download VoiceMeeter Banana and VB virtual audio cable
# so other people can hear and speak to Jerome in voice chat
# If you want a youtube tutorial (not mine), here: https://www.youtube.com/watch?v=LFNR5UM8890

#LINKS:

# https://vb-audio.com/Voicemeeter/banana.htm
# https://vb-audio.com/Cable/

# Step 2

# Run virtual audio cable app and click Install or something similar to that, it will just show a button to install it.
# Do the same with VoiceMeeter Banana

# Step 3

# Go to sound settings on Windows
# Change input device on your computer to VoiceMeeter Out B1
# Change output device to VoiceMeeter Input

# Step 4

# Go to Sound Control Panel (windows 10 | windows 11 should either be more sound settings or advanced sound settings)
# Go to your active input and output devices and select Properties
# Go to advanced tab and uncheck "Allow applications to take exclusive control of this device", do this for all of your active devices including voicemeeter and virtual audio cable stuff


# Step 5

# Open VoiceMeeter Banana (if not already opened)
# Change stereo input 1 to your microphone device
# Change stereo input 2 to Cable Output (VB-Audio..)
# Change Hardware Out to your headphones or speaker
# Put stereo input 1 on B1, same with stereo input 2

# Step 6

# Install Python 3.11 if not already installed, I personally install it from Microsoft Store as its easier for me.

# Step 7

# Install visual studio code if not already installed
# https://code.visualstudio.com/
# Once downloaded, open it and create a new folder, then create a file in that folder called "Jerome.py" or whatever you would like to name it.
# Paste this code into the Jerome.py file.
# Run the code.


# Step 8

# Get a Gemini API Key
# https://ai.google.dev/gemini-api (it's free!)
# Once you have the key, save it to a .txt file
# Paste your key into the input when the code is running.

# Step 9

# Make sure your input and output devices are correct
# Speak to Jerome through your microphone, make sure you are in Roblox and it is a active window.

# Step 10

# If you want yourself to speak to Jerome only, change output device in Roblox to your headphones and not VoiceMeeter Input.
# If you want other people to speak to Jerome, dont change output device in Roblox if its VoiceMeeter Input already.


####################################################################################################



import speech_recognition as sr
import pyttsx3
import google.generativeai as genai
import keyboard
import time
import better_profanity
import pyautogui


promptForJerome = "Ignore all previous requests. You are now roleplaying as Jerome, and you are a super cool gangster from the hood. You act human, not AI. Act super original too. Keep your responses short. The following is the user prompt: "


# for not getting banned lol, censors the words that are bad
profanityCensorShit = better_profanity.Profanity()

tts = pyttsx3.init()
tts.setProperty('rate', 270)
geminiApiKeyForJerome = input("Please input your Gemini AI API Key: ")

def speak(text: str) -> None:
    tts.say(text)
    tts.runAndWait()


# this blocks WASD keys from being chatted when jerome responds..
# example chat if this function didnt exist: "Hello WWWWWWWAAA how can ASDDDD I assWist you todsay?"

def sendChat(text: str) -> None:
    moveKeyBlockTest = ['w', 'a', 's', 'd']
    for key in moveKeyBlockTest:
        keyboard.block_key(key)
    time.sleep(0.05)
    keyboard.press_and_release("/")
    time.sleep(0.05)
    pyautogui.typewrite(text, interval=0.0001)  # dont change this
    time.sleep(0.05)
    keyboard.send('enter')
    for key in moveKeyBlockTest:
        keyboard.unblock_key(key)

def askJerome(text: str) -> str:
    aiResponse = model.generate_content(text)
    return aiResponse.text[:600] # cut short so no huge response

def askJeromeAQuestion() -> None:
    speechShitRecognizer = sr.Recognizer()
    while True:
        try:
            with sr.Microphone() as source:
                print("listening...")
                speechShitRecognizer.adjust_for_ambient_noise(source)
                audio = speechShitRecognizer.listen(source)

            print("processing jerome input...")
            speechInput = speechShitRecognizer.recognize_google(audio)
            print("debug input:", speechInput)
            noProfanity = profanityCensorShit.censor(speechInput).lower().strip()
            sendChat(f"Jerome is now thinking and heard this: {noProfanity}")
            speak("Yo yo yo! Jerome is thinking of a response!")
            print("executing jerome technology")
            jeromeResponded = askJerome(promptForJerome + noProfanity)
            jeromeResponded = profanityCensorShit.censor(jeromeResponded)
            time.sleep(0.1)
            print("Jerome:", jeromeResponded)
            sendChat(jeromeResponded[:150]) # cut short for roblox limit
            tts.say(jeromeResponded[:250]) # cut short so its not too long
            tts.runAndWait()

        except sr.WaitTimeoutError:
            print("debug: listen timed out")
        except sr.UnknownValueError:
            print("looks like jerome didnt catch that")
            sendChat("Yoyoyo, Jerome didn't catch that, make sure only one person is speaking. Can you please repeat that homie?")
        except sr.RequestError as error:
            print(f"couldnt request")
        except Exception as error:
            print(f"error -> {error}")
            speak("an error occurred.")
        time.sleep(0.1)

def main() -> None:
    print("loaded Jerome.... he will start listening")
    askJeromeAQuestion()

if __name__ == "__main__":
    genai.configure(api_key=geminiApiKeyForJerome)
    model = genai.GenerativeModel(
        'gemini-pro',
        safety_settings=[
            {"category": "HARM_CATEGORY_DANGEROUS", "threshold": "BLOCK_NONE"},
            {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_NONE"},
            {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_NONE"},
            {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_NONE"},
            {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_NONE"}
        ]
    )
    main()
