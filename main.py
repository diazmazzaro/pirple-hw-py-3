#  __    __  ____    __    ____      ____   
# |  |  |  | \   \  /  \  /   /     |___ \  
# |  |__|  |  \   \/    \/   / ______ __) | 
# |   __   |   \            / |______|__ <  
# |  |  |  |    \    /\    /         ___) | 
# |__|  |__|     \__/  \__/         |____/  
#                                           

# Compare 3 values if 2 or more are equals return True
def TripleCompare(a,b,c):
	if int(a) == int(b):
		return True
	if int(a) == int(c):
		return True
	if int(b) == int(c): 
		return True
	return False

# Compare 3 values if 2 or more are equals return True. Shorter definition
def TripleCompareShort(a,b,c):
	return int(a) == int(b) or int(a) == int(c) or int(b) == int(c)

# Should be False
print(TripleCompare(1,2,3))

# Should be True
print(TripleCompare(1,2,2))

# Should be True also
print(TripleCompare(2,2,2))

# Should be True (with int parse)
print(TripleCompare(0,2,"2"))

# Should be False (with int parse)
print(TripleCompare(0,"2",3))


# Should be False
print(TripleCompareShort(1,2,3))

# Should be True
print(TripleCompareShort(1,2,2))

# Should be True also
print(TripleCompareShort(2,2,2))

# Should be True (with int parse)
print(TripleCompareShort(0,2,"2"))

# Should be False (with int parse)
print(TripleCompareShort(0,"2",3))