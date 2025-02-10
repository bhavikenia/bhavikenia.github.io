import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read the CSV file
data = pd.read_csv('t20.csv')  # Replace 'your_file.csv' with the path to your CSV file

# Specify the variable for which you want to create a boxplot
variable_of_interest = 'Inns'  # Replace 'MonthlyExpenses' with the name of the column containing your variable

# Create a boxplot using Seaborn
sns.boxplot(x=data[variable_of_interest], showfliers=True)

# Add a title
plt.title(f'Boxplot of {variable_of_interest} innings played by cricket players in T20')

# # Display the plot
# plt.show()

# Saves the plot automtically to the folder
plt.savefig("boxplot.png")