#!/usr/bin/env python
# coding: utf-8

# In[6]:


def validate_cc(n):
    digit_list=number_to_list(n)
    
    if len(digit_list)%2==0:
        double_alt_digits(0,digit_list)
    else:
        double_alt_digits(1,digit_list)
    return sum(digit_list)%10==0
    
def number_to_list(n):
    return [int(x) for x in str(n)]

def double_alt_digits(start_index,digit_list):
    for i in range(start_index,len(digit_list),2):
        double_value=digit_list[i]*2
        if double_value<10:
            digit_list[i]= double_value
        else:
            digit_list[i]=sum_of_digits(double_value)
            
def sum_of_digits(n):
    return(n//10)+(n%10)
print(validate_cc(int(input("Enter CC number to validate\n>"))))


# In[ ]:




