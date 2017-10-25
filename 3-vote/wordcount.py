from collections import defaultdict
def get_count(input_tuple):
	return input_tuple[1]

wordcount= defaultdict(int)
wordcountList = []
voters = defaultdict(int)
try:
	f = open("votes.txt")
	for l in f:
		s=l.split("-")
		colour=s[1].strip()
		v=s[0].strip().lower()
		#print(s)
		if(voters[v]==0):
			voters[v] = 1
			wordcount[colour] = wordcount[colour]+1;
finally:
	f.close()
wordcountList= list(wordcount.items())
wordcountList.sort(key=get_count,reverse=True)
print(wordcountList[:1])
#print(voters)
