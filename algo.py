from main import *

def by_word_count():
	c = open("comments.txt").read().split("\n")
	a = MultiThread(c, calc_words)
	g = a.run_all()
	print g

if __name__ == '__main__':
	by_word_count()
