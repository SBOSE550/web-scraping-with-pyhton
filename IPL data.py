#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import requests


# In[ ]:


# url of the website.
# If the output is not 200 then there is something wrong with the website


# In[2]:


url = 'https://www.timesofsports.com/cricket/ipl/which-is-the-best-team/'
requests.get(url)


# In[ ]:


# all the HTML code will be assigned to soup in text format


# In[4]:


page = requests.get(url)
soup = BeautifulSoup(page.text,'html')
print(soup)


# In[7]:


table = soup.find('table', width="581")
print(table)


# In[ ]:


# column_data only contains the column value.


# In[16]:


x = table.find_all('tr')[0]
column_data = x.find_all('td')
print(column_data)


# In[ ]:


#column_name only contains the column names in a list in text formant and the strip function cleans the data.


# In[17]:


column_name = [name.text.strip() for name in column_data]
print(column_name)


# In[18]:


import pandas as pd


# In[20]:


df = pd.DataFrame(columns = column_name)
df


# In[22]:


row_data= table.find_all('tr')[1:]
print(row_data)


# In[25]:


for x in row_data:
    row = x.find_all('td')
    individual_row_data = [y.text.strip() for y in row]
    #print(individual_row_data) # to check the if the number of item in individual_row_data is the same as number of column 
    length = len(df)
    df.loc[length]=individual_row_data


# In[26]:


df


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




