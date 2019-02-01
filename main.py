#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Pandas activation
import pandas as pd


# In[2]:


#Import the CSV file
PyBank_file = 'Resources/budget_data.csv'
#read the CSV file
PyBank_df = pd.read_csv(PyBank_file)

PyBank_df.head()


# In[18]:


#The total number of months included in the dataset
Month_count = PyBank_df["Date"].count()
Month_count


# In[19]:


#The total net amount of "Profit/Losses" over the entire period
Net_PL = PyBank_df["Profit/Losses"].sum()
Net_PL


# In[20]:


#The average change in "Profit/Losses" between months over the entire period
PyBank_df['Change PL'] = PyBank_df["Profit/Losses"].diff(periods=1)
PyBank_df.head()
#Average
PLC_Mean = PyBank_df["Change PL"].mean()
PLC_Mean


# In[31]:


#Greatest increase in profits
Max_Profit = PyBank_df["Profit/Losses"].max()
#Max Profit Month
Max_Date = PyBank_df.loc[PyBank_df["Profit/Losses"] == Max_Profit,"Date"]
Max_Date


# In[39]:


#Lowest increase in profits
Min_Profit = PyBank_df["Profit/Losses"].min()
#Max Profit Month
Min_Date = PyBank_df.loc[PyBank_df["Profit/Losses"] == Min_Profit,"Date"]
Min_Date


# In[40]:

print("Financial Analysis")
print("-----------------")
print("Total Months: " + str(Month_count))
print("Total: $" + str(Net_PL))
print("Average Change: $" + str(PLC_Mean))
print("Greatest Increase in Profits: " + str(Max_Date) + " ($" + str(Max_Profit) + ")")
print("Greatest Decrease in Profits: " + str(Min_Date) + " ($" + str(Min_Profit) + ")")

import sys
sys.stdout = open('Financial Analysis.txt','wt')

print("Financial Analysis")
print("-----------------")
print("Total Months: " + str(Month_count))
print("Total: $" + str(Net_PL))
print("Average Change: $" + str(PLC_Mean))
print("Greatest Increase in Profits: " + str(Max_Date) + " ($" + str(Max_Profit) + ")")
print("Greatest Decrease in Profits: " + str(Min_Date) + " ($" + str(Min_Profit) + ")")


# In[ ]:




