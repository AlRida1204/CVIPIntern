import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Load the dataset
df = pd.read_csv("C:\\Users\\User\\Downloads\\email.csv")

# Visualize spam distribution with a bar plot
plt.figure(figsize=(6, 4))
sns.boxplot(x='spam', data=df, palette=['blue', 'orange'])
plt.xlabel('Spam')
plt.ylabel('Count')
plt.title('Spam Distribution')
plt.xticks([0, 1], ['Not Spam', 'Spam'])
plt.show()

# Prepare data
X = df['text'].astype(str)
y = df['spam'].replace({0: "Not Spam", 1: "Spam"}).astype("object")

# Calculate email lengths
email_lengths = X.str.len()


# Plot violin plot of email lengths vs. spam
plt.figure(figsize=(8, 6))
sns.violinplot(x=y, y=email_lengths, palette=['yellow', 'black'])
plt.xlabel('spam')
plt.ylabel('Email Length')
plt.title('Violin plot of Email Lengths vs. Spam')
plt.show()

