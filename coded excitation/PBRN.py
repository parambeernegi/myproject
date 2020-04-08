import numbers, random, sys
if sys.version_info.major ==2:
    range = xrange


# Random number generator class(implments most functionlity of random.Random)

class LfsrRandom(random.Random):

    def __new__(cls, *args, **kwargs): # magic beacause the superclass doesn't cooperate
        return random.Random.__new__(cls, random.random())


    def __init__(self, charis, state):
        assert isinstance(charis, numbers.Integral)
        assert isinstance(state, numbers.Integral)

        if charis < 0:
            raise ValueError("Invalid characteristic polynomial -negative")

        if charis.bit_length() < 2:
            raise ValueError("invalid characteristic polynomial - degee too low")

        if state == 0:
            raise ValueError("Invalid characteristic polynomial - all zero")

        if state.bit_length() >= charis.bit_length():
            raise ValueError("Invalid state polynomial - degree >= char poly degree")

        self.characteristic = charis
        self.degree = charis.bit_length()-1
        self.state = state


    def randbit(self):
        result = self.state & 1  # use but 0 in the LFSR state a s the reuslt
        self.state = self.state << 1  # multiply by x
        if(self.state >> self.degree ) & 1 !=0:  # If degree of state polynomial matches degree of char poly
            self.state ^= self.characteristic  # Then subtract the characteristic
        return result

    def getrandbits(self, k):
        result = 0
        for i in range(k):
            result = (result << 1)  | self.randbit()
        return result

    def random(self):
        return self.getrandbits(8)/ float(1<<3)


# Demo main program

if __name__ =="__main__":
    # Polynomial : x^16 + x^14 +x^13+ x^11 + x^0
    rand = LfsrRandom(0b10111001000101,1)
    for i in range(10):
        print(rand.random())
    for i in range(20):
        print(rand.random())
