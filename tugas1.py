import collections
def fungsiwordcount(input):
	myinp=input.split(' ')
	a=collections.Counter(myinp)
	return (dict(a));
	
input = input('Enter words: ')
print (fungsiwordcount(input));
