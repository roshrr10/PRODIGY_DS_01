#!/usr/bin/env python
# coding: utf-8

# # TASK 1

# # Insurance Data Analysis
# 
# AIM: To analyze the distribution of various features in the insurance dataset.
# 
# The dataset contains information about individuals, including their age, gender, body mass index (BMI), and other attributes. I've created visualizations to understand the distributions of these features better.

# In[1]:


# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


# Load the dataset
file_path = 'insurance.csv'
data = pd.read_csv(file_path)


# In[3]:


# Display the first few rows of the dataset
data.head()


# In[4]:


# Plotting the distribution of ages using a histogram
plt.figure(figsize=(10, 6))
sns.histplot(data['age'], kde=False, bins=30)
plt.title('Distribution of Ages')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()


# In[7]:


# Plotting the distribution of bmi using a histogram
plt.figure(figsize=(10, 6))
sns.histplot(data['bmi'], kde=False, bins=30)
plt.title('Distribution of BMI')
plt.xlabel('BMI')
plt.ylabel('Frequency')
plt.show()


# In[6]:


# Plotting the distribution of genders using a bar chart
plt.figure(figsize=(8, 4))
sns.countplot(x='sex', data=data)
plt.title('Distribution of Genders')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.show()

