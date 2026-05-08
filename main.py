#importing the necessary libraries
import pandas as pd
import matplotlib.pyplot as plt  
import seaborn as sns

#read the file
iris_data = pd.read_csv('Iris.csv')

#We will now count the number of each species in the table
count = iris_data['Species'].value_counts()
print(count)


columns = [
    "SepalLengthCm",
    "SepalWidthCm",
    "PetalLengthCm",
    "PetalWidthCm"
]

sns.set_theme(style = 'whitegrid')
#create histograms
plt.figure(figsize=(12, 8))
for i, col in enumerate(columns, 1):
    plt.subplot(2, 2, i) #create a position for the graphs as they are plotted
    sns.histplot(data = iris_data, x = col, hue = "Species", bins = 10, kde = True)
    plt.title(col)
plt.tight_layout()
plt.savefig('Histograms.png')

#create boxplots
for i, col in enumerate(columns, 1):
    plt.subplot(2, 2, i)
    sns.boxplot(data = iris_data, x = 'Species',y = col, hue = 'Species', palette = 'Set1')
    plt.title(f'Box plot for {col}')
plt.tight_layout()
plt.savefig('Boxplots.png')

#creating pairplots
new_iris_data = iris_data[['PetalLengthCm', 'PetalWidthCm', 'SepalLengthCm', 'SepalWidthCm', 'Species']]
plt.figure(figsize = (14, 9))
sns.pairplot(new_iris_data, hue = 'Species', palette = 'pastel')
plt.savefig('Pairplot.png')

#creating a correlation matrix
plt.figure(figsize = (12, 8))
corr_matrix = iris_data.select_dtypes(include=['float64', 'int64']).corr()
sns.heatmap(corr_matrix, annot = True, cmap = 'Reds')
plt.savefig('Correlation_heatmap.png')

print('\nAnalysis Complete! Go to FINDINGS file for a summary of the findings.')
