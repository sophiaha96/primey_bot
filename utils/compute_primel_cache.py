# Sieve of Eratosthenes
# https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes

from constants import MAX

primel_cache = []
def compute_primel_cache():
    not_prime = set()

    for num in range(2, MAX + 1):
        if num in not_prime:
            continue

        for n in range(num * 2, MAX + 1, num):
            not_prime.add(n)

        primel_cache.append(num)