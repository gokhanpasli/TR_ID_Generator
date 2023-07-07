#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random


# In[ ]:


def generate_tc_id():
    
    # Generating 9 random digits
    tc_digits = [random.randint(0, 9) for _ in range(9)]
    
    # The first digit can not be zero
    tc_digits[0] = random.randint(1, 9)
    
    # Sum of the 1, 3, 5, 7 and 9. digits multiplied by 7 plus
    # Sum of the 2, 4, 6 and 8. digits multiplied by 9 gives the 10th digit.
    sum_odd_digits = sum(tc_digits[0::2])
    sum_even_digits = sum(tc_digits[1::2])
    tenth_digit = ((sum_odd_digits * 7) + (sum_even_digits * 9)) % 10
    
    # The ones digit of the sum of the first 10 digits gives the 11th digit
    eleventh_digit = (sum(tc_digits) + tenth_digit) % 10
    tc_digits.append(tenth_digit)
    tc_digits.append(eleventh_digit)
    
    # Output TC ID number
    return "".join(map(str, tc_digits))


# In[ ]:


# A loop for generating ID numbers of the amount that is needed.
num_of_ids = int(input("How many ID numbers would you like to generate?: "))

for i in range(num_of_ids):
    tc_id = generate_tc_id()
    print(tc_id)

