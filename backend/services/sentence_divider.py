import nltk
from nltk.tokenize import sent_tokenize

# Ensure that the necessary NLTK data is downloaded
# nltk.download('punkt')
def divide(text):
    return list(sent_tokenize(text))


