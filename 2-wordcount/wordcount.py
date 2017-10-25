excerpt = """
The Babel fish, said The Hitchhikers Guide to the Galaxy quietly,
is small, yellow, and leech-like, and probably the oddest thing in
the Universe. It feeds on brainwave energy received not from its own
carrier but from those around it. It absorbs all unconscious mental
frequencies from this brainwave energy to nourish itself with. It then
excretes into the mind of its carrier a telepathic matrix formed by
combining the conscious thought frequencies with nerve signals picked
up from the speech centres of the brain which has supplied them. The
practical upshot of all this is that if you stick a Babel fish in your
ear you can instantly understand anything said to you in any form of
language. The speech patterns you actually hear decode the brainwave
matrix which has been fed into your mind by your Babel fish.
"""

# Write a python program to print the three most common words from the
# text above
def get_count(input_tuple):
	return input_tuple[1]

strings = excerpt.split()
wordcount= {}
wordcountList = []
for s in strings:
	s=s.lower()
	if(wordcount.__contains__(s)):
		wordcount[s] = wordcount[s]+1;
	else:
		wordcount[s] = 1;
#for t in wordcount.items():
#	wordcountList.append(t)
#wordcountList = wordcount.items();
wordcountList= list(wordcount.items())
wordcountList.sort(key=get_count,reverse=True)
print(wordcountList[0:3])
