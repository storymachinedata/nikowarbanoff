import numpy as np
import altair as alt
import pandas as pd
import streamlit as st
from datetime import datetime, timedelta
import pytz
import re
import time
import datetime as dt
from helpers import *



st.set_page_config(layout="wide")

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


col1, col2= st.columns(2)

with col1:
	st.image("https://storymachine.mocoapp.com/objects/accounts/a201d12e-6005-447a-b7d4-a647e88e2a4a/logo/b562c681943219ea.png", width=200)
   
with col2:
	st.header("Data Team Dashboard")


st.title('Dobner: LinkedIn Keyword Search Monitoring')

st.image(
    "https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/LinkedIn_logo_initials.png/640px-LinkedIn_logo_initials.png",
    width=100,
)


with st.expander('Monitoring Keyword Search in LinkedIn everyday'):
	st.write('')

my_bar = st.progress(0)

for percent_complete in range(100):
	time.sleep(0.05)
	my_bar.progress(percent_complete + 1)


month = datetime.today().month
day = datetime.today().day

dobner_search_results = f'https://phantombuster.s3.amazonaws.com/UhrenaxfEnY/WVWDm0XnEmqgQ4iNu89Rkg/dobner_keywordSearchMonitor{month}_{day}.csv'

#dobner_search_results = 'https://phantombuster.s3.amazonaws.com/UhrenaxfEnY/WVWDm0XnEmqgQ4iNu89Rkg/dobner_keywordSearchMonitor1_23.csv'

						 #https://phantombuster.s3.amazonaws.com/UhrenaxfEnY/WVWDm0XnEmqgQ4iNu89Rkg/dobner_keywordSearchMonitor1_18.csv


df =pd.read_csv(dobner_search_results)
df = df.dropna(how='any', subset=['textContent'])
df.drop(['connectionDegree', 'timestamp'], axis=1, inplace=True)


df['postDate'] = df.postUrl.apply(getActualDate)
df = df.dropna(how='any', subset=['postDate'])
df['date'] =  pd.to_datetime(df['postDate'])
df.drop_duplicates(subset=['postUrl'], inplace=True)
df = df.reset_index(drop=True)
df['Total Interactions'] = df['likeCount'] + df['commentCount']
df['likeCount'] = df['likeCount'].fillna(0)
df['commentCount'] = df['commentCount'].fillna(0)
df['Total Interactions'] = df['Total Interactions'].fillna(0)
df['likeCount'] = df['likeCount'].astype(int)
df['commentCount'] = df['commentCount'].astype(int)
df['Total Interactions'] = df['Total Interactions'].astype(int)
df['Keyword']  = df['category']

df12 = df['query'].value_counts()

df.loc[(df['query']) == "https://www.linkedin.com/search/results/content/?datePosted=%22past-24h%22&heroEntityKey=urn%3Ali%3Aorganization%3A11870586&keywords=steuer&origin=FACETED_SEARCH&position=0&searchId=ad687b96-ac37-4dad-a72a-49ac8c08e75f&sid=fkq&sortBy=%22date_posted%22", "Keyword"] = "Steuer"
df.loc[(df['query']) == "https://www.linkedin.com/search/results/content/?datePosted=%22past-24h%22&keywords=steuern&origin=GLOBAL_SEARCH_HEADER&sid=MbM&sortBy=%22date_posted%22", "Keyword"] = "Steuer"
df.loc[(df['query']) == "https://www.linkedin.com/search/results/content/?datePosted=%22past-24h%22&keywords=Erbschaftssteuer&origin=GLOBAL_SEARCH_HEADER&sid=%2CPh&sortBy=%22date_posted%22", "Keyword"] = "Erbschaftssteuer"
df.loc[(df['query']) == "https://www.linkedin.com/search/results/content/?datePosted=%22past-24h%22&keywords=Grundsteuer&origin=GLOBAL_SEARCH_HEADER&sid=1I4&sortBy=%22date_posted%22", "Keyword"] = "Grundsteuer"
df.loc[(df['query']) == "https://www.linkedin.com/search/results/content/?datePosted=%22past-24h%22&heroEntityKey=urn%3Ali%3Aorganization%3A19970&keywords=elster&origin=FACETED_SEARCH&position=0&searchId=d3375d16-eaae-4d97-bf60-78dc566e2f08&sid=nah&sortBy=%22date_posted%22", "Keyword"] = "ELSTER"

