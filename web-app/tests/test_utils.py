from utils import *

class Tests:
	def test_extract_first_sentence_1(self):
		text = 'hello, great. hi'
		result = extract_first_sentence(text)
		assert result == 'hello, great'

	def test_extract_first_sentence_2(self):
		text = 'hello, great'
		result = extract_first_sentence(text)
		assert result == 'hello, great'

	def test_extract_first_sentence_3(self):
		text = 'hello, great. hi. hello'
		result = extract_first_sentence(text)
		assert result == 'hello, great'