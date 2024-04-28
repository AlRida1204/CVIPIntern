import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = pd.read_csv("C:\\Users\\DELL\\Desktop\\path_to_your_file.csv")

# Convert the 'Date' column to datetime format
data['Date'] = pd.to_datetime(data['Date'])

# Set 'Date' column as the index
data.set_index('Date', inplace=True)

data.plot(figsize=(10, 6))
plt.title('Stock Prices Over Time')
plt.xlabel('Date')
plt.ylabel('Price')
plt.grid(True)
plt.legend(loc='upper left')
plt.show()

corr = data.corr()

# Plot correlation matrix
plt.figure(figsize=(10, 8))
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Matrix of Stock Prices')
plt.show()

plt.figure(figsize=(10, 6))
sns.boxplot(data=data)
plt.title('Boxplot of Stock Prices')
plt.xlabel('Stock')
plt.ylabel('Price')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