df.loc[(df['query']) == "https://www.linkedin.com/search/results/content/?datePosted=%22past-24h%22&keywords=Finanzamt&origin=GLOBAL_SEARCH_HEADER&sid=JO~&sortBy=%22date_posted%22", "Keyword"] = "Finanzamt"
df.loc[(df['query']) == "https://www.linkedin.com/search/results/content/?datePosted=%22past-24h%22&keywords=Steuerrecht&origin=GLOBAL_SEARCH_HEADER&sid=Qn6&sortBy=%22date_posted%22", "Keyword"] = "Steuerrecht"
df.loc[(df['query']) == "https://www.linkedin.com/search/results/content/?datePosted=%22past-24h%22&keywords=tax%20law&origin=GLOBAL_SEARCH_HEADER&sid=~%2CM&sortBy=%22date_posted%22", "Keyword"] = "tax law"
df.loc[(df['query']) == "https://www.linkedin.com/search/results/content/?datePosted=%22past-24h%22&keywords=Internationales&origin=GLOBAL_SEARCH_HEADER&sid=ZvW&sortBy=%22date_posted%22", "Keyword"] = "Internationales"

df13 = df['Keyword'].value_counts()





st.write(f'last updated : {month}-{day}')
col1, col2 = st.columns(2)

with col1:
	st.header("Select Time Range")
	number = st.number_input('Select the days you want to see the posts', min_value=1, max_value=30, value=1, step=1)
	if number:
		df = df[df['date']>=(dt.datetime.now()-dt.timedelta(days=number))] #hours = 6,12, 24
		st.success(f'Monitor Posts from last {int(number)} Days', icon="✅")

with col2:
	st.header('Choose Filter') 
	option = st.selectbox(
    'How would you like to filter posts',
    ('Total Interactions','postDate'))
	st.success(f'Posts will filter based on  {option} ', icon="✅")
    
st.header("Choose Keyword to Search")

## major two tabs
search_results, account_monitor = st.tabs(['Linkedin Search Results', 'Account Monitoring'])

