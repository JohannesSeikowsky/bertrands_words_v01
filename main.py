# Bertrands words 2
import pickle, random, os
from nltk.corpus import wordnet
from word_extraction import all_words_from_dir
from datetime import *

from utils import *
from email_utils import send_email


# read in from pickle
f = open(os.environ['PATH_TO_CODE'] + "bertrands_words.pickle", "rb")
word_freqs = pickle.load(f)
f.close()


# user settings
set_number = 15
set_range = "1-20"


# get the words in relevant range
def parse_range(range):
	return [int(each) for each in range.split("-")]
range_low_end, range_high_end = parse_range(set_range)

lower_bound = round(len(word_freqs) / 100 * range_low_end)
upper_bound = round(len(word_freqs) / 100 * range_high_end)

words = word_freqs[lower_bound:upper_bound]


# choose the set_number of randomly chose words from the word range
random_indexes = random.sample(range(0, len(words)), set_number)
chosen_words = [words[each][0] for each in random_indexes]


# get definitions and examples of chosen words
# compose and send Email based on them
email_subject = "Bertrands Words Training"
email_content = ""

for word in chosen_words:
	try:
		word_synset = wordnet.synsets(word)[0]
		word_definition = word_synset.definition()

		word_definition = word + " - " + word_definition + "\n"
		email_content += word_definition 

		if len(word_synset.examples()) >= 1:
			word_expample = word_synset.examples()[0]
			word_expample = "e.g. " + word_expample + "\n"
			email_content += word_expample

		email_content += "\n"
	except:
		pass

send_email(email_subject, email_content)