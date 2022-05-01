num = int(input("Put in the upper bound of a range: "))
primes = [2]
for i in range(3, num+1):
    isPrime = True
    for num in primes:
        if i % num == 0:
            isPrime = False
    if isPrime:
        primes.append(i)
for prime in primes:
    print(prime)