with search_results:
## subtab under search results tabs
	tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10, tab11, tab12, tab13, tab14 = st.tabs(["All", "Steuer", "ELSTER", "Grundsteuer", "Erbschaftssteuer", "Steuerrecht", "Finanzamt", "Internationales","Übererwerbsteuer","Tax Law", "Search for a Keyword Inside Posts","Rainer Holznagel","Christian Lindner","Dr. Dominik Benner"])
	df.sort_values([option], ascending=False, inplace=True)
	df_all = df
	df_renew = df.loc[df.Keyword == 'Steuer']
	df_renew = df_renew.reset_index(drop=True)
	df_wind = df.loc[df.Keyword == 'ELSTER']
	df_wind = df_wind.reset_index(drop=True)
	df_gru = df.loc[df.Keyword == 'Grundsteuer']
	df_gru = df_gru.reset_index(drop=True)
	df_erb = df.loc[df.Keyword == 'Erbschaftssteuer']
	df_erb = df_erb.reset_index(drop=True)
	df_Steuerrecht = df.loc[df.Keyword == 'Steuerrecht']
	df_Steuerrecht = df_Steuerrecht.reset_index(drop=True)
	df_fin = df.loc[df.Keyword == 'Finanzamt']
	df_fin = df_fin.reset_index(drop=True)
	df_intern = df.loc[df.Keyword == 'Internationales']
	df_intern = df_intern.reset_index(drop=True)
	df_tax = df.loc[df.Keyword == 'tax law']
	df_tax = df_tax.reset_index(drop=True)
	df_all['Hour'] = pd.to_datetime(df_all.postDate).dt.strftime("%H")
	df_renew['Hour'] = pd.to_datetime(df_renew.postDate).dt.strftime("%H")
	df_wind['Hour'] = pd.to_datetime(df_wind.postDate).dt.strftime("%H")
	df_gru['Hour'] = pd.to_datetime(df_gru.postDate).dt.strftime("%H")
	df_erb['Hour'] = pd.to_datetime(df_erb.postDate).dt.strftime("%H")



	with tab1:
		if st.button('Show All Data'):
			st.write(df_all)

		st.write(f'Total posts found in last Hours: ', df_all.shape[0])
		st.header(f'Most Recent Posts')
		st.info(f'Most recent posts appear based on {option}', icon="ℹ️")
	
		df_all = df_all.reset_index(drop=True)
		df_all_100 = df_all.head(200)
		num_posts = df_all.shape[0]

		if  num_posts>0:
			splits = df_all_100.groupby(df_all_100.index // 3)
			for _, frames in splits:
				frames = frames.reset_index(drop=True)
				thumbnails = st.columns(frames.shape[0])
				for i, c in frames.iterrows():
					with thumbnails[i]:
						printFunction(i, c, frames)               
		else:
			printError()



	with tab2:
		if st.button('Show Data with Keyword Steuer'):
			st.write(df_renew)

		st.write(f'Total posts found in last Hours: ', df_renew.shape[0])
		st.header(f'Most Recent Posts')
		st.info(f'Most recent posts appear based on {option}', icon="ℹ️")

		df_renew = df_renew.reset_index(drop=True)
		num_posts = df_renew.shape[0]

		if  num_posts>0:
			splits = df_renew.groupby(df_renew.index // 3)
			for _, frames in splits:
				frames = frames.reset_index(drop=True)
				thumbnails = st.columns(frames.shape[0])
				for i, c in frames.iterrows():
					with thumbnails[i]:
						printFunction(i, c, frames)                 
		else:
			printError()


	with tab3:
		if st.button('Show Data with Keyword ELSTER'):
			st.write(df_wind)

		st.write(f'Total posts found in last Hours: ', df_wind.shape[0])
		st.header(f'Most Recent Posts')
		st.info(f'Most recent posts appear based on {option}', icon="ℹ️")

		df_wind = df_wind.reset_index(drop=True)
		num_posts = df_wind.shape[0]

		if  num_posts>0:
			splits = df_wind.groupby(df_wind.index // 3)
			for _, frames in splits:
				frames = frames.reset_index(drop=True)
				thumbnails = st.columns(frames.shape[0])
				for i, c in frames.iterrows():
					with thumbnails[i]:
						printFunction(i, c, frames)
						
		else:
			printError()


	with tab4:
		if st.button('Show Data with Keyword Grundsteuer'):
			st.write(df_gru)

		st.write(f'Total posts found in last Hours: ', df_gru.shape[0])
		st.header(f'Most Recent Posts')
		st.info(f'Most recent posts appear based on {option}', icon="ℹ️")

		df_gru = df_gru.reset_index(drop=True)
		num_posts = df_gru.shape[0]

		if  num_posts>0:
			splits = df_gru.groupby(df_gru.index // 3)
			for _, frames in splits:
				frames = frames.reset_index(drop=True)
				thumbnails = st.columns(frames.shape[0])
				for i, c in frames.iterrows():
					with thumbnails[i]:
						printFunction(i, c, frames)               				
		else:
			printError()


	with tab5:
		if st.button('Show Data with Keyword Erbschaftssteuer'):
			st.write(df_erb)

		st.write(f'Total posts found in last Hours: ', df_erb.shape[0])
		st.header(f'Most Recent Posts')
		st.info(f'Most recent posts appear based on {option}', icon="ℹ️")

		df_erb = df_erb.reset_index(drop=True)
		num_posts = df_erb.shape[0]

		if  num_posts>0:
			splits = df_erb.groupby(df_erb.index // 3)
			for _, frames in splits:
				frames = frames.reset_index(drop=True)
				thumbnails = st.columns(frames.shape[0])
				for i, c in frames.iterrows():
					with thumbnails[i]:
							printFunction(i, c, frames)             
		else:
			printError()


	with tab6:

		if st.button('Show Data with Keyword Steuerrecht'):
			st.write(df_Steuerrecht)

		st.write(f'Total posts found in last Hours: ', df_Steuerrecht.shape[0])
		st.header(f'Most Recent Posts')
		st.info(f'Most recent posts appear based on {option}', icon="ℹ️")

		df_Steuerrecht = df_Steuerrecht.reset_index(drop=True)
		num_posts = df_Steuerrecht.shape[0]

		if  num_posts>0:
			splits = df_Steuerrecht.groupby(df_Steuerrecht.index // 3)
			for _, frames in splits:
				frames = frames.reset_index(drop=True)
				thumbnails = st.columns(frames.shape[0])
				for i, c in frames.iterrows():
					with thumbnails[i]:
						printFunction(i, c, frames)             
		else:
			printError()


	with tab7:
		if st.button('Show Data with Keyword Finanzamt'):
			st.write(df_fin)
		st.write(f'Total posts found in last Hours: ', df_fin.shape[0])
		st.header(f'Most Recent Posts')
		st.info(f'Most recent posts appear based on {option}', icon="ℹ️")
		df_fin = df_fin.reset_index(drop=True)
		num_posts = df_fin.shape[0]

		if  num_posts>0:
			splits = df_fin.groupby(df_fin.index // 3)
			for _, frames in splits:
				frames = frames.reset_index(drop=True)
				#print(frames.head())
				thumbnails = st.columns(frames.shape[0])
				for i, c in frames.iterrows():
					with thumbnails[i]:
						printFunction(i, c, frames)
		else:
			printError()


	with tab8:
		if st.button('Show Data with Keyword Internationales'):
			st.write(df_intern)

		st.write(f'Total posts found in last Hours: ', df_intern.shape[0])
		st.header(f'Most Recent Posts')
		st.info(f'Most recent posts appear based on {option}', icon="ℹ️")

		df_intern = df_intern.reset_index(drop=True)
		num_posts = df_intern.shape[0]

		if  num_posts>0:
			splits = df_intern.groupby(df_intern.index // 3)
			for _, frames in splits:
				frames = frames.reset_index(drop=True)
				#print(frames.head())
				thumbnails = st.columns(frames.shape[0])
				for i, c in frames.iterrows():
					with thumbnails[i]:
						printFunction(i, c, frames)      
		else:
			printError()


	with tab10:

		if st.button('Show Data with Keyword Tax Law'):
			st.write(df_tax)

		st.write(f'Total posts found in last Hours: ', df_tax.shape[0])
		st.header(f'Most Recent Posts')
		st.info(f'Most recent posts appear based on {option}', icon="ℹ️")

		df_tax = df_tax.reset_index(drop=True)
		num_posts = df_tax.shape[0]

		if  num_posts>0:
			splits = df_tax.groupby(df_tax.index // 3)
			for _, frames in splits:
				frames = frames.reset_index(drop=True)
				#print(frames.head())
				thumbnails = st.columns(frames.shape[0])
				for i, c in frames.iterrows():
					with thumbnails[i]:
						printFunction(i, c, frames)		
		else:
			printError()


	with tab9:
		printError()

	with tab12:
		printError()

	with tab13:
		printError()

	with tab14:
		printError()


	with tab11:
		title = st.text_input('Search for a keyword inside posts', 'sustainability')
		title = title.lower()
		df_all.textContent= df_all.textContent.str.lower()

		df_all['client'] = df_all.textContent.str.contains(title)
		df_search = df_all.loc[df_all.client == 1] 
		df_search = df_search.reset_index(drop=True)
		st.write(f'Posts found with keyword {title}:',df_search.shape[0])
		st.header(f'Posts which mention the keyword {title}')

		num_posts = df_search.shape[0]

		if  num_posts>0:
			splits = df_search.groupby(df_search.index // 3)
			for _, frames in splits:
				frames = frames.reset_index(drop=True)
				thumbnails = st.columns(frames.shape[0])
				for i, c in frames.iterrows():
					with thumbnails[i]:
						printFunction(i, c, frames)       		
		else:
			printError()





with account_monitor:
	acc_df = pd.read_csv('https://phantombuster.s3.amazonaws.com/UhrenaxfEnY/PB6agmKm3dPp5oU6GwuSXw/dobner_account_monitor.csv')
	acc_df = acc_df.dropna(how='any', subset=['postContent'])
	acc_df = acc_df.drop(columns = ['timestamp', 'error', 'postDate', 'viewCount'])
	acc_df['postDate'] = acc_df.postUrl.apply(getActualDate)
	acc_df['date'] =  pd.to_datetime(acc_df['postDate'])
	acc_df.drop_duplicates(subset=['postUrl'], inplace=True)
	acc_df = acc_df.reset_index(drop=True)
	acc_df['likeCount'] = acc_df['likeCount'].fillna(0).astype(int)
	acc_df['commentCount'] = acc_df['commentCount'].fillna(0).astype(int)
	acc_df['Total Interactions'] = acc_df['likeCount'] + acc_df['commentCount']
	acc_df['Total Interactions'] = acc_df['Total Interactions'].astype(int)
	acc_df['Account_Name'] = acc_df.profileUrl.apply(lambda x : url2name_mapper[x])
	acc_df['Branche'] = acc_df.profileUrl.apply(lambda x : url2Branch_mapper[x])
	acc_df.reset_index(drop=True, inplace=True)

	df.sort_values([option], ascending=False, inplace=True)

	if number:
		acc_df = acc_df[acc_df['date']>=(dt.datetime.now()-dt.timedelta(days=number))] #hours = 6,12, 24
		st.success(f'Monitor Posts from last {int(number)} Days', icon="✅")


	option_branch = st.selectbox(
    'How would you like to filter posts',
    ('All','Akademisch','Journalismus',
	'Politik', 'Steuerberater',
	'Unternehmer', 'Wirtschaftsinstitut',
	'Richter', 'Versicherungen'))
	st.success(f'Displaying Posts for account related to branch  {option_branch} ', icon="✅")
	printAccountInfo(acc_df, option_branch)


	#st.success(f'Posts will filter based on  {option} ', icon="✅")

