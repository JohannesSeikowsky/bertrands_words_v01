# utils
from wordfreq import word_frequency
from collections import OrderedDict
import pickle, os

def sort_by_val(in_dict):
	out_dict = sorted(in_dict.items(), key=lambda x: x[1])
	return out_dict


def get_word_freqs(words):
	word_freqs =  {}
	for word in words:
		word_freq = word_frequency(word, "en")
		word_freqs[word] = word_freq

	word_freqs = sort_by_val(word_freqs)
	return word_freqs


def create_pickle(pickle_file, to_pickle):
	file = open(pickle_file, "wb")
	pickle.dump(to_pickle, file)
	file.close()