import string
import os

totalWords = 16

# totalWords: The number of words to output
# At 16 words, it fills up the screen so you don't need to scroll up *
# * 2560×1600 display

wordListType = "as"

# Options 1 & 2 search through a wordlist of 416,335 words
# Options 3 & 4 search through a wordlist of 370,102 words
# Option 3 is recommended as you'll get more 'relevant' words
# This also makes it less suspicious
# when the words you answer with are always at the top of the alphabet
# You will also not get results such as 'trinitrophenylmethylnitramine' that increases suspicion

# Option 1: Wordlist sorted by character length
# Result: Words with the shortest length
# Option 2: Wordlist sorted alphabetically
# Result: Words that start at the top of the alphabet (A, B, C...)
# Option 3: Wordlist sorted by character length, only containing more 'real' words
# Result: Words that are more common, with the shortest length
# Option 4: Wordlist sorted alphabetically, only containing more 'real' words
# Result: Words that are more common that start at the top of the alphabet (A, B, C...)

wordlist = []

if wordListType == "c" or wordListType == "char" or wordListType == "len":
	wordListFile = "wordlistchar.txt"
elif wordListType == "n" or wordListType == "normal":
	wordListFile = "wordlist.txt"
elif wordListType == "as":
	wordListFile = "words_alpha_sorted.txt"
elif wordListType == "a":
	wordListFile = "words_alpha.txt"

f = open(wordListFile, "r")
for line in f.readlines():
	wordlist.append(line)

check = input("Letters: ").lower()
allCorrect = []
count = 0
for word in wordlist:
	if check in word:
		allCorrect.append(word)
		count += 1
		if count > totalWords:
			break

# Sort by Length
sortedWords = sorted(allCorrect, key=len, reverse=False)

# Print Matching Words
os.system('clear')
for word in sortedWords:
	print("Letters: " + str(len(word) - 1))
	print(word)
