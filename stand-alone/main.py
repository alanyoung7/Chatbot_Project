import csv
import pyttsx3
import speech_recognition as sr
import time
import os.path
wordlist = []
# reading csv file for name and making a list of skill
with open('name.csv', encoding='utf-8-sig') as csv_file:
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
bit = 0
Answer = "None"
for i in wordlist:
	word = str(i)[2:-2]

	# starts text-to-speech process
	engine.say("Hey alexa, open " + word)   # Queue up things to say.
	engine.runAndWait()   # Flush the say() queue and play the audio
	# ends text-to-speech process 
	
	print("I am Listening.....")
	
	# starts speech-to-text process 
	start = time.time()
	with mic as source:

		# audio = r.record(source, offset = 0, duration=20)  
		audio = r.listen(source)  
	# output = r.recognize_google(audio)
	end = time.time()
	try:
		output = r.recognize_google(audio)
		total_time = end - start
		bit = 1
		Answer = "None"
		print(word, " - ", output, "\n")
	except sr.RequestError:
		output = "API Unavailable"
		print(output)
	except sr.UnknownValueError:
		total_time = 0
		output = "Could not recognize the voice!"
		print(output)
		# break
	# ends speech-to-text process
	
	# writing the skill name and the output from alexa to the csv file
	file_exists = os.path.isfile('output.csv')
	with open('output.csv', mode='a') as out:
		fieldnames = ['Skill Name', 'Description', 'Time', 'Bit', 'Answer']
		writer = csv.DictWriter(out, fieldnames=fieldnames, delimiter=',')
		if not file_exists:
			writer.writeheader()
		writer.writerow({'Skill Name': word, 'Description': output, 'Time': total_time, 'Bit': bit, 'Answer': Answer})





