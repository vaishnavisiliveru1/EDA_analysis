# EDA_analysis
This project applies Exploratory Data Analysis (EDA) to the Student Performance Dataset, which contains demographic, family, lifestyle, and academic details of secondary school students.The dataset includes three grade evaluations (G1, G2, G3) along with contextual variables such as study time, absences, parental education, and internet access.

##  Project Overview
This project performs **Exploratory Data Analysis (EDA)** on the *Student Performance Dataset*.  
The goal is to uncover **patterns, correlations, and key influencing factors** that affect student grades.

---

##  Objectives
- Perform statistical summaries of the dataset.
- Visualize distributions and relationships between variables.
- Identify correlations and key factors influencing final grades (G3).
- Present insights in a structured, easy-to-understand format.

---

##  Dataset
- **Source:** Kaggle / UCI Machine Learning Repository  
- **Rows:** ~650  
- **Columns:** 33 (demographics, family background, lifestyle, grades)  
- **Target Variable:** `G3` (Final Grade)

---

##  Tools & Libraries
- **Python 3.9+**
- **Pandas** – data manipulation
- **NumPy** – numerical operations
- **Matplotlib & Seaborn** – visualizations
- **Jupyter Notebook / Spyder** – analysis environment

---

##  EDA Workflow
1. **Data Understanding**
   - Inspected dataset shape, data types, and first few rows.
2. **Data Cleaning**
   - No missing values detected.
   - No duplicate rows found.
3. **Univariate Analysis**
   - Histograms for age, absences, and grades.
   - Boxplots to detect outliers in absences and grades.
   - Count plots for categorical variables (gender, address).
4. **Bivariate & Multivariate Analysis**
   - Correlation heatmap for grades and numeric features.
   - Scatterplots (e.g., G1 vs G3).
   - Boxplots (study time vs final grade).
   - Pairplots for key variables.
5. **Key Influencing Factors**
   - Grouped analysis by gender, study time, and internet access.
6. **Insights & Recommendations**
   - Summarized findings with actionable points.

---

## Key Insights (from analysis)
- **No missing values or duplicates** → dataset is clean and ready for analysis.
- **Gender:** Average final grade (G3) is slightly higher for males (≈10.9) compared to females (≈9.9).
- **Study Time:** Students with higher study time (levels 3 & 4) achieve better grades (≈11.3).
- **Internet Access:** Students with internet access score higher (≈10.6) than those without (≈9.4).
- **Absences:** Higher absences correlate with lower performance.
- **Grades Correlation:** Strong positive correlation between G1, G2, and G3 (early grades predict final outcomes).

---

##  How to Run
1. Clone this repository
2. jupyter notebook EDA_analysis.ipynb

