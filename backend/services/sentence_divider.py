import nltk
from nltk.tokenize import sent_tokenize

# Ensure that the necessary NLTK data is downloaded
#nltk.download('punkt')

# Path to the text file
file_path = 'test.txt'

# Read the text from the file
with open(file_path, 'r', encoding='utf-8') as file:
    text = file.read()

# Tokenize the text into sentences
sentences = sent_tokenize(text)


AI = []
user = []
i = 0
for sentence in sentences:
    AI.append(sentence) if i%2==0 else user.append(sentence)
    i+=1

for i in range((len(AI)+len(user))//2):
    print("AI:", AI[i])
    print("User:", user[i])
    print()
    print()
# Print the list of sentences
#print(sentences)
