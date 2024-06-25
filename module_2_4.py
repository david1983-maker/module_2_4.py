numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
primes = []
not_primes = []

a = len(numbers)

for i in range(a):
    d = 0
    for j in range(1, i + 1):

        if i % j == 0:
            d += 1
    if d == 2:
        primes.append(i)
    else:
        not_primes.append(i)

print('Primes:',primes )

print('Not Primes:',not_primes[2::])
