import pandas as pd
import numpy as np

# 1 question reading csv
data = pd.read_csv('data.csv', delimiter=',')
print(data)
# 2 question meaning of table
data_series = data.describe()
print(data_series)
# 3 question first rows and last rows print
print(data.head())
print(data.tail())
# 5 question
data['DebtRatio'] = data['DebtRatio'] * data['MonthlyIncome']
print(data['DebtRatio'])
# 6 question
data.rename(columns={'DebtRatio': 'Debt'}, inplace=True)
print(data['Debt'])
# 7 question
print(data['MonthlyIncome'])
data_null = pd.isnull(data['MonthlyIncome'])
i = data_null == True
data['MonthlyIncome'] = i.mean()
print(data['MonthlyIncome'])
#8 question
#data_grouped = data.groupby('SeriousDlqin2yrs')

data_num_dep = data['SeriousDlqin2yrs'].groupby(data['NumberOfDependents']).mean()
data_num_estate = data['SeriousDlqin2yrs'].groupby(data['NumberRealEstateLoansOrLines']).mean()
print(data_num_dep)
print(data_num_estate)
