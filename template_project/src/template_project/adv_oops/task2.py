def make_multiplier(n):
    def multiplier(x):
        return x * n

    return multiplier


doubler = make_multiplier(2)
tripler = make_multiplier(3)

if __name__ == "__main__":
    print(doubler(5))
    print(doubler(10))
    print(tripler(5))
    print(tripler(10))
