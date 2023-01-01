import pandas as pd
import matplotlib.pyplot as plt


#importing the csv file that contains relevant data
#can be sourced from https://www.investindia.gov.in/states 
# or https://data.gov.in
df=pd.read_csv('data.csv')

#create our hypothetical compound variable
df['investment_prob']=df['gsdp']*df['population']
df['investment_prob']*=df['Ease of Doing Business Rank']
#HDI can be sourced from https://hdr.undp.org/data-center/human-development-index#/indicies/HDI
df['investment_prob']*=df['HDI/Human Development Index']

#removing unecessary columns
df.drop(columns=['gsdp'],inplace=True)
df.drop(columns=['Ease of Doing Business Rank'],inplace=True)
df.drop(columns=['population'],inplace=True)
df.drop(columns=['HDI/Human Development Index'],inplace=True)

#sorting the list in terms of our hypothetical index
df.sort_values(by='investment_prob',ascending=True)

#can use plt.plot for graphical purposes