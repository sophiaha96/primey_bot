import math

primel_cache = []

# sieve of eratosthenes
def compute_primel_cache(limit: int):
    not_prime = set()

    for num in range(2, limit):
        if num in not_prime:
            continue

        for n in range(num * 2, limit, num):
            not_prime.add(n)
        
        primel_cache.append(num)