#!/usr/bin/env python
# coding: utf-8

# In[2]:


from bs4 import BeautifulSoup
import requests


# In[ ]:


# if output is not 200 then there is something wrong with the website


# In[4]:


url = 'https://en.wikipedia.org/wiki/List_of_highest-grossing_Indian_films'
requests.get(url)


# In[ ]:


# Here soup content everything in HTML code and convert it in text


# In[5]:


page = requests.get(url)
soup = BeautifulSoup(page.text,'html')


# In[6]:


print(soup)


# In[ ]:


# here find only use when if we need the first table date where class = 'wikitable sortable plainrowheaders'.
# if there are more than one table in this class then we have to use find_all then to specify which table we need we will use ther position in list like [0]


# In[11]:


table = soup.find('table',class_='wikitable sortable plainrowheaders')


# In[12]:


print(table)


# In[ ]:


# to retrieve only the column data from the table, we are using find_all('th',scope='col')


# In[18]:


column_data = table.find_all('th',scope='col')
print(column_data)


# In[ ]:


# Here we want only the column name in a list.
# so .text function will only return the text not the HTML code and the .strip() function will cleen the data


# In[19]:


column_name = [name.text.strip() for name in column_data ]
print(column_name)


# In[20]:


import pandas as pd


# In[ ]:


# Here we are assigned in the column name to the df data frame form the column_name list 


# In[22]:


df = pd.DataFrame(columns=column_name)
df


# In[ ]:


# here we can clearly see that there are column data as well


# In[47]:


row_data = table.find_all('tr')
print(row_data)


# In[ ]:


# Here we only need the row data so to exclude the column data we did [1:] this


# In[29]:


row_data = table.find_all('tr')[1:]
print(row_data)


# In[ ]:


# we can see that the title data are in between 'th' and othes are in between 'td'.
# so we crated two list here for both of them.(individual_row,title_data)


# In[45]:


for x in row_data:
    row= x.find_all('td')
    title = x.find_all('th')
    individual_row = [y.text.strip() for y in row]
    title_data = [z.text.strip() for z in title]
    # to insert the title_data in individual_row in position 1 
    position = 1
    for item in title_data:
        individual_row.insert(position,item)
        position += 1
    individual_row_data = individual_row
    # to check the if the number of item is the same as number of column
    #print(individual_row_data)
    
    length = len(df)
    df.loc[length] = individual_row_data


# In[46]:


print(df)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




