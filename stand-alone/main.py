import csv
import pyttsx3
import speech_recognition as sr
import time

wordlist = []

# reading csv file for name and making a list of skill
with open('names.csv', encoding='utf-8-sig') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        wordlist.append(row)

# One time initialization for text-to-speech
engine = pyttsx3.init()

# Set properties _before_ you add things to say
engine.setProperty('rate', 160)    # Speed percent (can go over 100)
engine.setProperty('volume', 0.9)  # Volume 0-1

# One time initialization for speech-to-text
r = sr.Recognizer()
mic = sr.Microphone()
with mic as source: 
	r.adjust_for_ambient_noise(source)
print("Set minimum energy threshold to {}".format(r.energy_threshold))
for i in wordlist:
	word = str(i)[2:-2]

	# starts text-to-speech process
	engine.say("Hey alexa, open " + word)   # Queue up things to say.
	engine.runAndWait()   # Flush the say() queue and play the audio
	# ends text-to-speech process 
	
	print("I am Listening.....")
	
	# starts speech-to-text process 
	with mic as source:
		# audio = r.record(source, offset = 0, duration=20)  
		audio = r.listen(source)  

	output = r.recognize_google(audio)
	# ends speech-to-text process
	
	print(word, " - ", output, "\n")

	# writing the skill name and the output from alexa to the csv file
	with open('output.csv', mode='a') as out:
		writer = csv.writer(out, delimiter=',')
		writer.writerow([word, output])

	# time.sleep(20)
