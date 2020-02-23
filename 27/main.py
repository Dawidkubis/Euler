def generate_primes(lim):
    primes = []
    nums = list(range(2, lim))
    while nums != []:
        primes.append(nums[0])
        nums = [i for i in nums if i%primes[-1] != 0]
    return primes

def is_prime (number):
    prime = True

    root = int(math.sqrt(number)) + 1

    for i in generate_primes(root):
        if number % i == 0:
            prime = False
            break
    return prime


