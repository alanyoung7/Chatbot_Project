# CPSC 8580 project
# Text-to-speech implementation

import pyttsx3

# One time initialization
engine = pyttsx3.init()

# Set properties _before_ you add things to say
engine.setProperty('rate', 160)    # Speed percent (can go over 100)
engine.setProperty('volume', 0.9)  # Volume 0-1

# Queue up things to say.
engine.say("Hey Alexa, what is the weather like today?")

# Flush the say() queue and play the audio
engine.runAndWait()




##########################################################################
#Changing voice here
##########################################################################
# voices = engine.getProperty('voices')
# for voice in voices:
#     print("Voice:")
#     print(" - ID: %s" % voice.id)
#     print(" - Name: %s" % voice.name)
#     print(" - Languages: %s" % voice.languages)
#     print(" - Gender: %s" % voice.gender)
#     print(" - Age: %s" % voice.age)


    # Voice IDs pulled from engine.getProperty('voices')
# These will be system specific
# en_voice_id = "com.apple.speech.synthesis.voice.Alex"


# # Use female English voice
# engine.setProperty('voice', en_voice_id)
# engine.say('My name is Jeffrey')
# engine.runAndWait()