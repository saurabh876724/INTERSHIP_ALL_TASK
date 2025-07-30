import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load CSV
df = pd.read_csv("grade.csv")

# 2. Display first few rows
print(df.head())

# 3. Show summary statistics
print(df.describe(), "\n")

# 4. Calculate and display average grade
avg_grade = df['Grade'].mean()
print(f"✅ Average Grade: {avg_grade:.2f}")

# 5. Drop rows with missing Grade values
df = df.dropna(subset=['Grade'])

# 6. Create Grade Band column (e.g., 40s, 50s, 60s)
df['GradeBand'] = (df['Grade'] // 10 * 10).astype(int)

# 7. Bar Chart: Count of Students by Grade Band
df['GradeBand'].value_counts().sort_index().plot(kind='bar', color='skyblue', edgecolor='black')
plt.title("Count of Students by Grade Band")
plt.xlabel("Grade Band")
plt.ylabel("Number of Students")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# 8. Scatter Plot: Study Hours vs Grade
plt.figure(figsize=(6, 4))
plt.scatter(df['StudyHours'], df['Grade'], color='green')
plt.title("Study Hours vs Grade")
plt.xlabel("Study Hours")
plt.ylabel("Grade")
plt.grid(True)
plt.tight_layout()
plt.show()

# 9. Heatmap: Correlation Matrix
plt.figure(figsize=(5, 4))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.show()

# 10. Observations
print("\n🔍 Observations:")
print("1. There is a strong positive correlation between Study Hours and Grade.")
print("2. Average student grade is {:.2f}, indicating average performance.".format(avg_grade))
print("3. Most students fall into the Grade Band of {}.".format(df['GradeBand'].value_counts().idxmax()))

# Scatter plot: Study Hours vs Grade
plt.scatter(df['StudyHours'], df['Grade'])
plt.title("Study Hours vs Grade")
plt.xlabel("Study Hours")
plt.ylabel("Grade")
plt.show()

# Heatmap: correlation
sns.heatmap(df.corr(), annot=True)
plt.title("Correlation Heatmap")
plt.show()

# 3 Observations
print("\n🔍 Observations:")
print("1. There is a positive correlation between study hours and grades.")
print("2. The average grade is around {:.2f}, showing overall performance.".format(avg_grade))
print("3. Grade distribution peaks around bands: {}"
      .format(df['GradeBand'].value_counts().idxmax()))
