import os
from os.path import dirname, join
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import speech

class Tests:
		
	def test_1(self):
		output = speech.AudioText(1, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+'/tests/werent-you-listening.wav')
		assert output == "weren't you listening"
		
	def test_2(self):
		output = speech.AudioText(1, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+'/tests/we-need-to-have.wav')
		assert output == "we need to have a serious talk"
	
	def test_3(self):
		output = speech.AudioText(1, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+'/tests/youre-on-the-right-track.wav')
		assert output == "you're on the right track"
	
	def test_background_noise(self):
		output = speech.AudioText(1, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+'/tests/this-part-of-my-life-this-little-part-is-called-happiness.wav')
		assert output == "this part of my life this little part is called happiness"
	