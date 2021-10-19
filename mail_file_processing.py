# Apply the pandas methods and functions along with profiling and interpret your findings from given dataset.

import pandas as pd
import pandas_profiling as pp
df = pd.read_csv("mail_customers.csv") #import dataset into environment
print("first 5 rows ")
print(df.head()) #check if it has been imported correctly, shows first 5 records
print("Column headings ")
print(df.columns)# see what column headings are present
print("Last 5 rows ")
print(df.tail()) # check last 5 rows of dataset
#calculate basic mean/median/mode of numerical data
mean = df['Annual Income (k$)'].mean()
median = df['Annual Income (k$)'].median()
mode = df['Annual Income (k$)'].mode()
print("mean annual income (k$) =", mean)
print ("median annual income (k$) = ", median)
print ("mode annual income (k$) =", mode)
mean = df['Spending Score (1-100)'].mean()
median = df['Spending Score (1-100)'].median()
mode = df['Spending Score (1-100)'].mode()
print("mean Spending Score (1-100) =", mean)
print ("median Spending Score (1-100) = ", median)
print ("Spending Score (1-100) =", mode)
mean = df['Age'].mean()
median = df['Age'].median()
mode = df['Age'].mode()
print("mean Age =", mean)
print ("median Age = ", median)
print ("mode Age =", mode)

mean_income_gender = df.groupby("Genre")["Annual Income (k$)"].mean() #simple brackets for grouping by, square for data to be grouped
print("Average income per gender =",mean_income_gender)
df.loc[df["Age"]<20,"new cat"] = "under 20"
df.loc[(df["Age"]<30)&(df["Age"]>19),"new cat"] = "20 - 29"
df.loc[(df["Age"]<40)&(df["Age"]>29),"new cat"] = "30 - 39"
df.loc[(df["Age"]<50)&(df["Age"]>39),"new cat"] = "40 - 49"
df.loc[(df["Age"]<60)&(df["Age"]>49),"new cat"] = "50 - 59"
df.loc[df["Age"]>59,"new cat"] = "over 60"
mean_agec = df.groupby("new cat")["Annual Income (k$)"].mean()
print(mean_agec)
mean_spend = df.groupby("new cat")['Spending Score (1-100)'].mean()
print(mean_spend)



profile = pp.ProfileReport(df)
profile.to_file("Summaryreport.html") #takes a long time to run!