# codes for the project (only codes) :
# importing libraries that are required:
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os
#importing the file that is need to be analysed
df = pd.read_csv('final.csv')

top = int(input('top:'))
# questions :
#1
#1 Compute -- What are the top 10 Zipcodes for 911
print(df['zip'].value_counts().head(top))
#1 Question 1: Are Zipcodes 19446 and 19090 present ?

#2
#2 Compute -- What are the top 4 townships (twp) for 911 calls
df['twp'].value_counts()
town = str(input('enter town : '))
#2 Question 2: Which of the following township are not present? -- LOWER POTTSGROVE, NORRISTOWN,HORSHAM, ABINGTON
A = df['twp'].value_counts()
if  town not in A :
    print('town does not exist')
else:
    print('town exist')
# compute - Create new features
# apply() with a custom lambda expression to create a new column called "Reason" that contains this string value
df['reasons']=df['title'].apply(lambda title:title.split(':')[0])
# Question 3: What is the most common Reason for a 911 call based on Reason Column? Which comes second
df['reasons'].value_counts(5)
#4
#compute -- Plot barchart using matplot for 911 calls by Reason
plt.bar(df['title'].head(3),df['title'].value_counts().head(3))
plt.show()
# Question 4: How can you plot the bars horizontally ?
plt.barh(df['title'].head(3),df['title'].value_counts().head(3))
plt.show()
#5
#convert the timeStamp form str to DataTime objects

df['timeStamp']=pd.to_datetime(df['timeStamp'])
df['Date']=df['timeStamp'].apply(lambda t: t.date())
df['Day'] = df['timeStamp'].apply(lambda time:time.day)
df['Hour']=df['timeStamp'].apply(lambda time:time.hour)
df['Month']=df['timeStamp'].apply(lambda time: time.month)
df['Day of Week']=df['timeStamp'].apply(lambda time: time.dayofweek)
df['Day of Week'].unique()
dmap={0:'Monday',1:'Tuesday',2:'Wednesday',3:'Thursday',4:'Friday',5:'Saturday',6:'Sunday'}
df['Day of Week']=df['Day of Week'].map(dmap)
df['Day of Week'].unique()
df['Day of Week'].value_counts()

#7
sns.countplot(x=df['Month'], data=df,hue='reasons')
plt.legend(bbox_to_anchor=(1.05,1),loc=(2),borderaxespad=0.)
plt.show()

sns.countplot(x=df['Day of Week'],data=df,hue='twp')
plt.legend(bbox_to_anchor=(1.05,1),loc=(2),borderaxespad=0.)
plt.show()

sns.countplot(x=df['Day'],data=df,hue='zip')
plt.legend(bbox_to_anchor=(1.05,1),loc=(2),borderaxespad=0.)
plt.show()