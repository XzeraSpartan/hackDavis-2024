import nltk
from nltk.tokenize import sent_tokenize

# Ensure that the necessary NLTK data is downloaded
<<<<<<< Updated upstream
# nltk.download('punkt')
=======
nltk.download('punkt')
>>>>>>> Stashed changes
def divide(text):
    return list(sent_tokenize(text))


