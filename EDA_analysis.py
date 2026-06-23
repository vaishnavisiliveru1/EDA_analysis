
# 1. Import Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set style
sns.set(style="whitegrid")
plt.rcParams["figure.figsize"] = (8,5)

# 2. Load Dataset
df = pd.read_csv("student_data.csv")

# 3. Basic Understanding
print("Shape:", df.shape)
print("\nData Types:\n", df.dtypes)
print("\nFirst 5 rows:\n", df.head())

# 4. Statistical Summaries
print("\nNumerical Summary:\n", df.describe())
print("\nCategorical Summary:\n", df.describe(include="object"))

# 5. Missing Values & Duplicates
print("\nMissing Values:\n", df.isnull().sum())
print("\nDuplicate Rows:", df.duplicated().sum())
df = df.drop_duplicates()

# 6. Univariate Analysis
# Histograms for numeric features
df[['age','absences','G1','G2','G3']].hist(bins=15, figsize=(12,6))
plt.suptitle("Distribution of Numeric Features")
plt.show()

# Boxplots for outlier detection
for col in ['age','absences','G1','G2','G3']:
    sns.boxplot(x=df[col])
    plt.title(f"Boxplot of {col}")
    plt.show()

# Bar chart for categorical variables
sns.countplot(x="sex", data=df)
plt.title("Gender Distribution")
plt.show()

sns.countplot(x="address", data=df)
plt.title("Urban vs Rural Students")
plt.show()

# 7. Bivariate Analysis
# Correlation matrix
corr = df[['age','absences','G1','G2','G3']].corr()
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

# Scatter plot: G1 vs G3
sns.scatterplot(x="G1", y="G3", hue="sex", data=df)
plt.title("Relationship between G1 and Final Grade (G3)")
plt.show()

# Boxplot: Studytime vs G3
sns.boxplot(x="studytime", y="G3", data=df)
plt.title("Study Time vs Final Grade")
plt.show()
# 8. Multivariate Analysis
sns.pairplot(df[['G1','G2','G3','studytime','absences']], diag_kind="kde")
plt.suptitle("Pairplot of Key Variables", y=1.02)
plt.show()

# 9. Key Influencing Factors
# Grouped analysis
print("\nAverage Final Grade by Gender:\n", df.groupby("sex")["G3"].mean())
print("\nAverage Final Grade by Study Time:\n", df.groupby("studytime")["G3"].mean())
print("\nAverage Final Grade by Internet Access:\n", df.groupby("internet")["G3"].mean())

