#stopwords



from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

example_sentance = "This is an exmaple showing off stop word filtration."
stop_words = set(stopwords.words("english"))

words = word_tokenize(example_sentance)

filtered_sentence = []

for w in words:
	if w not in stop_words:
		filtered_sentence.append(w)

print(filtered_sentence)