import random
from string import capwords
from Name import Name


class NameFactory:

	def __init__(self):

		self.n = None
		self.seed = 2451
		self.vo = 'aeiou'
		self.co = 'bcdfghjklmnpqrstvwxzjy'

	def getNameObj(self):

		self.n = Name()

		return self.n

	def populateNameObj(self, length):

		# random.seed(self.seed)
		nn = ''
		while len(nn) < length:
			txt = self.n.ranStr()
			nn += txt
			self.seed += 1 # for reproducibility
		self.n.out = nn # store name in Name() obj
		return self.n
		
	def returnElfName(self, ln):

		x = True
		while x:
			count = 0
			self.getNameObj()
			new = self.populateNameObj(ln)
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

	def returnOrcName(self, ln):

		x = True
		while x:
			count = 0
			self.getNameObj()
			new = self.populateNameObj(ln)
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

