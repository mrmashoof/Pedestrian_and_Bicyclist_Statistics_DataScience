# Course   : Data Science with Python
# Teacher  : Mr. Pouriya Baghdadi
# Student  : Mohammadreza Mashouf
# Session  : 6


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


path = 'C:\Mohammad\Learning\Python\Python-P.Baghdadi-My Course\Session_6\S6_Assignment\pedestrian-and-bicyclist-counts.csv'
df_csv = pd.DataFrame(pd.read_csv(path))
'*****************************************************************************************************************************'

# Question : 01
df_csv['Total'] = df_csv['Cyclists'] + df_csv['Pedestrians']
'*****************************************************************************************************************************'

# Question : 02
df_csv['Cyclists - Pedestrians'] = df_csv['Cyclists'] - df_csv['Pedestrians']
CycDays = df_csv.loc[df_csv['Cyclists - Pedestrians']>0]
print ('Question 02 : \n' +
       'In ' +
       str('{:,.0f}'.format(len(CycDays.index))) +
       ' days, the cyclists numbers have been more than pedestrians .'+
       '\n')
'*****************************************************************************************************************************'

# Question : 03
CycMean = df_csv['Cyclists'].mean()
PedMean = df_csv['Pedestrians'].mean()
print ('Question 03 : \n' +
       'Cyclists average numbers (per day) : ' +
       str('{:,.0f}'.format(CycMean)) +
       '\n' +
       'Pedestrians average numbers (per day) : ' +
       str('{:,.0f}'.format(PedMean)) +
       '\n')
'*****************************************************************************************************************************'

# Question : 04
sns.kdeplot(df_csv['Pedestrians'])
plt.show()
print ('Question 04 : \n'
       'As the chart shows, the distribution is like normal distribution with positive (right) skewness.'+
       '\n')
'*****************************************************************************************************************************'

# Question : 05
Ped_percentile_9970 = np.percentile(df_csv['Pedestrians'],q=99.70)
print ('Question 05 : \n' +
       ' 99.7% observations is less than ' +
       str('{:,.0f}'.format(Ped_percentile_9970)) +
       ' pedestrians.' +
       '\n')
'*****************************************************************************************************************************'

# Question : 06
Ped_percentile_7500 = np.percentile(df_csv['Pedestrians'],q=75)
print ('Question 06 : \n' +
        'In 3th quarter, 75% of the observations  for pedestrians is less than ' +
        str('{:,.0f}'.format(Ped_percentile_7500)) +
        '.' +
        '\n')
'*****************************************************************************************************************************'

# Question : 07
Ped_std = df_csv['Pedestrians'].std()
Ped_range = np.ptp(df_csv['Pedestrians'])
print ('Question 07 : \n' +
       'Pedestrians Standard Deviation = ' +
       str('{:,.2f}'.format(Ped_std)) +
       '\n' +
       'Pedestrians Range = ' +
       str('{:,.0f}'.format(Ped_range)) +
       '\n')
'*****************************************************************************************************************************'

# Question : 08
Cyc_skew = df_csv['Cyclists'].skew()
Cyc_kurt = df_csv['Cyclists'].kurt()
print ('Question 08 : \n' +
       'Cyclists Skewness = ' +
       str('{:,.2f}'.format(Cyc_skew)) +
       '\n' +
       'Cyclists Kurtosis = ' +
       str('{:,.2f}'.format(Cyc_kurt)) +
       '\n' +
       'In result, because skewness and kurtosis are between -2 and +2, so the cyclists distribution could count as a normal distribution.' +
       '\n')
'*****************************************************************************************************************************'

# Question : 09
print ('Question 09 : \n' +
       'Option 3 is correct. If (Mean > Median > Mode) then we have Positive Skew.' +
       '\n')
'*****************************************************************************************************************************'

# Question : 10
print ('Question 10 : \n' +
       'Option 3 is correct. When Standard deviation is four, it shows all datas,include 99% of them, are between 112 and 120, and other options are wrong. ' +
       '\n')