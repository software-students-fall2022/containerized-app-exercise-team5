# Python program to translate
# speech to text and text to speech
 
 
import speech_recognition as sr
import pyttsx3
import sys
# Initialize the recognizer
r = sr.Recognizer()
 
# Function to convert text to
# speech
def SpeakText(command):
     
    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()
     
        
# Loop infinitely for user to
# speak
def AudioText(int, string):
	#print(string);
	#var audio;
	if (int == 0):
		while(1):   
	 
			# Exception handling to handle
			# exceptions at the runtime
			#try:
		 
				# use the microphone as source for input.
				with sr.Microphone() as source2:
			 
					# wait for a second to let the recognizer
					# adjust the energy threshold based on
					# the surrounding noise level
					r.adjust_for_ambient_noise(source2, duration=0.2)
			 
					#listens for the user's input
					audio = r.listen(source2)
	else:
		##filename = "werent-you-listening.wav"
		with sr.AudioFile(string) as source:
			# listen for the data (load audio to memory)
			audio = r.record(source)	 
		 
				# Using google to recognize audio
	MyText = r.recognize_google(audio)
	MyText = MyText.lower()

	print(MyText)
	#SpeakText(MyText)
	return MyText;
		#except sr.RequestError as e:
			#print("Could not request results; {0}".format(e))
		 
		#except sr.UnknownValueError:
			#print("unknown error occurred")


