import pandas as pd
import matplotlib.pyplot as plt

# Raw Data
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

print("=== RAW PILOT DATA TABLE ===")
print(df.to_string(index=False))

print("\n=== DESCRIPTIVE STATISTICS ===")
print(df[['Req_CPU', 'Actual_CPU_Util', 'Volatility_CPU']].describe())

print("\n=== MEAN ACTUAL CPU UTILISATION BY TASK TYPE ===")
print(df.groupby('Task_Type')['Actual_CPU_Util'].mean())

df['Efficiency_CPU'] = df['Actual_CPU_Util'] / df['Req_CPU']
print("\nMean CPU Efficiency Ratio:", round(df['Efficiency_CPU'].mean(), 4))

corr = df['Req_CPU'].corr(df['Actual_CPU_Util'])
print("Pearson Correlation:", round(corr, 4))

# Bar Chart
means = df.groupby('Task_Type')['Actual_CPU_Util'].mean()
means.plot(kind='bar', color=['#1f77b4', '#ff7f0e', '#2ca02c'], figsize=(8,5))
plt.title('Average CPU Utilisation by Task Type (Pilot Sample)')
plt.ylabel('CPU Utilisation')
plt.xlabel('Task Type')
plt.xticks(rotation=0)
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig('pilot_bar_chart.png', dpi=300)
plt.show()

print("\nBar chart saved as 'pilot_bar_chart.png'")