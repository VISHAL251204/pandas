import pandas as pd

# 1. Load the dataset
df = pd.read_csv("Employee.csv", encoding="latin1")
print("Step 1: Data loaded successfully.\n Total rows:", len(df))

# 2. Clean 'Annual Salary' 
# We remove '$' and ',' so they treats the salary as a number 

df['Annual Salary'] = df['Annual Salary'].replace(r'[\$,]', '', regex=True).astype(float)
print(df['Annual Salary'].head())

# 3. Clean 'Bonus %' and calculate 'Incentive'
df['Bonus %'] = df['Bonus %'].str.rstrip('%').astype('float') / 100.0
df['Incentive'] = df['Annual Salary'] * df['Bonus %']

print(df[['Annual Salary', 'Bonus %', 'Incentive']].head())

print("Step 3: 'Incentive' calculated based on salary.")

# 4. GroupBy Operations

dept_summary = df.groupby("Department").agg({"Annual Salary": ["mean", "sum", "count"], "Incentive": "sum"})
print("Step 4: Department-wise statistics calculated:")
print(dept_summary.head())

# 5. Date Operations

df['Hire Date'] = pd.to_datetime(df['Hire Date'])
df['Year'] = df['Hire Date'].dt.year
df['Month'] = df['Hire Date'].dt.month
print("Step 5: 'Hire Date' processed into Year and Month columns.")

# 6. Correlation Analysis
# This shows the statistical relationship between age, salary, and incentives.
correlation_matrix = df[["Age", "Annual Salary", "Incentive"]].corr()
print("Step 6: Correlation analysis completed:")
print(correlation_matrix)

# Final Look
print("\n--- Final Cleaned Data ---")
print(df[["Full Name", "Department", "Annual Salary", "Incentive", "Year"]])