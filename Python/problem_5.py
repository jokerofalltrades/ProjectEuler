def gen_primes(max: int, min: int = 0) -> list[int]:
    primes = [True] * (max)
    primes[0], primes[1] = False, False

    for i in range(2, int(max ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, max, i):
                primes[j] = False
    return [i for i in range(min, max) if primes[i]]

def find_prime_factors(num: int, prime_numbers: list[int]) -> dict[int, int]:
    prime_factors: dict[int, int] = {prime: 0 for prime in prime_numbers}
    while num != 1:
        for prime in prime_numbers:
            while num % prime == 0:
                prime_factors[prime] += 1
                num = num // prime
    return prime_factors

prime_numbers = gen_primes(20)
prime_factors: dict[int, int] = {prime: 0 for prime in prime_numbers}
for i in range(1, 20):
    new_freq = find_prime_factors(i, prime_numbers)
    prime_factors = {prime: max(freq, new_freq[prime]) for prime, freq in prime_factors.items()}

final_multiple: int = 1
for prime, freq in prime_factors.items():
    final_multiple *= prime ** freq

print(final_multiple)
