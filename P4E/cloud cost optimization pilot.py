import pandas as pd

data = {
    'Record_ID': [1,2,3,4,5,6,7,8,9,10,11,12],
    'Task_Type': ['Production','Best-Effort','Production','Batch','Production',
                  'Best-Effort','Production','Batch','Production','Best-Effort',
                  'Production','Batch'],
    'Req_CPU': [0.45,0.12,0.78,0.25,0.55,0.08,0.92,0.35,0.60,0.15,0.40,0.28],
    'Actual_CPU_Util': [0.38,0.09,0.65,0.22,0.48,0.06,0.81,0.29,0.52,0.11,0.35,0.25],
    'Volatility_CPU': [0.08,0.03,0.12,0.05,0.07,0.02,0.15,0.06,0.09,0.04,0.10,0.05]
}

df = pd.DataFrame(data)

# Descriptive statistics
print(df[['Req_CPU', 'Actual_CPU_Util', 'Volatility_CPU']].describe())

# Mean by Task Type
print("\nMean Actual CPU Utilisation by Task Type:")
print(df.groupby('Task_Type')['Actual_CPU_Util'].mean())

# Efficiency ratio
df['Efficiency_CPU'] = df['Actual_CPU_Util'] / df['Req_CPU']
print("\nMean CPU Efficiency Ratio:", df['Efficiency_CPU'].mean())

# Correlation
corr = df['Req_CPU'].corr(df['Actual_CPU_Util'])
print("Pearson Correlation (Req_CPU vs Actual_CPU_Util):", round(corr, 4))
