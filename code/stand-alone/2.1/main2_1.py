import csv
import pyttsx3
import speech_recognition as sr
import time
import os.path

def readfile(fileIN):
	nameList = []
	with open(fileIN, encoding='utf-8-sig') as csv_file:  # reading csv file for name and making a list of skill
	    csv_reader = csv.reader(csv_file)
	    for row in csv_reader:
	        nameList.append(row)
	return nameList

def wrtie_to_file(fileOut):
	file_exists = os.path.isfile('output.csv')
	with open('output.csv', mode='a', newline='') as out:
		fieldnames = ['Skill Name', 'Description', 'Time', 'Bit', 'Answer']
		writer = csv.DictWriter(out, fieldnames=fieldnames, delimiter=',')
		if not file_exists:
			writer.writeheader()
		# writer.writerow({'Skill Name': skill, 'Description': output, 'Time': total_time, 'Bit': bit, 'Answer': Answer})
		writer.writerow({'Skill Name': fileOut[0], 'Description': fileOut[1], 'Time': fileOut[2], 'Bit': fileOut[3], 'Answer': fileOut[4]})

def fileexist(): 
	if os.path.isfile('output.csv'):
		print("file exists")
	else:
		with open('output.csv', mode='a', newline='') as out:
			fieldnames = ['Skill Name', 'Description', 'Time', 'Bit', 'Answer']
			writer = csv.DictWriter(out, fieldnames=fieldnames, delimiter=',')
			writer.writeheader()

def alexa_stop(sentence):
	# starts text-to-speech process
	engine.say("Hey alexa, " + sentence)   # Queue up things to say.
	engine.runAndWait()   # Flush the say() queue and play the audio
	# ends text-to-speech process

def text_to_speech(sentence):
	# starts text-to-speech process
	engine.say("Hey alexa, open " + sentence)   # Queue up things to say.
	engine.runAndWait()   # Flush the say() queue and play the audio
	# ends text-to-speech process

def tts_reply(reply):
	# starts text-to-speech process
	engine.say(reply)   # Queue up things to say.
	engine.runAndWait()   # Flush the say() queue and play the audio
	# ends text-to-speech process 

def speech_to_text(skill_name):
	start = time.time()
	with mic as source:
		# audio = r.record(source, offset = 0, duration=20)  
		audio = r.listen(source)  
	end = time.time()
	total_time = 0
	bit = 1	
	Answer = "None"
	try:
		output = r.recognize_google(audio)
		total_time = end - start
		bit = 1
		Answer = "None"
	except sr.RequestError:
		output = "API Unavailable"
	except sr.UnknownValueError:
		output = "Could not recognize the voice!"
	return [skill_name,output,total_time,bit,Answer] 

def checker(description,row_num):
	boolean = 1
	with open('output.csv', 'rt') as f:
		reader = csv.reader(f, delimiter=',')
		for row in reader:
			if description == row[row_num]:
				print("in checker ",description, row[row_num])
				boolean = 0
				break
			else:
				boolean = 1
	f.close()
	return boolean

def bit_checker(value, row_num):
	with open('output.csv', 'rt') as f:
		reader = csv.reader(f, delimiter=',')
		for row in reader:
			if row[row_num] == 'Bit':
				continue
			elif int(value) == int(row[row_num]):
				# print("in SECOND checker ", row[row_num])
				boolean = 0
				break
			else:
				boolean = 1
	f.close
	return boolean

def getAnswer(description,row_num):
	with open('output.csv', 'rt') as f:
		reader = csv.reader(f, delimiter=',')
		for row in reader:
			if description == row[row_num]:
				ans = row[4]
	f.close()
	return ans

def main():
	wordlist = readfile("name.csv")
	# print(wordlist)
	outputList = []
	for i in wordlist:
		word = str(i)[2:-2]

		# listen and store
		text_to_speech(word)
		print("I am Listening.....")
		textout = speech_to_text(word)
		# print(textout[0],textout[1],textout[2])
		# check if in file or not
		skill_check = checker(textout[0],0)
		description_check = checker(textout[1],1)
		bit_check = bit_checker(0, 3)
		
		while bit_check != 0:
			if skill_check == 1 and description_check == 1:
				wrtie_to_file(textout)
				skill_check = checker(textout[0],0)
				description_check = checker(textout[1],1)
			time.sleep(10)
			bit_check = bit_checker(0, 3)

		# print(skill_check, description_check, bit_check)
		# check for conditions
		if skill_check == 0 and description_check == 0 and bit_check == 0:
			text_to_speech(word)
			out_temp = speech_to_text(word)
			answer = getAnswer(textout[1], 1)
			tts_reply(answer)
			temp = speech_to_text(word)
			wrtie_to_file(temp)
		else:
			wrtie_to_file(textout) 
		# elif skill_check == 1 and description_check == 1 and bit_check == 1:
			# wrtie_to_file(textout)

		alexa_stop(" stop ")
		time.sleep(7)


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
fileexist()
main()



