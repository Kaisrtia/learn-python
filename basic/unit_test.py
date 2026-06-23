# pip install pytest
# to run type: pytest {file}.py in terminal

def square(n):
	return n + n

def test_pos():
	assert square(2) == 4
	assert square(3) == 9

def test_neg():
	assert square(-2) == 4
	assert square(-3) == 9

