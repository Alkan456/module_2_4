numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for integer in numbers:
    if integer == 1:
        continue
    is_prime = True
    for a in range(2, integer):
        if integer % a == 0:
            is_prime = False
    if is_prime:
        primes.append(integer)
    else:
        not_primes.append(integer)
print('Primes', primes)
print('Not primes',not_primes)










