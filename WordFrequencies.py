import nltk
import string
from nltk.tokenize import sent_tokenize, word_tokenize

# input: an uncleaned paragraph (string)
# output: a cleaned dictionary of frequencies

stop_list = nltk.corpus.stopwords.words("english")
punctuation_list = string.punctuation

def get_good_words(paragraph):
	sentences = sent_tokenize(paragraph)
	word_dict = []
	good_words = []

	for sentence in sentences:
		word_list = word_tokenize(sentence)
		for word in word_list:
			word_dict.append(word.lower())

	for word in word_dict:
		if word not in stop_list and word not in punctuation_list:
			good_words.append(word)

	return good_words

def word_frequencies(paragraph):
	word_list = get_good_words(paragraph)

	freq_dict = {}

	for word in word_list:
		if word in freq_dict:
			freq_dict[word]+=1
		else:
			freq_dict[word] = 1

	return freq_dict