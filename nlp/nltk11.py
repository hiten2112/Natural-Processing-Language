#Text Classification
#word as Features
#Naive Bayes Algorithm
#based on positive and negative text


import nltk
import random
from nltk.corpus import movie_reviews

documents = [(list(movie_reviews.words(fileid)),category)
				for category in movie_reviews.categories()
				for fileid in movie_reviews.fileids(category)]

#documents = []

#for category in movie_reviews.categories():
#		for fileid in movie_reviews.fileids(category):
#			documents.append(list(movie_reviews.words(fileid)),category)

random.shuffle(documents)

#print(documents[1])

all_words = []
for w in movie_reviews.words():
	all_words.append(w.lower())

all_words = nltk.FreqDist(all_words) #freq distribution

#print(all_words.most_common(15))
#print(all_words["stupid"])  #number of stupid word in all words

word_features = list(all_words.keys())[:3000]

def find_features(document):
	words = set(document)
	features = {}
	for w in word_features:
		features[w] = (w in words)
	return features

print((find_features(movie_reviews.words('neg/cv000_29416.txt'))))

featuresets = [(find_features(rev), category) for (rev, category) in documents]

#naive bayes algorithm
training_set =featuresets[:1900]
testing_set = featuresets[1900:]


classifier = nltk.NaiveBayesClassifier.train(training_set)
print("Naive Bayes Algo Accuracy percent :",(nltk.classify.accuracy(classifier, testing_set))*100 )
classifier.show_most_informative_features(15)