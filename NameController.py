import random
from string import capwords
from Name import Name
from makeName import NameFactory

class NameControl:

	def __init__(self, race, minlen, maxlen):

		self.rc = race
		self.ln = random.choice(range(minlen, maxlen)) # Name length
		self.vo = 'aeiou'
		self.co = 'bcdfghjklmnpqrstvwxzjy'
		self.nf = NameFactory()
		self.cur = self.getNamebyRace()


	def __str__(self):

		return str(self.cur)

	def getNamebyRace(self):

		if self.rc == 'elf':
			return self.returnElfName()
		elif self.rc == 'orc':
			return self.returnOrcName()


	def returnElfName(self):

		x = True
		while x:
			count = 0
			self.nf.getNameObj()
			new = self.nf.populateNameObj(self.ln)
			for pos,c in enumerate(str(new)):
				if c in self.vo:
					count += 1
				if c in 'ozwkrtqx':
					count -= 3
				if c in 'dhalrin':
					count += 2
			try:
				# check if next char is consonant
				if c and str(new)[pos + 1] in self.co:
						count -= 5
			except IndexError as e:
				pass
			if str(new)[len(str(new)) - 1] in 'rnm':
					count += 9

			if count >= 15:
				x = False

		return capwords(str(new))	

	def returnOrcName(self):

		x = True
		while x:
			count = 0
			self.nf.getNameObj()
			new = self.nf.populateNameObj(self.ln)
			for pos,c in enumerate(str(new)):
				# check if char is vowel
				if c in self.vo:
					count += 1
				if c in 'ourkbztfs':
					count += 3
				if c in 'aijyx':
					count -= 10
			try:
				# check if next char is consonant
				# makes assumtions about more readable names
				if c and str(new)[pos + 1] in self.co:
						count -= 5
			except IndexError as e:
				pass
			if str(new)[len(str(new)) - 1] in 'rokg':
					count += 10

			if count >= 15:
				x = False

		return capwords(str(new))

def ohneVieleWorte():

	orc = NameControl('orc', 3 ,6)
	print(orc)
	for i in range(3):
		newElf = NameControl('elf', 3, 6)
		newElfSurname = NameControl('elf', 4, 7)
		print(str(newElf) + ' ' + str(newElfSurname))

ohneVieleWorte()


'''

def main():

	vovels = 'aeiou'
	consonants = "bcdfghjklmnpqrstvwxzjy"
	nf = NameFactory()
	print('dotcom:')
	for i in range(1):
		x = True
		while x:
			count = 0
			nf.getNameObj()
			new = nf.makeNewName()
			for pos,c in enumerate(str(new)):
				# check if char is vowel
				if c in vovels:
					count += 2
			try:
				# check if next char is consonant
				# makes assumtions about more readable names
				if c and str(new)[pos + 1] in consonants:
						count -= 9
			except IndexError as e:
				pass

			if count >= 3:
				x = False
			suff = random.choice(['.net', '.io', '.com'])
		print(' ' + capwords(str(new)) + suff)

	print('orc:')
	for i in range(3):
		x = True
		while x:
			count = 0
			nf.getNameObj()
			new = nf.makeNewName()
			for pos,c in enumerate(str(new)):
				# check if char is vowel
				if c in vovels:
					count += 1
				if c in 'ourkbztfs':
					count += 3
				if c in 'aijyx':
					count -= 10
			try:
				# check if next char is consonant
				# makes assumtions about more readable names
				if c and str(new)[pos + 1] in consonants:
						count -= 5
			except IndexError as e:
				pass
			if str(new)[len(str(new)) - 1] in 'rokg':
					count += 10

			if count >= 15:
				x = False

		print(' ' + capwords(str(new)))

	print('elf:')
	for i in range(3):
		x = True
		while x:
			count = 0
			nf.getNameObj()
			new = nf.makeNewName()
			for pos,c in enumerate(str(new)):
				# check if char is vowel
				if c in vovels:
					count += 1
				if c in 'ozwkrtqx':
					count -= 3
				if c in 'dhalrin':
					count += 2
			try:
				# check if next char is consonant
				# makes assumtions about more readable names
				if c and str(new)[pos + 1] in consonants:
						count -= 5
			except IndexError as e:
				pass

			if str(new)[len(str(new)) - 1] in 'rnm':
					count += 9

			if count >= 15:
				x = False

		print(' ' + capwords(str(new)))
main()

'''