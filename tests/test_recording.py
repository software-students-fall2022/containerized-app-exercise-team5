import pytest
from speechRecognition import speech-recognition

class Tests:
		
	def test_question(self):
		output = speech-recognition.AudioText(1, 'werent-you-listening.wav')
		assert output == "Did you say  weren't you listening"