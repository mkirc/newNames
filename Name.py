import random
# import string



class Name:

    def __init__(self):

        self.out = ''
        self.s = self.genStr()

    def __str__(self):
        return str(self.out)

    def ranStr(self):

        cur = random.choice([x for x in self.s.keys()])
        s = self.s[cur]
        return random.choice(s)
        

    def genStr(self):

        self.s = {}

        consonants = "bcdfghjklmnpqrstvwxz"
        vowels = "aeiouy"
        filterd = "bcdfghklmnprstvwz"

        cvc = []
        cv_vc = []
        values = []
        values.append(''.join([consonants, vowels]))

        for c in filterd:
            for v in vowels:
                cv_vc.append(''.join([c,v]))
                cv_vc.append(''.join([v,c]))
                for cc in filterd:
                    cvc.append(''.join([c, v, cc]))
            values.append(cv_vc)
            values.append(cvc)
        # matrix = [[i for i in chunks[j:j + 20]] for j in range(0, 2399, 20)]

        for i in range(3):
            self.s[i + 1] = values[i]
        return self.s
        

def main():

    n = Name()
    n.genStr()
    for pos,i in enumerate(n.s[1]):
        try:
            print(i, n.s[1][pos +1 ])
        except IndexError as e:
            pass
    

# main()