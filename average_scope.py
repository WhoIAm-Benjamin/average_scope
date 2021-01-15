from time import sleep
from statistics import mean

import sys


def intellect(b):
	""" def 'intellect' for calculate value 
	:param b: list of scopes; 
	"""
	while True:
		print('\rWhat average scope do you want?', end = ' ')
		
		average = input()
		try:
			average = float(average)
			break
		except ValueError:
			continue
	k = 0
	while (mean(b) < average + 0.01):
		b.append(5)
		k += 1
	print('You need else', k, '"5"')
	print('Average scope will be -', mean(b))
	input()

def main():
	""" main function on program """
	i = 0
	b = []
	print('For exit enter "end"')
	while True:
		print('\rEnter scope:', end = ' ')
		a = input()
		
		try:
			a = int(a)
			i += a
			b.append(a)
		except ValueError:
			if a == 'end':
				print('\nOK')
				break
			else:
				continue
	average = i / len(b)

	print('Your average scope is', average)

	while True:
		print('\rAre you want improve average score?(y/n)', end = ' ')
		need = input().lower()
		if need == 'n':
			print('\nOK')
			sleep(5)
			sys.exit()
		elif need == 'y':
			print('\nNow we will calculate')
			intellect(b)
			break
		else:
			continue

if __name__ == '__main__':
	main()