import os
from os.path import dirname, join
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import sentiment_analysis

class Tests:
    def testNegative(self):
        x = sentiment_analysis.SentimentAnalysis("I had a really horrible day. It was the worst day ever! But every now and then I have a really good day that makes me happy.")
        assert x.sentiment() == False
        # assert x.positiveWords() == ['really good', 'happy']
               
# pipenv shell
# pipenv install pytest
# pipenv install spacy
# pipenv install spacytextblob
# python -m textblob.download_corpora
# python -m spacy download en_core_web_sm