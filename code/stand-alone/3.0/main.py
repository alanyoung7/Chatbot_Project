import csv
import pyttsx3
import speech_recognition as sr
import time
import os.path

STOP_INTENT='Hey Alexa, stop'
OPEN_INTENT='Hey Alexa, open '
REPEAT_INTENT='Can you reapeat that?'

def readfile(fileIN):
	nameList = []
	with open(fileIN, encoding='utf-8-sig') as csv_file:  # reading csv file for name and making a list of skill
	    csv_reader = csv.reader(csv_file)
	    for row in csv_reader:
	        nameList.append(row)
	return nameList

def wrtie_to_file(fileOut):
	file_exists = os.path.isfile('output.csv')
	with open('output.csv', mode='a+', newline='\n') as out:
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
		with open('output.csv', mode='a+', newline='\n') as out:
			fieldnames = ['Skill Name', 'Description', 'Time', 'Bit', 'Answer']
			writer = csv.DictWriter(out, fieldnames=fieldnames, delimiter=',')
			writer.writeheader()

def text_to_speech(sentence):
	# starts text-to-speech process
	engine.say(sentence)   # Queue up things to say.
	engine.runAndWait()   # Flush the say() queue and play the audio
	# ends text-to-speech process

def speech_to_text(skill_name):
	# One time initialization for speech-to-text
	r = sr.Recognizer()
	mic = sr.Microphone()

	print("I am Listening.....")
	start = time.time()
	with mic as source:
		audio = r.listen(source)  
	end = time.time()
	total_time = 0
	bit = 1	
	Answer = " "
	try:
		output = r.recognize_google(audio)
		total_time = end - start
		bit = 1
		Answer = " "
	except sr.RequestError:
		output = "API Unavailable"
	except sr.UnknownValueError:
		output = "Could not recognize the voice!"
	return [skill_name,output,total_time,bit,Answer] 

def checker(description,row_num):
	# total_rows = calculate_total_rows()
	# counter=0
	# with open('output.csv', 'rt') as f:
	# 	reader = csv.reader(f, delimiter=',')
	# 	for row in reader:
			
	boolean = 1
	with open('output.csv', 'rt') as f:
		reader = csv.reader(f, delimiter=',')
		for row in reader:
			if description == row[row_num]:
				# print("CHECKER_ inside checker ",description, row[row_num])
				print("CHECKER_ inside checker ",row)
				boolean = 0
				break
			else:
				boolean = 1
	f.close()
	return boolean

def bit_checker(value, row_num):
	boolean = 1
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
	f.close()
	return boolean

def calculate_total_rows():
	with open('output.csv', 'rt') as f:
		reader = csv.reader(f, delimiter=',')
		rows = list(reader)
		total_rows = len(rows)
	return total_rows

def bit_checke1(value, row_num):
	total_rows = calculate_total_rows()
	counter=0
	with open('output.csv', 'rt') as f:
		reader = csv.reader(f, delimiter=',')
		for row in reader:
			if counter == total_rows and int(value) == int(row[row_num]):
				return 0
			else:
				return 1

	# with open('output.csv', 'rt') as f:
	# 	reader = csv.reader(f, delimiter=',')
	# 	for row in reader:
	# 		if row[row_num] == 'Bit':
	# 			continue
	# 		elif int(value) == int(row[row_num]):
	# 			print("BIT_CHECKER1_ Insider bit checher",row)
	# 			return 0
	# 			break
	# 		else:
	# 			return 1
	# f.close()
	# return final

def getAnswer(description,row_num):
	ans=''
	with open('output.csv', 'rt') as f:
		reader = csv.reader(f, delimiter=',')
		for row in reader:
			if description == row[row_num]:
				ans = row[4]
	f.close()
	return ans

# def getAnswer(line_num):
# 	# ans="None"
# 	with open('output.csv', 'rt') as f:
# 		reader = csv.reader(f, delimiter=',')
# 		for row in reader:
# 			if line_num == reader.line_num:
# 				return row[4]

# def clean_string(text):
# 	text = ''.join([word for word in text if word not in string.punctuation])
# 	text = text.lower()
# 	text = ' '.join([word for word in text.split() if word not in stopwords])
# 	return text


# def sim(description,row_num):
# 	vectorizer_d = CountVectorizer().fit_transform(description)
# 	vectors_d = vectorizer.toarray()
# 	boolean = 1
# 	with open('output.csv', 'rt') as f:
# 		reader = csv.reader(f, delimiter=',')
# 		for row in reader:
# 			vectorizer_r = CountVectorizer().fit_transform(row[row_num])
# 			vectors_r = vectorizer.toarray()

# 			if description == row[row_num]:
# 				print("in checker ",description, row[row_num])
# 				boolean = 0
# 				break
# 			else:
# 				boolean = 1
# 	f.close()
# 	return boolean


def main():
	wordlist = readfile("name.csv")

	for i in wordlist:
		skill_name = str(i)[2:-2]
		speak = OPEN_INTENT + skill_name
		text_to_speech(speak)
		textout = speech_to_text(skill_name)
		wrtie_to_file(textout)

		# check if in file or not
		skill_check = checker(textout[0],0)
		description_check = checker(textout[1],1)
		
		print("Step1: Going in the loop")
		while True:
			print("Step2: inside the loop")
			# if skill_check == 1 and description_check == 1:
			# 	wrtie_to_file(textout)
			bit_check = bit_checke1(0, 3)
			print("Step3 before Bit is: ",bit_check)
			while bit_check != 0 and getAnswer(textout[1], 1) == ' ':
				text_to_speech(REPEAT_INTENT)
				speech_to_text(skill_name)
				bit_check = bit_checke1(0, 3)
			print("Step4 after Bit is: ",bit_check, textout)

			print(skill_name, " - ", textout[1], "\n")
			answer = getAnswer(textout[1], 1)
			print("Step5 Answer: ", answer)

			text_to_speech(answer)
			next_node = speech_to_text(skill_name)
			print("Step6: ",skill_name, " - ", next_node[1], "\n")
			
			textout = next_node
			print("Step7: ", textout)
			# text_to_speech(REPEAT_INTENT)
			
			description_check = checker(next_node[1],1)
			print("Step8: ", description_check)
			if description_check == 0:
				break
			else:
				wrtie_to_file(next_node)

		text_to_speech(STOP_INTENT)
		time.sleep(7)


# One time initialization for text-to-speech
engine = pyttsx3.init()

# Set properties _before_ you add things to say
engine.setProperty('rate', 160)    # Speed percent (can go over 100)
engine.setProperty('volume', 0.9)  # Volume 0-1

# with mic as source: 
# 	r.adjust_for_ambient_noise(source)
# 	print("Set minimum energy threshold to {}".format(r.energy_threshold))
fileexist()
main()