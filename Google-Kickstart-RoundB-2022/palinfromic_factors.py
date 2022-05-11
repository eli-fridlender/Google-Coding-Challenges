import math
import numpy as np

def find_factor_palindromes(case_num):
  number = int(input())
  num_of_palindromes = 0

  num_of_factors, factors = get_factors(number)
  for factor in range(0, num_of_factors, 1):
    if is_palindrome(int(factors[factor])):
      num_of_palindromes += 1

  print(f"Case #{case_num}: {num_of_palindromes}")


def is_palindrome(num):
  temp = str(num)
  new_num = ""

  for i in range(0, len(temp), 1):
    new_num = new_num + temp[len(temp) - i - 1]
  return(str(num) == new_num)


def get_factors(num):
  ARRAY_SIZE = 1000000
  factors = np.ones(ARRAY_SIZE)
  num_of_factors = 1

  if num > 1:
    for i in range(1, math.ceil((num+1)/2), 1):
      if num % i == 0:
        factor = int(num/i)
        if i not in factors:
          factors[num_of_factors] = i
          num_of_factors +=1
        if factor not in factors:
          factors[num_of_factors] = factor
          num_of_factors +=1


  return num_of_factors, factors



num_cases = int(input())
for i in range(num_cases):
  find_factor_palindromes(i+1)