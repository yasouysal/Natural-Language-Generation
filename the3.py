# -*- coding: utf-8 -*-
import random
def isvowel(letter):
	vowels=["a","e","I","i","o","O","U","u"]
	if letter in vowels:
		return True
	else:
		return False


def isend(word, pivot):
	if len(word)-1 == pivot:
		return True
	else:
		return False

def GetValue(x): return x[1]

def GetTopTwo(candidates):
	temp = candidates.copy()
	if temp == {}:
		return []
	else:
		key1, value1 = max(temp.iteritems(), key=GetValue)
		
		del temp[key1]
		
		if temp == {}:
			return [key1]
		else:
			key2, value2 = max(temp.iteritems(), key=GetValue)
			return [key1, key2]




def hyphenate(word):
	pivot = 0
	is_finished = False
	while not is_finished:
		if isvowel(word[pivot]):
			if isend(word,pivot):
				is_finished = True
			else:
				pivot = pivot + 1
				if isvowel(word[pivot]):
					word = word[:pivot] + "-" + word[pivot:]
					pivot = pivot + 1
				else:
					looping = False
					while not looping:
						if isend(word,pivot):
							is_finished = True
							looping = True
						else:
							pivot = pivot + 1
							if isvowel(word[pivot]):
								word = word[:pivot-1] + "-" + word[pivot-1:]
								looping = True
							else:
								continue
		else:
			if isend(word, pivot):
				is_finished = True
			else:
				pivot = pivot + 1
	return word.split("-")


def execute():
	first_line = raw_input()
	b = True
	Lines = []
	while b:
		Lines.append(raw_input())
		if "=" in Lines:
			b = False

	M = []
	for j in range (len(Lines)-1):
		splitted_line = []
		for item in Lines[j].split():
			splitted_line.append(item)
			splitted_line.append(' ')
		splitted_line = splitted_line[:-1]
		

		hyphenated_line = []
		
		for i in range (len(splitted_line)):
			hyphenated_line = hyphenated_line + hyphenate(splitted_line[i])
			
		k = 0
		while k < len(hyphenated_line):
			
			if hyphenated_line[k][0] == '.' and hyphenated_line[k] != '.':
				
				hyphenated_line[k] = hyphenated_line[k][1:]
				hyphenated_line.insert(k,'.')
				k+=1
			
			elif hyphenated_line[k][-1] == '.' and hyphenated_line[k] != '.':
				
				hyphenated_line[k] = hyphenated_line[k][:-1]
				hyphenated_line.insert(k+1,'.')
				k+=1
			else:
				k+=1
		
		M = M + hyphenated_line
		if j != len(Lines)-2 and hyphenated_line[-1] != '.':
			M.append(' ')
	M.insert(0,' ')

	stats ={}
	previous_syl = ' ' 
	for current_syl in M:
		if previous_syl not in stats:
			stats[previous_syl] = {}
		if current_syl not in stats[previous_syl]:
			stats[previous_syl][current_syl] = 1
		else:
			stats[previous_syl][current_syl] += 1
		previous_syl = current_syl
	
	
	first_line_values = first_line.split(' ')
	output_text = ''
	previous_syl = random.choice(stats.keys())
	output_text += previous_syl
	word_count = 1
	
	
	while word_count <= int(first_line_values[0]) and len(output_text) <= int(first_line_values[1]):
		if output_text[-1] == '.':
			randomly_picked_word = random.choice(stats.keys())
			output_text += randomly_picked_word
			previous_syl = randomly_picked_word
		else:
			randomly_picked_word = random.choice(GetTopTwo(stats[previous_syl]))
			output_text += randomly_picked_word
			previous_syl = randomly_picked_word
		if randomly_picked_word == ' ':
			word_count += 1
		
	
	print output_text


