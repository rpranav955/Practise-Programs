import pandas as pd

data = {
    'Department': ['HR', 'HR','HR', 'IT', 'IT'],
    'Gender': ['Male', 'Female','Female', 'Male', 'Female'],
    'Salary': [30000, 35000, 35000, 45000, 50000]
}

df = pd.DataFrame(data)

pivot = pd.pivot_table(df,
                       values='Salary',
                       index='Department',
                       columns='Gender',
                       aggfunc='mean')
                       
df = pd.DataFrame(data)

table = pd.crosstab(df['Gender'], df['Department'])

print("Pivot Tabulation:")
print(pivot)

print()

print("Cross Tabulation:")
print(table)
