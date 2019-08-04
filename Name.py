import random
# import string



class Name:

    def __init__(self):

        self.out = ''
        # builds dict with values (single char (c/v),
        # consonant - vowel combination and c-v-c combination )
        self.s = self.genStr()
        self.cvcMatrix = []

    def __str__(self):
        return str(self.out)

    def ranStr(self):

        # makes random choice of string combination (one, two oder three) 
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
        self.cvcMatrix = [[i for i in cvc[j:j + 17]] for j in range(0, 1734, 17)]
        # print(len(filterd), len(vowels))

        for i in range(3):
            self.s[i + 1] = values[i]
        return self.s
        

def main():

    n = Name()
    # n.genStr()

    # for pos,i in enumerate(n.s[1]):
    #     try:
    #         print(i, n.s[1][pos + 1])
    #     except IndexError as e:
    #         pass
    

# main()