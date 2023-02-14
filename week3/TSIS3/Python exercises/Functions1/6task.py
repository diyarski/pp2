def reverse_words(s, a, b):
	while a < b:
		s[a], s[b] = s[b], s[a]
		a = a + 1
		b -= 1
s = "We are ready"
s = list(s)
a = 0
while True:
	try:
		b = s.index(' ', a)
		reverse_words(s, a, b - 1)
		a = b + 1
	except ValueError:
		reverse_words(s, a, len(s) - 1)
		break
s.reverse()
s = "".join(s)
print(s)
