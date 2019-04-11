# Questions
# Avg courses visited, time, lessons completed, projects
# How does this vary between students who completed projects and who didnt?
# Avg time to cancel. Does project completion relate at all to cancellation?
# Percent that have cancelled

# Import libraries
import pandas as pd
import numpy as np 
import datetime

# Import data as dataframes
df_engagement = pd.read_csv('../data/daily_engagement.csv')
df_enrollments = pd.read_csv('../data/enrollments.csv')
df_projects = pd.read_csv('../data/project_submissions.csv')

# Clean up data types 
df_enrollments['join_date'] = pd.to_datetime(df_enrollments['join_date'])
df_enrollments['cancel_date'] = pd.to_datetime(df_enrollments['cancel_date'])
df_engagement['utc_date'] = pd.to_datetime(df_engagement['utc_date'])
df_projects['creation_date'] = pd.to_datetime(df_projects['creation_date'])
df_projects['completion_date'] = pd.to_datetime(df_projects['completion_date'])

# Rename acct column in daily_engagement to account_key
df_engagement.rename(columns = {'acct' : 'account_key'}, inplace = True)

# Get count for unique accounts in each table
df_enrollments.account_key.nunique() # 1640 total, 1302 unique accounts
df_engagement.account_key.nunique() # 136240, 1237 unique accounts
df_projects.account_key.nunique() # 743 unique accounts

# Find rows in enrollment table that are not in engagement table
# Create indexes for both account key columns
en_index = pd.Index(df_enrollments.account_key)
daily_index = pd.Index(df_engagement.account_key)
difference = en_index.difference(daily_index)

# inspect difference
df_difference = df_enrollments.loc[df_enrollments['account_key'].isin(difference)]
df_difference.loc[(df_difference['days_to_cancel'].isnull()) | (df_difference['days_to_cancel'] > 0)]

# Remove test accounts (is_udacity = true)
df_enrollments = df_enrollments[df_enrollments.is_udacity is not True]
# Store indexes of test accounts in a df and then drop them 
indexTest = df_enrollments[df_enrollments['is_udacity']== True].index
df_enrollments.drop(indexTest, inplace = True)