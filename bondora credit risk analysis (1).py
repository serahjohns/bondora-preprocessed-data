#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import glob
import os
pd.set_option('display.max_columns',500)
import warnings
warnings.filterwarnings("ignore")


# In[2]:


# use glob to get all the csv files 
# in the folder
path = 'C:/Users/HP/OneDrive/Desktop/Bondora_raw'
csv_files = glob.glob(os.path.join(path, "*.csv"))
  
  
# loop over the list of csv files
for f in csv_files:
      
    # read the csv file
    df = pd.read_csv(f)
      
    # print the location and filename
    print('Location:', f)
    print('File Name:', f.split("\\")[-1])
      
    # print the content
    print('Content:')
    display(df)
    print()


# In[3]:


# settings to display all columns
pd.set_option("display.max_columns", None,"display.max_rows", None)
# display the dataframe head
df.head()


# In[4]:


df['Status'].value_counts()


# In[5]:


#to didplay only the column heads
df.columns.values


# In[6]:


msng_info = pd.DataFrame(df.isnull().sum().sort_values()).reset_index()
msng_info.rename(columns={'index':'col_name',0:'null_count'},inplace=True)
msng_info.head()


# In[7]:


msng_info['msng_pct'] = msng_info['null_count']/df.shape[0]*100
msng_info.head()


# In[8]:


msng_col = msng_info[msng_info['msng_pct']>=40]['col_name'].to_list()


# In[9]:


msng_col


# In[10]:


df_msng_rmvd=['RecoveryStage',
 'CreditScoreEeMini',
 'NextPaymentDate',
 'InterestAndPenaltyWriteOffs',
 'PrincipalWriteOffs',
 'PrincipalDebtServicingCost',
 'InterestAndPenaltyDebtServicingCost',
 'ContractEndDate',
 'PreviousEarlyRepaymentsBefoleLoan',
 'PlannedPrincipalTillDate',
 'CurrentDebtDaysSecondary',
 'DebtOccuredOnForSecondary',
 'ActiveLateLastPaymentCategory',
 'DebtOccuredOn',
 'CurrentDebtDaysPrimary',
 'ActiveLateCategory',
 'PlannedPrincipalPostDefault',
 'InterestRecovery',
 'PlannedInterestPostDefault',
 'EAD1',
 'EAD2',
 'PrincipalRecovery',
 'ReScheduledOn',
 'WorkExperience',
 'EmploymentPosition',
 'NrOfDependants',
 'CreditScoreFiAsiakasTietoRiskGrade',
 'Rating_V2',
 'GracePeriodEnd',
 'GracePeriodStart',
 'EL_V1',
 'Rating_V1',
 'CreditScoreEsEquifaxRisk',
 'EL_V0',
 'Rating_V0']


# In[11]:


df = df.drop(df_msng_rmvd,axis=1)


# In[12]:


df.head()


# In[13]:


df.columns


# In[14]:


cols_del = ['ReportAsOfEOD', 'LoanId', 'LoanNumber', 'ListedOnUTC', 'DateOfBirth',
       'BiddingStartedOn','UserName','NextPaymentNr',
       'NrOfScheduledPayments','IncomeFromPrincipalEmployer', 'IncomeFromPension',
       'IncomeFromFamilyAllowance', 'IncomeFromSocialWelfare',
       'IncomeFromLeavePay', 'IncomeFromChildSupport', 'IncomeOther','LoanApplicationStartedDate','ApplicationSignedHour',
       'ApplicationSignedWeekday','ActiveScheduleFirstPaymentReached', 'PlannedInterestTillDate',
       'ExpectedLoss', 'LossGivenDefault', 'ExpectedReturn',
       'ProbabilityOfDefault', 'PrincipalOverdueBySchedule',
       'StageActiveSince', 'ModelVersion','WorseLateCategory']


# In[15]:


df = df.drop(cols_del,axis=1)


# In[16]:


df.shape


# In[17]:


# let's find the counts of each status categories 
df['Status'].value_counts()


# In[18]:


# filtering out Current Status records
df_msng_rmvd2= df[df.Status !='Current']


# In[19]:


df_msng_rmvd2.shape


# In[20]:


df_msng_rmvd2.head(50)


# In[21]:


df_msng_rmvd2.columns


# In[23]:


df_msng_rmvd2.shape


# In[24]:


##pd.concat((pd.get_dummies(df.DefaultDate,columns=DefaultDate),pd.Dataframe(columns=DefaultDate))).fillna(0)


# In[25]:


df_DefaultDate1=df_msng_rmvd2["DefaultDate"]


# In[26]:


df_DefaultDate1


# In[27]:


##df_DefaultDate2 = pd.DataFrame(df_DefaultDate1)


# In[28]:


##df_DefaultDate2


# In[29]:


##df_DefaultDate2.columns


# In[30]:


##pd.get_dummies(df_msng_rmvd2 ,columns = ['DefaultDate'] ,dummy_na = True )


# In[31]:


##df_msng_rmvd2["DefaultDate"].value_counts()


# In[32]:


df_DefaultDate1.dtypes


# In[33]:


df_msng_rmvd2.dtypes


# In[34]:


df_msng_rmvd2["DefaultDate"].fillna("0", inplace = True)


# In[35]:


df_msng_rmvd2.head()


# In[36]:


df_msng_rmvd2["DefaultDate"] = np.where(df_msng_rmvd2["DefaultDate"] == "0", 0, 1)


# In[37]:


df_msng_rmvd2.shape


# In[38]:


df_msng_rmvd2.head(100)


# In[39]:


df_msng_rmvd2 = df_msng_rmvd2.drop('Status', axis=1)


# In[40]:


df_msng_rmvd2.shape


# In[41]:


df_msng_rmvd2["DefaultDate"].value_counts()


# In[42]:


#checking datatypes 
df.dtypes


# In[43]:


#checking the distribution of categorical variables
cat_data= df.select_dtypes('object')
data = df.drop(cat_data.columns, axis=1)


# In[44]:


data.head()


# In[45]:


bool_data= df.select_dtypes('bool')
data = df.drop(bool_data.columns, axis=1)


# In[46]:


#checking the distribution of all numeric columns
data.head()


# In[47]:


#checking the distribution of different categorical variavles
#for verification type
data['VerificationType'].value_counts().plot.bar(rot=0)


# In[48]:


#gender
data['Gender'].value_counts().plot.bar(rot=0)


# In[49]:


#language code
data['LanguageCode'].value_counts().plot.bar(rot=0)


# In[50]:


#use of loan
data['UseOfLoan'].value_counts().plot.bar(rot=0)


# In[51]:


#education
data['Education'].value_counts().plot.bar(rot=0)


# In[52]:


#marital status
data['MaritalStatus'].value_counts().plot.bar(rot=0)


# In[53]:


#employment status
data['EmploymentStatus'].value_counts().plot.bar(rot=0)


# In[54]:


#newcreditcustomer
bool_data['NewCreditCustomer'].value_counts().plot.bar(rot=0)


# In[55]:


#restructured
bool_data['Restructured'].value_counts().plot.bar(rot=0)


# In[56]:


#occupationarea
data['OccupationArea'].value_counts().plot.bar(rot=0)


# In[57]:


#homeownershiptype
data['HomeOwnershipType'].value_counts().plot.bar(rot=0)


# In[58]:


# save the final data
data.to_csv('Bondora_preprocessed.csv',index=False)


# In[59]:


df=pd.read_csv('Bondora_preprocessed.csv')


# In[ ]:


df.head()

