#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[ ]:


pd.set_option("display.max_columns", None)
file=input("Enter location/name of file:")
sheet=input("Enter sheet name you ish to sort:")
file_2= pd.read_excel(file, sheet_name=sheet, index_col=0, na_values=["NA"])

sorter=[]
style=[]
sortq=int(input("Please enter # of columns you wish to sort by:"))

for x in range(sortq):
    column_name=input(f"Nmae of column you wish to sort by {x+1}:")
    sorter.append(column_name)
    order=input(f"Type True for Asc, False for Desc sort{x+1}")
    style.append(order.lower()=="True")
    
    sort1= file_2.sort_values(by=sorter, ascending=style)
    
    destwb= input ("Enter destination and filename")
    sort1.to_excel(destwb, sheet_name="Sheet1")


# In[ ]:




