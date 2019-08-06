import random
from string import capwords
from Name import Name
from makeName import NameFactory

class NameControl:

	def __init__(self, race, minlen, maxlen):

		self.rc = race
		self.ln = random.choice(range(minlen, maxlen)) # Name length

		self.nf = NameFactory()
		self.cur = self.getNamebyRace()

	def __add__(self, other):

		return str(str(self.cur) + ' ' + str(other.cur))

	def __str__(self):

		return str(self.cur)

	def getNamebyRace(self):

		if self.rc == 'elf':
			return self.nf.returnElfName(self.ln)
		elif self.rc == 'orc':
			return self.nf.returnOrcName(self.ln)



def ohneVieleWorte():

	newOrcName = NameControl('orc', 3 ,6)
	newOrcSurname = NameControl('orc', 4, 7)
	print(newOrcName + newOrcSurname)
	for i in range(3):
		newElfName = NameControl('elf', 3, 6)
		newElfSurname = NameControl('elf', 5, 8)
		print(newElfName + newElfSurname)

ohneVieleWorte()

