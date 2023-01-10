import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data = {'Year': [1960,1965,1970,1975,1980,1985,1990,1995,2000,2005],
        'Mortality': [26.0, 24.7, 20.0, 16.1, 12.6, 10.6, 9.2, 7.6, 6.9, 6.9]}
df = pd.DataFrame (data=data)
df["Year squared"] = df["Year"]**2
df["Mortality * Year"] = df["Year"]*df["Mortality"]
total_year = df['Year'].sum()
total_mortality = df['Mortality'].sum()
total_yearsquared = df['Year squared'].sum()
total_yearmortality = df['Mortality * Year'].sum()

n=10
m = ((n*total_yearmortality - (total_year*total_mortality)))/((n*total_yearsquared)-(total_year)**2)
b= (total_mortality - (m*total_year))/n
print("slope: ", m)
print("y-intercept: ", b)
y = m*(df["Year"]) + b

reg = np.polyfit(df['Year'], df['Mortality'], deg = 1)
trend = np.polyval(reg, df['Year'])
plt.scatter(df['Year'], df['Mortality'])
plt.plot(df["Year"], trend, 'r')

y1 = m*(2010)+b
print('Predicted: ',y1)
print("\n")

#%% 11.20 - 11.23

data1 = {'Age': [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17],
          'SBP': [99,102,105,107,108,110,111,112,114,115,117,120,122,125,127,130,132]}
df1 = pd.DataFrame(data=data1)
df1["X**2"] = df1["Age"]**2
df1["Age * SBP"] = df1["Age"] * df1["SBP"]
total_age = df1['Age'].sum()
total_sbp = df1['SBP'].sum()
total_xsquared = df1["X**2"].sum()
total_agesbp = df1['Age * SBP'].sum()

p=17
m1 = ((p*total_agesbp-(total_age*total_sbp)))/((p*total_xsquared)-(total_age)**2)
b1 = (total_sbp - (m1*total_age))/p
print("slope: ",m1)
print("y-intercept: ",b1)

reg1 = np.polyfit(df1['Age'], df1['SBP'], deg = 1)
trend1 = np.polyval(reg1, df1['Age'])
plt.scatter(df1['Age'], df1['SBP'])
plt.plot(df1["Age"], trend1, 'r')
 

#11.20
y1 = m1*(13)+b1
print("Predict SBP for 13 year old dude: ",y1)
#plt.scatter(df1["Age"],df1["SBP"])

#11.22
y2 = m1*(17)+b1
print("Predict SBP for 17 year old dude: ",y2)

#11.23
#Yes it is a good fit since the errors are low. 