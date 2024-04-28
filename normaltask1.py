import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load transactional data into a DataFrame
transaction_data = pd.read_csv("C:\\Users\\DELL\\Desktop\\transaction_data.csv")

# Perform basic data exploration
print(transaction_data.head())  # Display the first few rows of the dataset
print(transaction_data.info())  # Get information about the dataset

# Check for missing values
print(transaction_data.isnull().sum())

# Explore customer demographics
print(transaction_data.describe())
print(transaction_data.value_counts())

# Visualize customer demographics
Overall_sales_per_month=transaction_data.groupby("MONTH")['VALUE'].sum()
Overall_sales_per_month.plot(kind='line',marker='d',linestyle='-')
plt.title('Overall_sales_per_month')
plt.xlabel('Month')
plt.ylabel('Overall sales')
plt.show()

Numerical_Values = transaction_data.select_dtypes(include=['float64', 'int64'])
correlation_matrix = Numerical_Values.corr()
print("Correlation Matrix:")
print(correlation_matrix)

plt.figure(figsize=(8, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='PuRd', fmt=".2f", linewidths=1.5)
plt.title('Correlation Matrix')
plt.show()
