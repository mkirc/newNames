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

	def populateNameObj(self, length):

		# random.seed(self.seed)
		nn = ''
		while len(nn) < length:
			txt = self.n.ranStr()
			nn += txt
			self.seed += 1 # for reproducibility
		self.n.out = nn # store name in Name() obj
		return self.n
		



