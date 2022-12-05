import os
from os.path import dirname, join
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import speech

sys.path.append("/test")

class Tests:
		
	def test_1(self):
		print(sys.path)
		output = speech.AudioText(1, 'werent-you-listening.wav')
		assert output == "weren't you listening"
		
	def test_2(self):
		output = speech.AudioText(1, 'we-need-to-have.wav')
		assert output == "we need to have a serious talk"
	
	def test_3(self):
		output = speech.AudioText(1, 'youre-on-the-right-track.wav')
		assert output == "you're on the right track"
	
	def test_background_noise(self):
		output = speech.AudioText(1, 'this-part-of-my-life-this-little-part-is-called-happiness.wav')
		assert output == "this part of my life this little part is called happiness"
	