#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().system('pip install mysqlclient')


# In[3]:


import MySQLdb


# In[5]:


get_ipython().system('pip install pandas')


# In[6]:


import pandas as pd


# In[7]:


import getpass


# In[ ]:


def get_user_input(result):
    return input(result)
def connect_to_db(host,user,password,db):
    try:
        db=MySQLdb.connect(host=host,user=user,password=password,db=db)
        return db
    except MySQLdb.error as e:
        print(f"The error is connecting to MySQL database: {e}")
        return None
def run_query(cursor,column,table):
    try:
        query= f"SELECT {column} FROM {table}"
        cursor.execute(query)
        rows=cursor.fetchall()
        columns=[desc[0] for desc in cursor.description]
        df=pd.DataFrame(rows, columns=columns)
        return df
    except MySQLdb.Error as e:
        print(f"Error executing query: {e}")
        return None

def main():
    host=get_user_input("Enter host name: ")
    user=get_user_input("Enter username: ")
    password=getpass.getpass("Enter password: ")
    db=get_user_input("Enter db name: ")
    
    db=connect_to_db(host,user,password,db)
    if db is None:
        return
    
    cursor=db.cursor()
    column=get_user_input("Enter column name: ")
    table=get_user_input("Enter table name: ")
    
    result_table=execute_query(cursor,column,table)
    if result_table is not None:
        print(result_table)
        
    cursor.close()
    db.close()

if __name__=="__main__":
    main()
    
        


# In[ ]:




