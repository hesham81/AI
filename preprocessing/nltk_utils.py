import nltk
from nltk.stem.porter import PorterStemmer

# Initialize the stemmer
stemmer = PorterStemmer()
nltk.download('punkt')


# Tokenization function
def tokenize(sentence):
    return nltk.word_tokenize(sentence)  # Corrected spelling


def stem(word):
    return stemmer.stem(word.lower())


def bag_of_words(tokenized_sentence, all_words):
    """
    Creates a bag of words (one-hot encoding style) for a sentence.
    """
    tokenized_sentence = [stem(w) for w in tokenized_sentence]
    bag = [1 if word in tokenized_sentence else 0 for word in all_words]
    return bag


# Example usage
a = "How Long Does Shipping Take?"
print("Original sentence:", a)

a = tokenize(a)
print("Tokenized sentence:", a)
