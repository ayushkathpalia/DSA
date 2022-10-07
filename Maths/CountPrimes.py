#(Sieve of Erathanos)
#Sieve of Eratosthenes is a method for finding all primes up to (and possibly including) a given natural. 
#This method works well when is relatively small, allowing us to determine whether any natural number less
#than or equal to is prime or composite. 

def countPrimes(n):
    if n <= 2:
        return 0
    count = 0
    prime = [True for i in range(n+1)]
    prime[0] = prime[1] = False
    p = 2
    while (p * p <= n):

        # If prime[p] is not
        # changed, then it is a prime
        if (prime[p] == True):

            # Update all multiples of p
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1

    # Print all prime numbers
    for p in range(2, n+1):
        if prime[p]:
            count+=1
    print(prime)
    return count


ans = countPrimes(3)
print(ans)