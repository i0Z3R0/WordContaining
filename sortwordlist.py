import string
import os

wordlist = []
if 1:
	f = open("words_alpha.txt", "r")
	for line in f.readlines():
		wordlist.append(line)
sword = sorted(wordlist,key=len)
g = open("words_alpha_sorted.txt", "w")
for word in sword:
	g.write(word)

if 0:
	check = input("Letters: ").lower()
	allcorrect = []
	count = 0
	for word in wordlist:
		if check in word:
			allcorrect.append(word)
			count += 1
			if count > totalwords:
				break

	# Sort by Length
	sortedwords = sorted(allcorrect, key=len, reverse=False)

	# Print Matching Words
	os.system('clear')
	for word in sortedwords:
		print("Letters: " + str(len(word) - 1))
		print(word)
