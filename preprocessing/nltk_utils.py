import nltk
from nltk.stem.porter import PorterStemmer

# Download the 'punkt_tab' resource if not already present
nltk.download('punkt_tab')
nltk.download("punkt")

stemmer = PorterStemmer()

def tokenize(sentence):
  return nltk.word_tokenize(sentence)

def stem(word):
 return stemmer.stem(word.lower())

def bag_of_words(tokenized_sentence, all_words):
  # tokenized_sentence = [stem(w) for w in tokenized_sentence]
  pass


a = "How Long Does  shipping take ? "
print(a)
a = tokenize(a)
print(a)