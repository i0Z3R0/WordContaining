import string

wordlist = []
with open("wordlist.txt") as f:
	for line in f:
		word = line.strip("\n")
		lowerword = word.lower()
		wordlist.append(lowerword)

#print(wordlist)


sorted = sorted(wordlist)

g = open("sorted.txt", "w")
if sorted == wordlist:
	print("same")
else:
	print('diff')

for word in sorted:
	g.write(word + "\n")



allbadwords = [".","'","-","-"]
#with open("sorted.txt") as k:
#	for line in k:
#		word = line.strip("\n")
#		allbadwords.append(word)

#print(allbadwords)

if 1:
	h = open("wordlist.txt","r")
	thelines = h.readlines()
	print("LINES READ")
	newlines = []
	with open("tmpwordlist.txt", "w") as f:
		for thisline in thelines:
			done = 0
			for badword in allbadwords:
				if done == 0:
					if "/" in thisline:
						print("Bad word detected")
						print(f"Word: {thisline}")
						done = 1
					else:
						if done == 0:
							newlines.append(thisline)
							#print("LINE WRITTEN")
							done = 1
		print("FINISHED CHECKING")
		for word in newlines:
			f.write(word)

print("DONE")
