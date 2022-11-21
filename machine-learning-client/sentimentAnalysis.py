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
            sent_label = "Positive"
        else:
            sent_label = "Negative"
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


# example usage
x = SentimentAnalysis("text = 'I had a really horrible day. It was the worst day ever! But every now and then I have a really good day that makes me happy.")
print(x.sentiment())
print(x.positiveWords())
print(x.negative_words())

# pip install -U spacy
# pip install spacytextblob
# python -m textblob.download_corpora
# python -m spacy download en_core_web_sm