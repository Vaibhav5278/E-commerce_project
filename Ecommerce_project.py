#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install plotly


# In[4]:


import pandas as pd    #used to clean the data 

import plotly.express as px   #it is advanced library for visualization
import plotly.graph_objects as go   #used to make advaanced graph
import plotly.io as pio    #used for graph tamplates
import plotly.colors as colors  #used for colors
pio.templates.default = "plotly_white"  #used for default templates


# In[5]:


data = pd.read_csv("Sample - Superstore.csv", encoding = 'latin-1') #latin reads special characters in data
data


# In[9]:


print(data.head(5))


# In[10]:


data.describe()    #describe default mathematical operation


# In[11]:


data.info()


# # CONVERTING DATE COLUMNS

# In[12]:


data['Order Date'] = pd.to_datetime(data['Order Date'])    #converting object to datetime data type


# In[13]:


data.info()


# In[14]:


data['Ship Date'] = pd.to_datetime(data['Ship Date'])    #converting object to datetime data type


# In[15]:


data.info()


# In[21]:


data.head()


# In[20]:


#created 3 new colums with the help of order date column
data['Order Month'] = data['Order Date'].dt.month
data['Order Year'] = data['Order Date'].dt.year
data['Order Day of Week'] = data['Order Date'].dt.dayofweek


# In[18]:


data.head()


# # MONTHLY SALES ANALYSIS

# In[22]:


sales_by_month = data.groupby('Order Month')['Sales'].sum().reset_index()


# In[23]:


sales_by_month


# In[24]:


fig = px.line(sales_by_month,
             x = 'Order Month',
             y = 'Sales',
             title = 'Monthly Sales Analysis')
fig.show()


# In[25]:


data.head()


# # SALES BY CATEGORY

# In[26]:


sales_by_category = data.groupby('Category')['Sales'].sum().reset_index()


# In[27]:


sales_by_category


# In[28]:


fig = px.pie(sales_by_category,
            values = 'Sales',
            names = 'Category',
            hole = 0.05,
            color_discrete_sequence=px.colors.qualitative.Pastel)

fig.update_traces(textposition='inside',textinfo='percent+label')
fig.update_layout(title='Sales Analysis by Category', title_font=dict(size=24))

fig.show()


# # Sales analysis by Sub Category

# In[29]:


data.head()


# In[30]:


sales_by_subcategory = data.groupby('Sub-Category')['Sales'].sum().reset_index()


# In[31]:


sales_by_subcategory


# In[32]:


fig = px.bar(sales_by_subcategory, x = 'Sub-Category', y = 'Sales', title = 'Sales analysis by sub-category')

fig.show()


# # Monthly Profit Analysis

# In[33]:


data.head()


# In[34]:


profit_by_month = data.groupby('Order Month')['Profit'].sum().reset_index()


# In[35]:


profit_by_month


# In[36]:


fig = px.line(profit_by_month, x = 'Order Month' , y = 'Profit', title = 'Monthly profit analysis')


# In[37]:


fig.show()


# # Profit by Category

# In[38]:


profit_by_category = data.groupby('Category')['Profit'].sum().reset_index()


# In[39]:


profit_by_category


# In[40]:


fig = px.pie(profit_by_category,
            values = 'Profit',
            names = 'Category',
            hole = 0.05,
            color_discrete_sequence=px.colors.qualitative.Pastel)

fig.update_traces(textposition='inside',textinfo='percent+label')
fig.update_layout(title='Profit Analysis by Category', title_font=dict(size=24))

fig.show()


# # Profit by sub-category

# In[35]:


profit_by_subcategory = data.groupby('Sub-Category')['Profit'].sum().reset_index()


# In[36]:


profit_by_subcategory


# In[37]:


fig = px.bar(profit_by_subcategory, x = 'Sub-Category', y = 'Profit', title = 'Sales analysis by sub-category')

fig.show()


# # Sales and profit for customer segment

# In[38]:


data.head()


# In[41]:


sales_profit_by_segment = data.groupby('Segment').agg({'Sales':'sum', 'Profit':'sum'}).reset_index()

color_palette = colors.qualitative.Pastel

fig = go.Figure()
fig.add_trace(go.Bar(x = sales_profit_by_segment['Segment'],
                    y = sales_profit_by_segment['Sales'],
                    name = 'Sales',
                    marker_color=color_palette[0]))


fig.add_trace(go.Bar(x = sales_profit_by_segment['Segment'],
                    y = sales_profit_by_segment['Profit'],
                    name = 'Profit',
                    marker_color=color_palette[1]))

fig.update_layout(title = 'Sales and profit analysis by customer segment',
                 xaxis_title = 'Customer Segment', yaxis_title = 'Amount')

fig.show()


# # Sales to profit ratio

# In[43]:


sales_profit_by_segment = data.groupby('Segment').agg({'Sales':'sum', 'Profit':'sum'}).reset_index()

sales_profit_by_segment['Sales_to_Profit_Ratio'] = sales_profit_by_segment['Sales'] / sales_profit_by_segment['Profit']

print(sales_profit_by_segment[['Segment', 'Sales_to_Profit_Ratio']])


# In[ ]:




