import numpy as np
import altair as alt
import pandas as pd
import streamlit as st
#import plotly.express as px
#from st_aggrid import AgGrid

#import pandas_profiling
#from streamlit_pandas_profiling import st_profile_report

from datetime import datetime,timedelta
import pytz
import re

#from germansentiment import SentimentModel

st.set_page_config(layout="wide")


with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

import time

col1,col2= st.columns(2)

with col1:
   #st.header("A cat")
   st.image("https://storymachine.mocoapp.com/objects/accounts/a201d12e-6005-447a-b7d4-a647e88e2a4a/logo/b562c681943219ea.png", width=200)
   
with col2:
   
   st.header("Data Team Dashboard")

st.sidebar.success("Choose Category")

st.title('LinkedIn Keyword Search Monitoring')

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





#st.balloons()

#st.header('`streamlit_pandas_profiling`')

#st.header('LinkedIn Keyword Search Monitor')



df =pd.read_csv('https://phantombuster.s3.amazonaws.com/UhrenaxfEnY/R7jpZMmKrJJJDoWyI7Ee5g/dobner_keyword_monitor.csv')
#df2 =pd.read_csv('https://phantombuster.s3.amazonaws.com/UhrenaxfEnY/FtuNWKMJKVUySGlR1lVmDg/live_windenergie.csv')
#df3 =pd.read_csv('https://phantombuster.s3.amazonaws.com/UhrenaxfEnY/JUeq71McCykmR5ZrlZTJdQ/Andere_CEOs_3.csv')

# df1.insert(len(df1.columns), 'Keyword', 'Renewable Energy')
# df2.insert(len(df2.columns), 'Keyword', 'Wind Energy')

# frames = [df1, df2]

# df = pd.concat(frames)


df = df.dropna(how='any', subset=['textContent'])


df.drop(['connectionDegree', 'timestamp'], axis=1, inplace=True)


def getActualDate(url):

    a= re.findall(r"\d{19}", url)

    a = int(''.join(a))

    a = format(a, 'b')

    first41chars = a[:41]

    ts = int(first41chars,2)

    #tz = pytz.timezone('Europe/Paris')

    actualtime = datetime.fromtimestamp(ts/1000).strftime("%Y-%m-%d %H:%M:%S %Z")

    return actualtime

df['postDate'] = df.postUrl.apply(getActualDate)


df = df.dropna(how='any', subset=['postDate'])


import datetime as dt

#def datenow(date):
     #a = re.(datetime.now() - df.postDate.days >1:)

#df5= df
#df5['date'] =  pd.to_datetime(df5['postDate'])
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




################
df['Keyword']  = df['category']
#st.write(df.head())
df12 = df['query'].value_counts()
#st.write(df12)





df.loc[(df['query']) == "https://www.linkedin.com/search/results/content/?datePosted=%22past-24h%22&keywords=steuer&origin=FACETED_SEARCH&sid=Fvt&sortBy=%22date_posted%22", "Keyword"] = "Steuer"
df.loc[(df['query']) == "https://www.linkedin.com/search/results/content/?datePosted=%22past-24h%22&keywords=steuern&origin=GLOBAL_SEARCH_HEADER&sid=MbM&sortBy=%22date_posted%22", "Keyword"] = "Steuer"
df.loc[(df['query']) == "https://www.linkedin.com/search/results/content/?datePosted=%22past-24h%22&keywords=erbschaftssteuer&origin=GLOBAL_SEARCH_HEADER&sid=(P%3A&sortBy=%22date_posted%22", "Keyword"] = "Erbschaftssteuer"
df.loc[(df['query']) == "https://www.linkedin.com/search/results/content/?datePosted=%22past-24h%22&keywords=grundsteuer&origin=GLOBAL_SEARCH_HEADER&sid=SUA&sortBy=%22date_posted%22", "Keyword"] = "Grundsteuer"
df.loc[(df['query']) == "https://www.linkedin.com/search/results/content/?datePosted=%22past-24h%22&keywords=ELSTER&origin=GLOBAL_SEARCH_HEADER&sid=GJC&sortBy=%22date_posted%22", "Keyword"] = "ELSTER"

df.loc[(df['query']) == "https://www.linkedin.com/search/results/content/?datePosted=%22past-month%22&keywords=Finanzamt&origin=FACETED_SEARCH&sid=2VO&sortBy=%22date_posted%22", "Keyword"] = "Finanzamt"
df.loc[(df['query']) == "https://www.linkedin.com/search/results/content/?datePosted=%22past-month%22&keywords=Steuerrecht&origin=GLOBAL_SEARCH_HEADER&sid=*C.&sortBy=%22date_posted%22", "Keyword"] = "Steuerrecht"

df13 = df['Keyword'].value_counts()
#st.write(df13)

#########################

st.header("Choose Keyword to Search")

tab1, tab2, tab3, tab4, tab5, tab6,tab7, tab8, tab9, tab10, tab11, tab12, tab13, tab14 = st.tabs(["All", "Steuer", "ELSTER", "Grundsteuer", "Erbschaftssteuer", "Steuerrecht", "Finanzamt", "Internationales","Übererwerbsteuer","tax law", "Search for a Keyword Inside Posts","Rainer Holznagel","Christian Lindner","Dr. Dominik Benner"])

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


df_all['Hour'] = pd.to_datetime(df_all.postDate).dt.strftime("%H")
df_renew['Hour'] = pd.to_datetime(df_renew.postDate).dt.strftime("%H")
df_wind['Hour'] = pd.to_datetime(df_wind.postDate).dt.strftime("%H")

df_gru['Hour'] = pd.to_datetime(df_gru.postDate).dt.strftime("%H")
df_erb['Hour'] = pd.to_datetime(df_erb.postDate).dt.strftime("%H")


with tab1:

   if st.button('Show All Data'):
      st.write(df_all)

   df_all = df_all[df_all['date']>=(dt.datetime.now()-dt.timedelta(days=1))] #hours = 6,12, 24
   st.write(f'Total posts found in last Hours: ', df_all.shape[0])
   st.subheader('Total Interaction getting in past hours in the day')
   st.bar_chart(df_all, x='Hour', y='Total Interactions')

   st.header(f'Top Interacting 100 Posts today')
   df_all.sort_values(['Total Interactions'], ascending=False, inplace=True)
   df_all = df_all.reset_index(drop=True)
   df_all_100 = df_all.head(100)
   num_posts = df_all_100.shape[0]

   if  num_posts>0:

     #splits = np.array_split(df5,5)
     splits = df_all_100.groupby(df_all_100.index // 3)
     for _, frames in splits:
          frames = frames.reset_index(drop=True)
          #print(frames.head())
          thumbnails = st.columns(frames.shape[0])
          for i, c in frames.iterrows():
               with thumbnails[i]:

                    if not pd.isnull(c['profileImgUrl']):
                        st.image(c['profileImgUrl'], width=150)
                    if not pd.isnull(c['profileUrl']):
                        #st.image(c['profileImgUrl'], width=150)
                        st.subheader(frames.fullName[i])
                        st.write('Personal Account')
                        st.write(c['title']) #postType
                        with st.expander('Post Content 📜'):
                             st.write(c['textContent'])  #postContent
                        st.write('Total Interactions 📈:  ',c['Total Interactions']) #totInteractions
                        st.write('Likes 👍:  ',c['likeCount']) #totInteractions
                        st.write('Comments 💬:  ',c['commentCount']) #totInteractions
                        #st.write('Action 📌:  ',c['action']) #totInteractions
                        st.write('Publish Date & Time 📆:         ',c['postDate']) #publishDate
                        with st.expander('Link to this Post 📮'):
                             st.write(c['postUrl']) #linktoPost
                        with st.expander('Link to  Profile 🔗'):
                             st.write(c['profileUrl']) #linktoProfile
                    
                    if not pd.isnull(c['logoUrl']):
                        st.image(c['logoUrl'], width=150)
                    
                        st.subheader(c['companyName'])
                        st.write('Corporate Account')
                        st.write('👥:  ',c['followerCount'])
                        with st.expander('Post Content 📜'):
                             st.write(c['textContent'])  #postContent
                        st.write('Total Interactions 📈:  ',c['Total Interactions']) #totInteractions
                        st.write('Likes 👍:  ',c['likeCount']) #totInteractions
                        st.write('Comments 💬:  ',c['commentCount']) #totInteractions
                        #st.write('Action 📌:  ',c['action']) #totInteractions
                        st.write('Publish Date & Time 📆:         ',c['postDate']) #publishDate
                        with st.expander('Link to this Post 📮'):
                             st.write(c['postUrl']) #linktoPost
                        with st.expander('Link to  Company Profile 🔗'):
                             st.write(c['companyUrl']) #linktoProfile
                        
                    
                    
                       

                    
                    #st.write('Type of Post 📨:  ',c['type']) #postType
                    
                    if not pd.isnull(c['postImgUrl']):
                        st.image(c['postImgUrl'])
                        st.write('Image from the Post  🗾')
                    
   else:
            st.image('https://img.freepik.com/premium-vector/hazard-warning-attention-sign-with-exclamation-mark-symbol-white_231786-5218.jpg?w=2000', width =200)
            st.subheader('Oops... No new post found in last Hours.')



with tab2:

   if st.button('Show Data with Keyword Steuer'):
      st.write(df_renew)

   df_renew = df_renew[df_renew['date']>=(dt.datetime.now()-dt.timedelta(days=1))] #hours = 6,12, 24
   st.write(f'Total posts found in last Hours: ', df_renew.shape[0])
   st.subheader('Total Interaction getting in past hours in the day')
   st.bar_chart(df_renew, x='Hour', y='Total Interactions')

   st.header(f'Top Interacting Posts today')
   df_renew.sort_values(['Total Interactions'], ascending=False, inplace=True)
   df_renew = df_renew.reset_index(drop=True)
   #df_renew_100 = df_renew.head(10)
   num_posts = df_renew.shape[0]

   if  num_posts>0:

     #splits = np.array_split(df5,5)
     splits = df_renew.groupby(df_renew.index // 3)
     for _, frames in splits:
          frames = frames.reset_index(drop=True)
          #print(frames.head())
          thumbnails = st.columns(frames.shape[0])
          for i, c in frames.iterrows():
               with thumbnails[i]:

                    if not pd.isnull(c['profileImgUrl']):
                        st.image(c['profileImgUrl'], width=150)
                    if not pd.isnull(c['profileUrl']):
                        #st.image(c['profileImgUrl'], width=150)
                        st.subheader(frames.fullName[i])
                        st.write('Personal Account')
                        st.write(c['title']) #postType
                        with st.expander('Post Content 📜'):
                             st.write(c['textContent'])  #postContent
                        st.write('Total Interactions 📈:  ',c['Total Interactions']) #totInteractions
                        st.write('Likes 👍:  ',c['likeCount']) #totInteractions
                        st.write('Comments 💬:  ',c['commentCount']) #totInteractions
                        #st.write('Action 📌:  ',c['action']) #totInteractions
                        st.write('Publish Date & Time 📆:         ',c['postDate']) #publishDate
                        with st.expander('Link to this Post 📮'):
                             st.write(c['postUrl']) #linktoPost
                        with st.expander('Link to  Profile 🔗'):
                             st.write(c['profileUrl']) #linktoProfile
                    
                    if not pd.isnull(c['logoUrl']):
                        st.image(c['logoUrl'], width=150)
                    
                        st.subheader(c['companyName'])
                        st.write('Corporate Account')
                        st.write('👥:  ',c['followerCount'])
                        with st.expander('Post Content 📜'):
                             st.write(c['textContent'])  #postContent
                        st.write('Total Interactions 📈:  ',c['Total Interactions']) #totInteractions
                        st.write('Likes 👍:  ',c['likeCount']) #totInteractions
                        st.write('Comments 💬:  ',c['commentCount']) #totInteractions
                        #st.write('Action 📌:  ',c['action']) #totInteractions
                        st.write('Publish Date & Time 📆:         ',c['postDate']) #publishDate
                        with st.expander('Link to this Post 📮'):
                             st.write(c['postUrl']) #linktoPost
                        with st.expander('Link to  Company Profile 🔗'):
                             st.write(c['companyUrl']) #linktoProfile
                        
                    
                    
                       

                    
                    #st.write('Type of Post 📨:  ',c['type']) #postType
                    
                    if not pd.isnull(c['postImgUrl']):
                        st.image(c['postImgUrl'])
                        st.write('Image from the Post  🗾')
                    
   else:
            st.image('https://img.freepik.com/premium-vector/hazard-warning-attention-sign-with-exclamation-mark-symbol-white_231786-5218.jpg?w=2000', width =200)
            st.subheader('Oops... No new post found in last Hours.')

with tab3:

   if st.button('Show Data with Keyword ELSTER'):
      st.write(df_wind)

   df_wind = df_wind[df_wind['date']>=(dt.datetime.now()-dt.timedelta(days=1))] #hours = 6,12, 24
   st.write(f'Total posts found in last Hours: ', df_wind.shape[0])
   st.subheader('Total Interaction getting in past hours in the day')
   st.bar_chart(df_wind, x='Hour', y='Total Interactions')

   st.header(f'Top Interacting Posts today')
   df_wind.sort_values(['Total Interactions'], ascending=False, inplace=True)
   df_wind = df_wind.reset_index(drop=True)
   #df_wind_100 = df_wind.head(10)
   num_posts = df_wind.shape[0]

   if  num_posts>0:

     #splits = np.array_split(df5,5)
     splits = df_wind.groupby(df_wind.index // 3)
     for _, frames in splits:
          frames = frames.reset_index(drop=True)
          #print(frames.head())
          thumbnails = st.columns(frames.shape[0])
          for i, c in frames.iterrows():
               with thumbnails[i]:

                    if not pd.isnull(c['profileImgUrl']):
                        st.image(c['profileImgUrl'], width=150)
                    if not pd.isnull(c['profileUrl']):
                        #st.image(c['profileImgUrl'], width=150)
                        st.subheader(frames.fullName[i])
                        st.write('Personal Account')
                        st.write(c['title']) #postType
                        with st.expander('Post Content 📜'):
                             st.write(c['textContent'])  #postContent
                        st.write('Total Interactions 📈:  ',c['Total Interactions']) #totInteractions
                        st.write('Likes 👍:  ',c['likeCount']) #totInteractions
                        st.write('Comments 💬:  ',c['commentCount']) #totInteractions
                        #st.write('Action 📌:  ',c['action']) #totInteractions
                        st.write('Publish Date & Time 📆:         ',c['postDate']) #publishDate
                        with st.expander('Link to this Post 📮'):
                             st.write(c['postUrl']) #linktoPost
                        with st.expander('Link to  Profile 🔗'):
                             st.write(c['profileUrl']) #linktoProfile
                    
                    if not pd.isnull(c['logoUrl']):
                        st.image(c['logoUrl'], width=150)
                    
                        st.subheader(c['companyName'])
                        st.write('Corporate Account')
                        st.write('👥:  ',c['followerCount'])
                        with st.expander('Post Content 📜'):
                             st.write(c['textContent'])  #postContent
                        st.write('Total Interactions 📈:  ',c['Total Interactions']) #totInteractions
                        st.write('Likes 👍:  ',c['likeCount']) #totInteractions
                        st.write('Comments 💬:  ',c['commentCount']) #totInteractions
                        #st.write('Action 📌:  ',c['action']) #totInteractions
                        st.write('Publish Date & Time 📆:         ',c['postDate']) #publishDate
                        with st.expander('Link to this Post 📮'):
                             st.write(c['postUrl']) #linktoPost
                        with st.expander('Link to  Company Profile 🔗'):
                             st.write(c['companyUrl']) #linktoProfile
                        
                    
                    
                       

                    
                    #st.write('Type of Post 📨:  ',c['type']) #postType
                    
                    if not pd.isnull(c['postImgUrl']):
                        st.image(c['postImgUrl'])
                        st.write('Image from the Post  🗾')
                    
   else:
            st.image('https://img.freepik.com/premium-vector/hazard-warning-attention-sign-with-exclamation-mark-symbol-white_231786-5218.jpg?w=2000', width =200)
            st.subheader('Oops... No new post found in last Hours.')




with tab4:

   if st.button('Show Data with Keyword Grundsteuer'):
      st.write(df_gru)

   df_gru = df_gru[df_gru['date']>=(dt.datetime.now()-dt.timedelta(days=1))] #hours = 6,12, 24
   st.write(f'Total posts found in last Hours: ', df_gru.shape[0])
   st.subheader('Total Interaction getting in past hours in the day')
   st.bar_chart(df_gru, x='Hour', y='Total Interactions')

   st.header(f'Top Interacting Posts today')
   df_gru.sort_values(['Total Interactions'], ascending=False, inplace=True)
   df_gru = df_gru.reset_index(drop=True)
   #df_gru_100 = df_gru_100.head(10)
   num_posts = df_gru.shape[0]

   if  num_posts>0:

     #splits = np.array_split(df5,5)
     splits = df_gru.groupby(df_gru.index // 3)
     for _, frames in splits:
          frames = frames.reset_index(drop=True)
          #print(frames.head())
          thumbnails = st.columns(frames.shape[0])
          for i, c in frames.iterrows():
               with thumbnails[i]:

                    if not pd.isnull(c['profileImgUrl']):
                        st.image(c['profileImgUrl'], width=150)
                    if not pd.isnull(c['profileUrl']):
                        #st.image(c['profileImgUrl'], width=150)
                        st.subheader(frames.fullName[i])
                        st.write('Personal Account')
                        st.write(c['title']) #postType
                        with st.expander('Post Content 📜'):
                             st.write(c['textContent'])  #postContent
                        st.write('Total Interactions 📈:  ',c['Total Interactions']) #totInteractions
                        st.write('Likes 👍:  ',c['likeCount']) #totInteractions
                        st.write('Comments 💬:  ',c['commentCount']) #totInteractions
                        #st.write('Action 📌:  ',c['action']) #totInteractions
                        st.write('Publish Date & Time 📆:         ',c['postDate']) #publishDate
                        with st.expander('Link to this Post 📮'):
                             st.write(c['postUrl']) #linktoPost
                        with st.expander('Link to  Profile 🔗'):
                             st.write(c['profileUrl']) #linktoProfile
                    
                    if not pd.isnull(c['logoUrl']):
                        st.image(c['logoUrl'], width=150)
                    
                        st.subheader(c['companyName'])
                        st.write('Corporate Account')
                        st.write('👥:  ',c['followerCount'])
                        with st.expander('Post Content 📜'):
                             st.write(c['textContent'])  #postContent
                        st.write('Total Interactions 📈:  ',c['Total Interactions']) #totInteractions
                        st.write('Likes 👍:  ',c['likeCount']) #totInteractions
                        st.write('Comments 💬:  ',c['commentCount']) #totInteractions
                        #st.write('Action 📌:  ',c['action']) #totInteractions
                        st.write('Publish Date & Time 📆:         ',c['postDate']) #publishDate
                        with st.expander('Link to this Post 📮'):
                             st.write(c['postUrl']) #linktoPost
                        with st.expander('Link to  Company Profile 🔗'):
                             st.write(c['companyUrl']) #linktoProfile
                        
                    
                    
                       

                    
                    #st.write('Type of Post 📨:  ',c['type']) #postType
                    
                    if not pd.isnull(c['postImgUrl']):
                        st.image(c['postImgUrl'])
                        st.write('Image from the Post  🗾')
                    
   else:
            st.image('https://img.freepik.com/premium-vector/hazard-warning-attention-sign-with-exclamation-mark-symbol-white_231786-5218.jpg?w=2000', width =200)
            st.subheader('Oops... No new post found in last Hours.')





with tab5:

   if st.button('Show Data with Keyword Erbschaftssteuer'):
      st.write(df_erb)

   df_erb = df_erb[df_erb['date']>=(dt.datetime.now()-dt.timedelta(days=1))] #hours = 6,12, 24
   st.write(f'Total posts found in last Hours: ', df_erb.shape[0])
   st.subheader('Total Interaction getting in past hours in the day')
   st.bar_chart(df_erb, x='Hour', y='Total Interactions')

   st.header(f'Top Interacting Posts today')
   df_erb.sort_values(['Total Interactions'], ascending=False, inplace=True)
   df_erb = df_erb.reset_index(drop=True)
   #df_gru_100 = df_gru_100.head(10)
   num_posts = df_erb.shape[0]

   if  num_posts>0:

     #splits = np.array_split(df5,5)
     splits = df_erb.groupby(df_erb.index // 3)
     for _, frames in splits:
          frames = frames.reset_index(drop=True)
          #print(frames.head())
          thumbnails = st.columns(frames.shape[0])
          for i, c in frames.iterrows():
               with thumbnails[i]:

                    if not pd.isnull(c['profileImgUrl']):
                        st.image(c['profileImgUrl'], width=150)
                    if not pd.isnull(c['profileUrl']):
                        #st.image(c['profileImgUrl'], width=150)
                        st.subheader(frames.fullName[i])
                        st.write('Personal Account')
                        st.write(c['title']) #postType
                        with st.expander('Post Content 📜'):
                             st.write(c['textContent'])  #postContent
                        st.write('Total Interactions 📈:  ',c['Total Interactions']) #totInteractions
                        st.write('Likes 👍:  ',c['likeCount']) #totInteractions
                        st.write('Comments 💬:  ',c['commentCount']) #totInteractions
                        #st.write('Action 📌:  ',c['action']) #totInteractions
                        st.write('Publish Date & Time 📆:         ',c['postDate']) #publishDate
                        with st.expander('Link to this Post 📮'):
                             st.write(c['postUrl']) #linktoPost
                        with st.expander('Link to  Profile 🔗'):
                             st.write(c['profileUrl']) #linktoProfile
                    
                    if not pd.isnull(c['logoUrl']):
                        st.image(c['logoUrl'], width=150)
                    
                        st.subheader(c['companyName'])
                        st.write('Corporate Account')
                        st.write('👥:  ',c['followerCount'])
                        with st.expander('Post Content 📜'):
                             st.write(c['textContent'])  #postContent
                        st.write('Total Interactions 📈:  ',c['Total Interactions']) #totInteractions
                        st.write('Likes 👍:  ',c['likeCount']) #totInteractions
                        st.write('Comments 💬:  ',c['commentCount']) #totInteractions
                        #st.write('Action 📌:  ',c['action']) #totInteractions
                        st.write('Publish Date & Time 📆:         ',c['postDate']) #publishDate
                        with st.expander('Link to this Post 📮'):
                             st.write(c['postUrl']) #linktoPost
                        with st.expander('Link to  Company Profile 🔗'):
                             st.write(c['companyUrl']) #linktoProfile
                        
                    
                    
                       

                    
                    #st.write('Type of Post 📨:  ',c['type']) #postType
                    
                    if not pd.isnull(c['postImgUrl']):
                        st.image(c['postImgUrl'])
                        st.write('Image from the Post  🗾')
                    
   else:
            st.image('https://img.freepik.com/premium-vector/hazard-warning-attention-sign-with-exclamation-mark-symbol-white_231786-5218.jpg?w=2000', width =200)
            st.subheader('Oops... No new post found in last Hours.')

with tab6:

   if st.button('Show Data with Keyword Steuerrecht'):
      st.write(df_Steuerrecht)

   df_Steuerrecht = df_Steuerrecht[df_Steuerrecht['date']>=(dt.datetime.now()-dt.timedelta(days=1))] #hours = 6,12, 24
   st.write(f'Total posts found in last Hours: ', df_Steuerrecht.shape[0])
   st.subheader('Total Interaction getting in past hours in the day')
   #st.bar_chart(df_Steuerrecht, x='Hour', y='Total Interactions')

   st.header(f'Top Interacting Posts today')
   df_Steuerrecht.sort_values(['Total Interactions'], ascending=False, inplace=True)
   df_Steuerrecht = df_Steuerrecht.reset_index(drop=True)
   #df_gru_100 = df_gru_100.head(10)
   num_posts = df_Steuerrecht.shape[0]

   if  num_posts>0:

     #splits = np.array_split(df5,5)
     splits = df_Steuerrecht.groupby(df_Steuerrecht.index // 3)
     for _, frames in splits:
          frames = frames.reset_index(drop=True)
          #print(frames.head())
          thumbnails = st.columns(frames.shape[0])
          for i, c in frames.iterrows():
               with thumbnails[i]:

                    if not pd.isnull(c['profileImgUrl']):
                        st.image(c['profileImgUrl'], width=150)
                    if not pd.isnull(c['profileUrl']):
                        #st.image(c['profileImgUrl'], width=150)
                        st.subheader(frames.fullName[i])
                        st.write('Personal Account')
                        st.write(c['title']) #postType
                        with st.expander('Post Content 📜'):
                             st.write(c['textContent'])  #postContent
                        st.write('Total Interactions 📈:  ',c['Total Interactions']) #totInteractions
                        st.write('Likes 👍:  ',c['likeCount']) #totInteractions
                        st.write('Comments 💬:  ',c['commentCount']) #totInteractions
                        #st.write('Action 📌:  ',c['action']) #totInteractions
                        st.write('Publish Date & Time 📆:         ',c['postDate']) #publishDate
                        with st.expander('Link to this Post 📮'):
                             st.write(c['postUrl']) #linktoPost
                        with st.expander('Link to  Profile 🔗'):
                             st.write(c['profileUrl']) #linktoProfile
                    
                    if not pd.isnull(c['logoUrl']):
                        st.image(c['logoUrl'], width=150)
                    
                        st.subheader(c['companyName'])
                        st.write('Corporate Account')
                        st.write('👥:  ',c['followerCount'])
                        with st.expander('Post Content 📜'):
                             st.write(c['textContent'])  #postContent
                        st.write('Total Interactions 📈:  ',c['Total Interactions']) #totInteractions
                        st.write('Likes 👍:  ',c['likeCount']) #totInteractions
                        st.write('Comments 💬:  ',c['commentCount']) #totInteractions
                        #st.write('Action 📌:  ',c['action']) #totInteractions
                        st.write('Publish Date & Time 📆:         ',c['postDate']) #publishDate
                        with st.expander('Link to this Post 📮'):
                             st.write(c['postUrl']) #linktoPost
                        with st.expander('Link to  Company Profile 🔗'):
                             st.write(c['companyUrl']) #linktoProfile
                        
                    
                    
                       

                    
                    #st.write('Type of Post 📨:  ',c['type']) #postType
                    
                    if not pd.isnull(c['postImgUrl']):
                        st.image(c['postImgUrl'])
                        st.write('Image from the Post  🗾')
                    
   else:
            st.image('https://img.freepik.com/premium-vector/hazard-warning-attention-sign-with-exclamation-mark-symbol-white_231786-5218.jpg?w=2000', width =200)
            st.subheader('Oops... No new post found in last Hours.')


with tab7:

   if st.button('Show Data with Keyword Finanzamt'):
      st.write(df_fin)

   df_fin = df_fin[df_fin['date']>=(dt.datetime.now()-dt.timedelta(days=1))] #hours = 6,12, 24
   st.write(f'Total posts found in last Hours: ', df_fin.shape[0])
   st.subheader('Total Interaction getting in past hours in the day')
   #st.bar_chart(df_Steuerrecht, x='Hour', y='Total Interactions')

   st.header(f'Top Interacting Posts today')
   df_fin.sort_values(['Total Interactions'], ascending=False, inplace=True)
   df_fin = df_fin.reset_index(drop=True)
   #df_gru_100 = df_gru_100.head(10)
   num_posts = df_fin.shape[0]

   if  num_posts>0:

     #splits = np.array_split(df5,5)
     splits = df_fin.groupby(df_fin.index // 3)
     for _, frames in splits:
          frames = frames.reset_index(drop=True)
          #print(frames.head())
          thumbnails = st.columns(frames.shape[0])
          for i, c in frames.iterrows():
               with thumbnails[i]:

                    if not pd.isnull(c['profileImgUrl']):
                        st.image(c['profileImgUrl'], width=150)
                    if not pd.isnull(c['profileUrl']):
                        #st.image(c['profileImgUrl'], width=150)
                        st.subheader(frames.fullName[i])
                        st.write('Personal Account')
                        st.write(c['title']) #postType
                        with st.expander('Post Content 📜'):
                             st.write(c['textContent'])  #postContent
                        st.write('Total Interactions 📈:  ',c['Total Interactions']) #totInteractions
                        st.write('Likes 👍:  ',c['likeCount']) #totInteractions
                        st.write('Comments 💬:  ',c['commentCount']) #totInteractions
                        #st.write('Action 📌:  ',c['action']) #totInteractions
                        st.write('Publish Date & Time 📆:         ',c['postDate']) #publishDate
                        with st.expander('Link to this Post 📮'):
                             st.write(c['postUrl']) #linktoPost
                        with st.expander('Link to  Profile 🔗'):
                             st.write(c['profileUrl']) #linktoProfile
                    
                    if not pd.isnull(c['logoUrl']):
                        st.image(c['logoUrl'], width=150)
                    
                        st.subheader(c['companyName'])
                        st.write('Corporate Account')
                        st.write('👥:  ',c['followerCount'])
                        with st.expander('Post Content 📜'):
                             st.write(c['textContent'])  #postContent
                        st.write('Total Interactions 📈:  ',c['Total Interactions']) #totInteractions
                        st.write('Likes 👍:  ',c['likeCount']) #totInteractions
                        st.write('Comments 💬:  ',c['commentCount']) #totInteractions
                        #st.write('Action 📌:  ',c['action']) #totInteractions
                        st.write('Publish Date & Time 📆:         ',c['postDate']) #publishDate
                        with st.expander('Link to this Post 📮'):
                             st.write(c['postUrl']) #linktoPost
                        with st.expander('Link to  Company Profile 🔗'):
                             st.write(c['companyUrl']) #linktoProfile
                        
                    
                    
                       

                    
                    #st.write('Type of Post 📨:  ',c['type']) #postType
                    
                    if not pd.isnull(c['postImgUrl']):
                        st.image(c['postImgUrl'])
                        st.write('Image from the Post  🗾')
                    
   else:
            st.image('https://img.freepik.com/premium-vector/hazard-warning-attention-sign-with-exclamation-mark-symbol-white_231786-5218.jpg?w=2000', width =200)
            st.subheader('Oops... No new post found in last Hours.')


with tab8:

   
            st.image('https://img.freepik.com/premium-vector/hazard-warning-attention-sign-with-exclamation-mark-symbol-white_231786-5218.jpg?w=2000', width =200)
            st.subheader('Oops... No new post found with the given keyword in last 24 Hours.')
with tab9:

   
            st.image('https://img.freepik.com/premium-vector/hazard-warning-attention-sign-with-exclamation-mark-symbol-white_231786-5218.jpg?w=2000', width =200)
            st.subheader('Oops... No new post found with the given keyword in last 24 Hours.')

with tab10:

   
            st.image('https://img.freepik.com/premium-vector/hazard-warning-attention-sign-with-exclamation-mark-symbol-white_231786-5218.jpg?w=2000', width =200)
            st.subheader('Oops... No new post found with the given keyword in last 24 Hours.')

with tab12:

   
            st.image('https://img.freepik.com/premium-vector/hazard-warning-attention-sign-with-exclamation-mark-symbol-white_231786-5218.jpg?w=2000', width =200)
            st.subheader('Oops...the data will be updated soon')

with tab13:

   
            st.image('https://img.freepik.com/premium-vector/hazard-warning-attention-sign-with-exclamation-mark-symbol-white_231786-5218.jpg?w=2000', width =200)
            st.subheader('Oops...the data will be updated soon')


with tab14:

   
            st.image('https://img.freepik.com/premium-vector/hazard-warning-attention-sign-with-exclamation-mark-symbol-white_231786-5218.jpg?w=2000', width =200)
            st.subheader('Oops...the data will be updated soon')

with tab11:


    
   #st.info('Search is c', icon="ℹ️")
   title = st.text_input('Search for a keyword inside posts', 'sustainability')
   title = title.lower()
   #title= f’\b{title}\b’
   #st.write( title)

   df_all.textContent= df_all.textContent.str.lower()

   df_all['client'] = df_all.textContent.str.contains(title)
   #df30['client'] = df30['textContent'].apply(lambda row: row.astype(str).str.contains(title).any())

   #st.write(df30['client'].value_counts())

   df_search = df_all.loc[df_all.client == 1] 
   df_search = df_search.reset_index(drop=True)
   st.write(f'Posts found with keyword {title}:',df_search.shape[0])
   #st.write(df_search)


   st.header(f'Posts which mention the keyword {title}')
   num_posts = df_search.shape[0]

   if  num_posts>0:

     #splits = np.array_split(df5,5)
     splits = df_search.groupby(df_search.index // 3)
     for _, frames in splits:
          frames = frames.reset_index(drop=True)
          #print(frames.head())
          thumbnails = st.columns(frames.shape[0])
          for i, c in frames.iterrows():
               with thumbnails[i]:

                    if not pd.isnull(c['profileImgUrl']):
                        st.image(c['profileImgUrl'], width=150)
                    if not pd.isnull(c['profileUrl']):
                        #st.image(c['profileImgUrl'], width=150)
                        st.subheader(frames.fullName[i])
                        st.write('Personal Account')
                        st.write(c['title']) #postType
                        with st.expander('Post Content 📜'):
                             st.write(c['textContent'])  #postContent
                        st.write('Total Interactions 📈:  ',c['Total Interactions']) #totInteractions
                        st.write('Likes 👍:  ',c['likeCount']) #totInteractions
                        st.write('Comments 💬:  ',c['commentCount']) #totInteractions
                        #st.write('Action 📌:  ',c['action']) #totInteractions
                        st.write('Publish Date & Time 📆:         ',c['postDate']) #publishDate
                        with st.expander('Link to this Post 📮'):
                             st.write(c['postUrl']) #linktoPost
                        with st.expander('Link to  Profile 🔗'):
                             st.write(c['profileUrl']) #linktoProfile
                    
                    if not pd.isnull(c['logoUrl']):
                        st.image(c['logoUrl'], width=150)
                    
                        st.subheader(c['companyName'])
                        st.write('Corporate Account')
                        st.write('👥:  ',c['followerCount'])
                        with st.expander('Post Content 📜'):
                             st.write(c['textContent'])  #postContent
                        st.write('Total Interactions 📈:  ',c['Total Interactions']) #totInteractions
                        st.write('Likes 👍:  ',c['likeCount']) #totInteractions
                        st.write('Comments 💬:  ',c['commentCount']) #totInteractions
                        #st.write('Action 📌:  ',c['action']) #totInteractions
                        st.write('Publish Date & Time 📆:         ',c['postDate']) #publishDate
                        with st.expander('Link to this Post 📮'):
                             st.write(c['postUrl']) #linktoPost
                        with st.expander('Link to  Company Profile 🔗'):
                             st.write(c['companyUrl']) #linktoProfile
                        
                    
                    
                       

                    
                    #st.write('Type of Post 📨:  ',c['type']) #postType
                    
                    if not pd.isnull(c['postImgUrl']):
                        st.image(c['postImgUrl'])
                        st.write('Image from the Post  🗾')
                    
   else:
            st.image('https://img.freepik.com/premium-vector/hazard-warning-attention-sign-with-exclamation-mark-symbol-white_231786-5218.jpg?w=2000', width =200)
            st.subheader(f'Oops... No new post found with keyword {title}.')



