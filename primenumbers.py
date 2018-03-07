class Generator:
    def __init__(self, amount):
        numbers = []
        for n in range(int(amount) + 1):
            for i in range(2, n):
                if not n % i == 0
