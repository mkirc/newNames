import random
from string import capwords
from Name import Name


class NameFactory:

	def __init__(self):

		self.n = None
		self.seed = 2451


	def getNameObj(self):

		self.n = Name()

		return self.n

	def makeNewName(self):

		# random.seed(self.seed)
		nn = ''
		length = random.choice(range(3, 6))
		while len(nn) < length:
			txt = self.n.ranStr()
			nn += txt
			self.seed += 1
		self.n.out = nn
		return self.n
		


def main():

	vovels = 'aeiou'
	consonants = "bcdfghjklmnpqrstvwxzjy"
	nf = NameFactory()
	for i in range(10):
		x = True
		while x:
			count = 0
			nf.getNameObj()
			new = nf.makeNewName()
			for pos,c in enumerate(str(new)):
				if c in vovels:
					count += 1
			try:
				if c and str(new)[pos + 1] in consonants:
						count -= 3
			except IndexError as e:
				pass

			if count >= 3:
				x = False

		print(capwords(str(new)))

main()



