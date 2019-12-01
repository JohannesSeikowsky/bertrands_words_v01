# word extraction funcs
import os, enchant, nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer 

def all_words_from_file(file_path):
	text = open(file_path).read().lower()
	words = word_tokenize(text)

	# exclude very short words (hack)
	min_len = 3
	words = [word for word in words if len(word) > min_len]

	# check for english words
	en_gb_dict = enchant.Dict("en_GB")
	words = [word for word in words if en_gb_dict.check(word)] # check() method --> checks whether string contains an English word
	return words


def all_words_from_dir(dir_path):
	# get all words from all docs in bertrands_docs directory
	all_words = []
	for file_name in os.listdir(dir_path):
		try:
			file_path = dir_path + "/" + file_name
			words = all_words_from_file(file_path)
			all_words = all_words + words
		except:
			pass

	# exclude duplicates
	all_words = set(all_words)

	# lemmatize every word
	lemmatizer = WordNetLemmatizer() 
	all_words = [lemmatizer.lemmatize(word) for word in all_words]
	return all_words