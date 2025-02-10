import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read the CSV file
data = pd.read_csv('t20.csv')  # Replace 'cars.csv' with your actual file path

# Specify the variable for which you want to create a strip plot
variable_of_interest = 'Mat'  

# Create a strip plot using Seaborn
sns.stripplot(data=data, x=variable_of_interest, hue=variable_of_interest)

# Add a title
plt.title(f'Strip plot of {variable_of_interest}ches played by cricket players in T20')

# # Display the plot
# plt.show()

plt.savefig("stripplot.png")
