import nltk
nltk.download('subjectivity')
nltk.download('vader_lexicon')
from nltk.classify import NaiveBayesClassifier
from nltk.tokenize import sent_tokenize
from nltk.corpus import subjectivity
from nltk.sentiment import SentimentAnalyzer
from nltk.sentiment.util import *
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# input: uncleaned up paragraph of many sentences
# output: a single integer representing 10 for positive, -10 for negative, and 0 for neutral.

def analyze_sentiment(paragraph):
	n_instances = 100
	subj_docs = [(sent, 'subj') for sent in subjectivity.sents(categories='subj')[:n_instances]]
	obj_docs = [(sent, 'obj') for sent in subjectivity.sents(categories='obj')[:n_instances]]

	train_subj_docs = subj_docs[:80]
	test_subj_docs = subj_docs[80:100]
	train_obj_docs = obj_docs[:80]
	test_obj_docs = obj_docs[80:100]
	training_docs = train_subj_docs+train_obj_docs
	testing_docs = test_subj_docs+test_obj_docs
	sentim_analyzer = SentimentAnalyzer()
	all_words_neg = sentim_analyzer.all_words([mark_negation(doc) for doc in training_docs])

	unigram_feats = sentim_analyzer.unigram_word_feats(all_words_neg, min_freq=4)
	sentim_analyzer.add_feat_extractor(extract_unigram_feats, unigrams=unigram_feats)

	training_set = sentim_analyzer.apply_features(training_docs)
	test_set = sentim_analyzer.apply_features(testing_docs)

	trainer = NaiveBayesClassifier.train
	classifier = sentim_analyzer.train(trainer, training_set)

	sid = SentimentIntensityAnalyzer()
	total_sum = 0
	count = 0.0

	sentences = sent_tokenize(paragraph)

	for sentence in sentences:
		total_sum += sid.polarity_scores(sentence)["compound"]
		count+=1

	return total_sum*10/count