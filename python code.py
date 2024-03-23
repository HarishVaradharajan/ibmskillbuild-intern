# -*- coding: utf-8 -*-
"""Untitled14.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1DLlvaKZhRHg960B4IAL7_BvcD0Jum00T
"""

# prompt: read the file named as CVD_cleaned.csv

import pandas as pd

df = pd.read_csv('CVD_cleaned.csv')

# Print the DataFrame
print(df)

# prompt: based on Smoking_History create a visualization

import matplotlib.pyplot as plt

# Get the value counts of Smoking_History
smoking_counts = df['Smoking_History'].value_counts()

# Create a bar chart
plt.bar(smoking_counts.index, smoking_counts.values)
plt.xlabel('Smoking History')
plt.ylabel('Count')
plt.title('Visualization of Smoking History')
plt.show()

# prompt: create a code based on General_Health create a visualization of piechart

# Get the value counts of General_Health
health_counts = df['General_Health'].value_counts()

# Create a pie chart
plt.pie(health_counts.values, labels=health_counts.index, autopct="%1.1f%%")
plt.title('Visualization of General Health')
plt.show()

# prompt: set Sex as the main attribute compare General_Health, Skin_Cancer,Other_Cancer

import pandas as pd
import matplotlib.pyplot as plt

# Create a crosstab of Sex, General_Health, Skin_Cancer, and Other_Cancer
crosstab = pd.crosstab(df['Sex'], [df['General_Health'], df['Skin_Cancer'], df['Other_Cancer']], margins=True)

# Plot the crosstab as a bar chart
crosstab.plot(kind='bar', stacked=True)
plt.xlabel('Sex')
plt.ylabel('Count')
plt.title('Comparison of General Health, Skin Cancer, and Other Cancer by Sex')
plt.show()

# prompt: based on Height_(cm),Weight_(kg),BMI create the visualization for their General_Health in visualization

import seaborn as sns

# Create a boxplot of BMI by General_Health
sns.boxplot(x="General_Health", y="BMI", data=df)
plt.xlabel('General Health')
plt.ylabel('BMI')
plt.title('Distribution of BMI by General Health')
plt.show()

# Create a scatter plot of Height_(cm) vs. Weight_(kg), colored by General_Health
sns.scatterplot(x="Height_(cm)", y="Weight_(kg)", hue="General_Health", data=df)
plt.xlabel('Height (cm)')
plt.ylabel('Weight (kg)')
plt.title('Relationship between Height, Weight, and General Health')
plt.show()