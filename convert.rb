#!/usr/bin/env ruby
require 'optparse'

# Dictionary to represent number to alphabet mapping
$number_to_alpha_dict={
	'0'=> ['0'],
	'1'=> ['1'],
	'2'=> ['2', 'a', 'b', 'c'],
	'3'=> ['3', 'd', 'e', 'f'],
	'4'=> ['4', 'g', 'h', 'i'],
	'5'=> ['5', 'j', 'k', 'l'],
	'6'=> ['6', 'm', 'n', 'o'],
	'7'=> ['7', 'p', 'q', 'r', 's'],
	'8'=> ['8', 't', 'u', 'v'],
	'9'=> ['9', 'w', 'x', 'y', 'z']
}

# Global variable that stores all wors in a dictionary
$dictionary_words_list=[]

def is_word(word)
	"Method reads dictionary and checks if a given word is in the dictionary
	Input parameter(s): word<str>
	Return(s): <bool>"

	if $dictionary_words_list == []
		File.foreach($options[:d]) do |line|
			$dictionary_words_list << line.chomp
		end
	end

	if $dictionary_words_list.include? word
		return true
	else
		return false
	end
end

def rec_method(remaining, processed)
	"Method recursively generates every possible word from a given number
	Input parameter(s):
	1. substring of number to be processed <str>
	2. substring of number already processed <str>"

	if remaining.length == 0
		if is_word(processed)
			puts processed
		end
	else
		pot_alpha_list=$number_to_alpha_dict[remaining[0]]
		for alpha in pot_alpha_list
			rec_method(remaining[1..remaining.length-1], processed+alpha)
		end
	end
end


$options = {}
OptionParser.new do |opts|
	opts.on("-d dictionary") { |o| $options[:d] = o }
	opts.on("-n number") { |o| $options[:n] = o }
end.parse!

if $options[:d] and $options[:n]
	rec_method($options[:n], "")
else
	puts "Usage: convert.rb -d 'dictionary.txt' -n '123'"
end
