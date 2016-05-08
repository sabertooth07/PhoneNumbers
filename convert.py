import argparse
import re

# Dictionary to represent number to alphabet mapping
number_to_alpha_dict={
	'1': ['1'],
	'2': ['a', 'b', 'c'],
	'3': ['d', 'e', 'f'],
	'4': ['g', 'h', 'i'],
	'5': ['j', 'k', 'l'],
	'6': ['m', 'n', 'o'],
	'7': ['p', 'q', 'r', 's'],
	'8': ['t', 'u', 'v'],
	'9': ['w', 'x', 'y', 'z']
}

# Global variable that stores all wors in a dictionary
dictionary_words_list=[]

def is_word(word):
	"""
	Method reads dictionary and checks if a given word is in the dictionary
	Input parameter(s): word<str>
	Return(s): <bool>
	"""
	global dictionary_words_list
	if dictionary_words_list == []:
		with open(args.d, "rb") as fobj:
			dictionary_words_list=fobj.read().splitlines()

	if word in dictionary_words_list:
		return True
	else:
		return False
	

def rec_method(remaining, processed):
	"""
	Method recursively generates every possible word from a given number
	Input parameter(s):
	1. substring of number to be processed <str>
	2. substring of number already processed <str>
	"""
	if len(remaining) == 0:
		if is_word(processed):
			print processed
	else:
		pot_alpha_list=number_to_alpha_dict.get(remaining[0])
		for alpha in pot_alpha_list:
			rec_method(remaining[1:], processed+alpha)


parser = argparse.ArgumentParser()
parser.add_argument("-d", required=True)
parser.add_argument("-n", required=True)
args=parser.parse_args()

number=args.n

# regex to check for a noticable pattern
pattern = re.compile('[0-9].*')
if not pattern.match(number):
	print "Please only use numbers and . eg: 1.800.123.123"
	exit(1)

# Skip first 6 digits if number start with 1.800
if number.startswith("1.800."):
	number=number[6:]

for counter,num in enumerate(number.split(".")):
	print "Possible words for digit string "+str(counter+1)
	rec_method(num, "")
