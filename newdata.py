import pandas as pd
import numpy as np

# 1. Loading
df = pd.read_csv("Employee.csv", encoding="latin1")
print("Step 1: Data Loaded")

# 2. Cleaning Data
df['Annual Salary'] = df['Annual Salary'].replace(r'[\$,]', '', regex=True).astype(float)
df['Bonus %'] = df['Bonus %'].str.rstrip('%').astype('float') / 100.0
print("Step 2: Salary and Bonus Cleaned")

# 3. NumPy Calculations
salary_array = df['Annual Salary'].to_numpy()
bonus_array = df['Bonus %'].to_numpy()
df['Incentive'] = np.multiply(salary_array, bonus_array)
print("Step 3: Incentive Calculated")

# 4. Sorting Data
# Sort by Salary (Highest to Lowest)
df_sorted = df.sort_values(by="Annual Salary", ascending=False)
print("\nStep 4: Data Sorted by Salary (Top 5)")
print(df_sorted[['Full Name', 'Annual Salary']].head())

# 5. Filtering with Multiple Conditions
# Employees in IT over the age of 40
it_senior = df[(df['Department'] == 'IT') & (df['Age'] > 40)]
print("\nStep 5: Filtered IT Employees Age > 40")
print(it_senior[['Full Name', 'Age', 'Department']].head())

# 6. Value Counts
# Counting employees by Country
country_counts = df['Country'].value_counts()
print("\nStep 6: Employee Count by Country")
print(country_counts)

# 7. Pivot Tables
# Average Salary by Department and Gender
pivot = df.pivot_table(values='Annual Salary', index='Department', columns='Gender', aggfunc='mean')
print("\nStep 7: Pivot Table - Avg Salary by Dept and Gender")
print(pivot)



# 8. Handling Missing Values
# Check for nulls and fill Exit Date with 'Active'
print("\nStep 8: Missing Values Count")
print(df.isnull().sum())
df['Exit Date'] = df['Exit Date'].fillna('Active')
print("Exit Date 'NaN' replaced with 'Active'")

# 9. Creating Bins (Categorizing)
# Categorizing Age into Groups
bins = [20, 30, 40, 50, 65]
labels = ['20-30', '31-40', '41-50', '51+']
df['Age Group'] = pd.cut(df['Age'], bins=bins, labels=labels)
print("\nStep 9: Age Groups Created")
print(df[['Full Name', 'Age', 'Age Group']].head())

# 10. String Operations
# Find all managers using string contains
managers = df[df['Job Title'].str.contains('Manager', case=False, na=False)]
print("\nStep 10: Found Employees with 'Manager' in Job Title")
print(managers[['Full Name', 'Job Title']].head())

# 11. Dropping Columns
# Remove unnecessary columns for a clean report
df_clean = df.drop(columns=['EEID', 'Ethnicity', 'City'])
print("\nStep 11: Unnecessary Columns Dropped")
print(df_clean.columns)

# 12. Exporting Data
# Save the final processed data to a new CSV
df.to_csv("Processed_Employee_Data.csv", index=False)
print("\nStep 12: Final Data Exported to Processed_Employee_Data.csv")