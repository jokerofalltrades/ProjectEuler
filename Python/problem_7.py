def gen_primes(max: int, min: int = 0) -> list[int]:
    primes = [True] * (max)
    primes[0], primes[1] = False, False

    for i in range(2, int(max ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, max, i):
                primes[j] = False
    return [i for i in range(min, max) if primes[i]]

print(gen_primes(1000000)[10000])
