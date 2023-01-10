import pandas as pd
df = pd.read_csv('3D+2DStrData.csv')
df.hist(column='EDV') #this is not a bell curve
df.hist(column='ESV') #this is not a bell curve
df.hist(column='EF') #this is a bell curve but skewed
df.hist(column='LS (Freewall)')#this is a bell curve but skewed
df.hist(column='LS Fre_Mean')#this is the most complete bell curve but still a little skewed
j = df.iloc[:,7:13].corr()#there is correlation between these variables. Most are above 0.5 which indicates strong and positive.
#Not printing the correlation because it cuts certain columns off. It is in the variable explorer
skew_edv = df.iloc[:,1] #selecting the first columns EDV
skew_edv1 = skew_edv.skew() #skew of EDV
kurt_edv = skew_edv.kurt() #kurtosis EDV
print("EDV Skew: ",skew_edv1)#this is acceptable skewedness since it falls between 3 and -3
print("EDV Kurtotsis: ",kurt_edv)#this is acceptable kurtosis since it falls between 10 and -10
print("\n")

skew_esv = df.iloc[:,2] #selecting the second column ESV
skew_esv1 = skew_esv.skew() #skew of ESV
kurt_esv = skew_esv.kurt() #kurtosis ESV
print("ESV Skew: ",skew_esv1)#this is not acceptable skewness since it falls outside of 3 and -3
print("ESV Kurtotsis: ",kurt_esv)#this is not acceptable kurtosis since it falls outside of 10 and -10
print("\n")

skew_ef = df.iloc[:,4] #selecting the 4th column EF
skew_ef1 = skew_ef.skew() #skew of EF
kurt_ef = skew_ef.kurt() #kurtosis of EF
print("EF Skew: ",skew_ef1)#this is acceptable skewness since it falls between 3 and -3
print("EF Kurtosis: ",kurt_ef)#this is acceptable kurtosis since it falls between 10 and -10
print("\n")

skew_LSF = df.iloc[:,8] #selecting the 8th column LS Freewall
skew_LSF1 = skew_LSF.skew() #skew LS Freewall
kurt_LSF = skew_LSF.kurt() #Kurtosis LS Freewall
print("LS Freewall skew: ",skew_LSF1) #This is acceptable skewness sicne it falls between 3 and -3
print("LS Freewall Kurtosis: ",kurt_LSF)#this is acceptable kurtosis since it falls between 10 and -10
print("\n")

skew_LFSM = df.iloc[:,10] #selecting the 10th column LS Fre_Mean
skew_LFSM1 = skew_LFSM.skew() #skew of LS Fre_Mean
kurt_LFSM = skew_LFSM.kurt() #Kurtosis of LS Fre_Mean
print("LS Fre_Mean: ",skew_LFSM1)#this is acceptalbe skewness since it falls between 3 and -3
print("LS Fre_Mean Kurtosis: ",kurt_LFSM)#this is acceptable kurtosis since it falls between 10 and -10
print("\n")

ap = df.loc[0:49, :] #dataframe is locating the specific rows from 0-49, Group APAH
ap_everything = ap.describe()
ap_mean = print("APAH Mean: ")
print("",ap_everything.iloc[2,:])
print("\n")
ap_std = print("APAH STD: ")
print("",ap_everything.iloc[3,:])
print("\n")

normal = df.loc[50:99, :] #dataframe is locating the specific rows from 50-99, Group Normal
normal_everything = normal.describe()
normal_mean = print("Normal Mean: ")
print("",normal_everything.iloc[2,:])
print("\n")
normal_std = print("Normal STD: ")
print(" ",normal_everything.iloc[3,:])
print("\n")

ph = df.loc[100:142, :] #dataframe is locating specific rows from 100-142, Group PH
ph_everything = ph.describe()
ph_mean = print("PH Mean: ")
print("",ph_everything.iloc[2,:])
print("\n")
ph_std = print("PH STD: ")
print("",ph_everything.iloc[3,:])