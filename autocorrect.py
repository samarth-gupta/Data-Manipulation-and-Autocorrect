
def parse( str ):
	new_str = ''
	for ch in str:
		if ch == '\'':
			continue
		if (65 <= ord(ch) <= 90):
			new_str += chr(ord(ch)+32)
		elif (97 <= ord(ch) <= 122):
			new_str += ch
		else:
			new_str += ' '
	return new_str

inp = ''
with open('Assignment_1/big.txt','r') as f:
	inp = f.read()

inp = parse(inp)

words = inp.split()
word_cnt = {}

for word in words:
	if word_cnt.get(word) == None:
		word_cnt[word] = 0
	word_cnt[word] += 1

words = sorted(set(word_cnt.keys()))

def edits1(word):
	alphabet = "abcdefghijklmnopqrstuvwxyz"
	splits     = [(word[:i], word[i:]) for i in range(len(word) + 1)]
	deletes    = [a + b[1:] for a, b in splits if b]
	transposes = [a + b[1] + b[0] + b[2:] for a, b in splits if len(b)>1]
	replaces   = [a + c + b[1:] for a, b in splits for c in alphabet if b]
	inserts    = [a + c + b     for a, b in splits for c in alphabet]
	return set(deletes + transposes + replaces + inserts)

def frequency(word):
	if word_cnt.get(word) == None:
		return 0
	else:
		return word_cnt[word]

word_in = input("Please enter a word\n")

one_dist = edits1(word_in)

two_dist = set()

for one_word in one_dist:
	temp = edits1(one_word)
	two_dist = two_dist.union(temp)



first_option = max(one_dist, key=frequency)
answer = first_option

if frequency(first_option) == 0:
	answer = max(two_dist, key=frequency)

print("The closest word in corpus is:",answer)