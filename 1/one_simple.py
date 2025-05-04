# # Import necessary libraries
# import seaborn as sns
# import matplotlib.pyplot as plt

# # Load the built-in Iris dataset
# iris = sns.load_dataset("iris")

# # Show the first few rows of the dataset
# print(iris.head())

# # Plot 1: Histogram of Sepal Length
# plt.figure(figsize=(6, 4))
# sns.histplot(iris['sepal_length'], kde=True, color='skyblue')
# plt.title("Histogram of Sepal Length")
# plt.xlabel("Sepal Length (cm)")
# plt.ylabel("Count")
# plt.show()

# # Plot 2: Scatter plot of Sepal Length vs Sepal Width
# plt.figure(figsize=(6, 4))
# sns.scatterplot(x='sepal_length', y='sepal_width', hue='species', data=iris)
# plt.title("Sepal Length vs Width by Species")
# plt.xlabel("Sepal Length (cm)")
# plt.ylabel("Sepal Width (cm)")
# plt.show()

# # Plot 3: Pairplot - compares all features
# sns.pairplot(iris, hue='species')
# plt.suptitle("Pairplot of Iris Dataset", y=1.02)
# plt.show()


#--------------------------------------------------------------------------------
# sepal_length  sepal_width  petal_length  petal_width    species
# 0           5.1          3.5            1.4           0.2    setosa
# 1           4.9          3.0            1.4           0.2    setosa
# 2           4.7          3.2            1.3           0.2    setosa
# 3           4.6          3.1            1.5           0.2    setosa


# # Import necessary libraries
import seaborn as sns
import matplotlib.pyplot as plt

# Load the built-in Iris dataset
iris = sns.load_dataset("iris")

# Select only the first 4 rows of the dataset
iris_subset = iris.head(4)

# 1. Histogram of Sepal Length (for first 4 entries)
plt.figure(figsize=(6, 4))
sns.histplot(iris_subset['sepal_length'], kde=True, color='skyblue')
plt.title("Histogram of Sepal Length (First 4 Entries)")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Count")
plt.show()

# 2. Scatter plot of Sepal Length vs Sepal Width (for first 4 entries)
plt.figure(figsize=(6, 4))
sns.scatterplot(x='sepal_length', y='sepal_width', hue='species', data=iris_subset)
plt.title("Sepal Length vs Width by Species (First 4 Entries)")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Sepal Width (cm)")
plt.show()

# 3. Pairplot - compares all features (for first 4 entries)
sns.pairplot(iris_subset, hue='species')
plt.suptitle("Pairplot of First 4 Entries of Iris Dataset", y=1.02)
plt.show()




