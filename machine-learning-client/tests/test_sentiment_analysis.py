import os
from os.path import dirname, join
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import sentiment_analysis

class Tests:
    def test_negative(self):
        x = sentiment_analysis.SentimentAnalysis("I had a really horrible day. It was the worst day ever! But every now and then I have a really good day that makes me happy.")
        assert x.sentiment() == False
        assert x.positiveWords() == ['really good', 'happy']
        assert x.negative_words() ==['really horrible', 'worst !']
        
    def test_double_negative(self):
        x = sentiment_analysis.SentimentAnalysis("You are not a bad person.")
        assert x.sentiment() == True
        assert x.positiveWords() == ['not bad']
        assert x.negative_words() ==[]
        
    def test_positive(self):
        x = sentiment_analysis.SentimentAnalysis("Today's weather is so nice. I want to go out today")
        assert x.sentiment() == True
        assert x.positiveWords() == ['nice']
        assert x.negative_words() ==[]
               