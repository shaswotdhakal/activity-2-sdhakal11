"""Generate all prime number upto n"""
def getPrimeNumbers(n):

    """Checking if the num is prime or not"""
    def if_prime(num):

     
     if num < 2:
            return False
     
     for i in range(2, num):

        if num % i == 0:       
                return False
        
        return True
     """Generate a list of prime numbers"""
    return [num for num in range(2, n+1) if if_prime(num)]

"""Call the function and print the number withing 1000"""
print(getPrimeNumbers(1000)) 

