import spacy
from spacytextblob.spacytextblob import SpacyTextBlob

class SentimentAnalysis:
    def __init__(self, text):
        nlp = spacy.load('en_core_web_sm')
        nlp.add_pipe('spacytextblob')
        self.doc = nlp(text)
    
    def sentiment(self):
        sentiment = self.doc._.blob.polarity
        sentiment = round(sentiment,2)
        if sentiment > 0:
            sent_label = True
        else:
            sent_label = False
        return sent_label
    
    def positiveWords(self):
        positive_words = []
        for x in self.doc._.blob.sentiment_assessments.assessments:
            if x[1] > 0:
                positive_words.append(' '.join(x[0]))
            else:
                pass
        return positive_words
    
    def negative_words(self):
        negative_words = []
        for x in self.doc._.blob.sentiment_assessments.assessments:
            if x[1] < 0:
                negative_words.append(' '.join(x[0]))
            else:
                pass
        return negative_words

