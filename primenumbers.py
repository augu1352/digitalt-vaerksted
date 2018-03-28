class Generator:
    def __init__(self):
        pass
    def findPrimes(self, amount):
        Pnumbers = []
        for n in range(1, int(amount) + 1):
            isPrime = True
            for i in range(2, n):
                if i == n or i == 1:
                    break
                if n % i == 0:
                    isPrime = False
                    break
            if isPrime:
                Pnumbers.append(n)

        return Pnumbers

g = Generator()
print(g.findPrimes(1000000))

