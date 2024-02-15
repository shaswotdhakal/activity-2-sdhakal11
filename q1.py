def isPrime(num):
"""
This function check if the number is prime.
"""

if num < 2: 
   return False
for i in range(2, int(num**0.5)+1):
   if num % i == 0:
     return False
return True

def getPrimeNumbers(n):
  """
  THis function returns a list of all prime numbers between 2 and n.
  """

return [num for num in range(2, n+1) if isPrime(num)]
