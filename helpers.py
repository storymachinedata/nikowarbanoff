import pandas as pd
import streamlit as st
from datetime import datetime
import re



name = 'myname'


url2name_mapper = {'https://www.linkedin.com/in/julia-jaekel/': 'Julia Jaekel',
 'https://www.linkedin.com/in/prof-dr-yasmin-wei%C3%9F-731a51157/': 'Prof. Dr. Yasmin Weiß',
 'https://www.linkedin.com/in/arnoldweissman/?originalSubdomain=de': 'Arnold Weissmann',
 'https://www.linkedin.com/in/marcel-fratzscher/': 'Marcel Fratzscher',
 'https://www.linkedin.com/in/claudia-kemfert-517598167/': 'Claudia Kemfert',
 'https://www.linkedin.com/in/dr-rainer-esser-b1670361/': 'Dr. Rainer Esser',
 'https://www.linkedin.com/in/sebastianmatthes/?originalSubdomain=de': 'Sebastian Matthes',
 'https://www.linkedin.com/in/larissa-holzki/': 'Larissa Holzki',
 'https://www.linkedin.com/in/ulf-poschardt-312278213/': 'Ulf Poschardt',
 'https://www.linkedin.com/in/thomasmkuhn/': 'Thomas M. Kuhn',
 'https://www.linkedin.com/in/claus-ruhe-madsen-017a81ab/': 'Claus Ruhe Madsen',
 'https://www.linkedin.com/in/ecs/': 'Ernst-Christoph Stolter',
 'https://www.linkedin.com/in/florian-toncar/': 'Dr. Florian Toncar',
 'https://www.linkedin.com/in/strack-zimmermann/': 'Marie-Agnes Strack-Zimmermann',
 'https://www.linkedin.com/in/salome-preiswerk-a0979b9/': 'Salome Preiswerk',
 'https://www.linkedin.com/in/matthias-loose-429b9098/': 'Matthias Loose',
 'https://www.linkedin.com/in/christian-wolsztynski-642134200/': 'Christian Wolsztynski',
 'https://www.linkedin.com/in/drhuening/recent-activity/': 'Dr. Michael Hüning',
 'https://www.linkedin.com/in/ralfheussner/': 'Ralf Heussner',
 'https://www.linkedin.com/in/stefan-ditsch/': 'Stefan Ditsch',
 'https://www.linkedin.com/in/j%C3%BCrgen-bauderer-6b88171/': 'Jürgen Bauderer',
 'https://www.linkedin.com/in/friedel-drees-00028366/': 'Friedel Drees',
 'https://www.linkedin.com/in/christian-klein/': 'Christian Klein',
 'https://www.linkedin.com/in/timh%C3%B6ttges/?locale=en_US': 'Tim Höttges',
 'https://www.linkedin.com/in/oliver-b%C3%A4te/?originalSubdomain=de': 'Oliver Bäte',
 'https://www.linkedin.com/in/werner-baumann/?originalSubdomain=de': 'Werner Baumann',
 'https://www.linkedin.com/in/frank-appel/?originalSubdomain=de': 'Frank Appel',
 'https://www.linkedin.com/in/naumeroekonom/': 'Dr. Hans-Joerg Naumer',
 'https://www.linkedin.com/in/volker-priebe-39b484/': 'Volker Priebe',
 'https://www.linkedin.com/in/andreas-peichl-67041812a/': 'Andreas Peichl',
 'https://www.linkedin.com/in/dr-johann-schachtner-98ab98103/': 'Johann Schachtner',
 'https://www.linkedin.com/in/stefan-bach-0a5b7077/': 'Stefan Bach'}

url2Branch_mapper = {'https://www.linkedin.com/in/julia-jaekel/': 'Akademisch',
 'https://www.linkedin.com/in/prof-dr-yasmin-wei%C3%9F-731a51157/': 'Akademisch',
 'https://www.linkedin.com/in/arnoldweissman/?originalSubdomain=de': 'Akademisch',
 'https://www.linkedin.com/in/marcel-fratzscher/': 'Akademisch',
 'https://www.linkedin.com/in/claudia-kemfert-517598167/': 'Akademisch',
 'https://www.linkedin.com/in/dr-rainer-esser-b1670361/': 'Journalismus',
 'https://www.linkedin.com/in/sebastianmatthes/?originalSubdomain=de': 'Journalismus',
 'https://www.linkedin.com/in/larissa-holzki/': 'Journalismus',
 'https://www.linkedin.com/in/ulf-poschardt-312278213/': 'Journalismus',
 'https://www.linkedin.com/in/thomasmkuhn/': 'Journalismus',
 'https://www.linkedin.com/in/claus-ruhe-madsen-017a81ab/': 'Politik',
 'https://www.linkedin.com/in/ecs/': 'Politik',
 'https://www.linkedin.com/in/florian-toncar/': 'Politik',
 'https://www.linkedin.com/in/strack-zimmermann/': 'Politik',
 'https://www.linkedin.com/in/salome-preiswerk-a0979b9/': 'Politik',
 'https://www.linkedin.com/in/matthias-loose-429b9098/': 'Richter',
 'https://www.linkedin.com/in/christian-wolsztynski-642134200/': 'Richter',
 'https://www.linkedin.com/in/drhuening/recent-activity/': 'Steuerberater',
 'https://www.linkedin.com/in/ralfheussner/': 'Steuerberater',
 'https://www.linkedin.com/in/stefan-ditsch/': 'Steuerberater',
 'https://www.linkedin.com/in/j%C3%BCrgen-bauderer-6b88171/': 'Steuerberater',
 'https://www.linkedin.com/in/friedel-drees-00028366/': 'Steuerberater',
 'https://www.linkedin.com/in/christian-klein/': 'Unternehmer',
 'https://www.linkedin.com/in/timh%C3%B6ttges/?locale=en_US': 'Unternehmer',
 'https://www.linkedin.com/in/oliver-b%C3%A4te/?originalSubdomain=de': 'Unternehmer',
 'https://www.linkedin.com/in/werner-baumann/?originalSubdomain=de': 'Unternehmer',
 'https://www.linkedin.com/in/frank-appel/?originalSubdomain=de': 'Unternehmer',
 'https://www.linkedin.com/in/naumeroekonom/': 'Versicherungen',
 'https://www.linkedin.com/in/volker-priebe-39b484/': 'Versicherungen',
 'https://www.linkedin.com/in/andreas-peichl-67041812a/': 'Wirtschaftsinstitut',
 'https://www.linkedin.com/in/dr-johann-schachtner-98ab98103/': 'Wirtschaftsinstitut',
 'https://www.linkedin.com/in/stefan-bach-0a5b7077/': 'Wirtschaftsinstitut'}



def getActualDate(url):
    a= re.findall(r"\d{19}", url)
    a = int(''.join(a))
    a = format(a, 'b')
    first41chars = a[:41]
    ts = int(first41chars,2)
    actualtime = datetime.fromtimestamp(ts/1000).strftime("%Y-%m-%d %H:%M:%S %Z")
    return actualtime





def printFunction(i, rows, dataframe):
   
    if not pd.isnull(rows['companyUrl']):
        st.subheader(rows.companyName)
        st.write('Company Account')
      
        st.info(rows['textContent'])
        st.write('Total Interactions 📈:  ',rows['Total Interactions'])
        st.write('Likes 👍:  ',rows['likeCount']) 
        st.write('Comments 💬:  ',rows['commentCount'])
        st.write('Publish Date & Time 📆:         ',rows['postDate']) #publishDate
        with st.expander('Link to this Post 📮'):
                st.write(rows['postUrl']) #linktoPost
        with st.expander('Link to  Profile 🔗'):
                st.write(rows['companyUrl']) #linktoProfile


    if not pd.isnull(rows['profileUrl']):
        #st.image(rows['profileImgUrl'], width=150)
        st.subheader(dataframe.fullName[i])
        st.write('Personal Account')
        st.write(rows['title']) #postType
        st.write('-----------')
       
        st.info(rows['textContent'])  #postrowsontent
        st.write('Total Interactions 📈:  ',rows['Total Interactions']) #totInterarowstions
        st.write('Likes 👍:  ',rows['likeCount']) #totInterarowstions
        st.write('Comments 💬:  ',rows['commentCount']) #totInterarowstions
        #st.write('Arowstion 📌:  ',rows['arowstion']) #totInterarowstions
        st.write('Publish Date & Time 📆:         ',rows['postDate']) #publishDate
        with st.expander('Link to this Post 📮'):
                st.write(rows['postUrl']) #linktoPost
        with st.expander('Link to  Profile 🔗'):
                st.write(rows['profileUrl']) #linktoProfile


def printError():
    st.image('https://img.freepik.com/premium-vector/hazard-warning-attention-sign-with-exclamation-mark-symbol-white_231786-5218.jpg?w=2000', width =200)
    st.subheader('Oops... No new post found in last Hours.')


def printAccountInfo(dataframe, option):
    if option != 'All':
        dataframe_copy = dataframe[dataframe.Branche == option]
    else:
        dataframe_copy = dataframe
    dataframe_copy = dataframe_copy.reset_index(drop=True)
    num_post = dataframe_copy.shape[0]
    st.write(f'There are {num_post}  posts: ')
    if num_post>0:
        splits = dataframe_copy.groupby(dataframe_copy.index//3)
        for _,frame in splits:
            frame = frame.reset_index(drop=True)
            thumbnail = st.columns(frame.shape[0])
            for i, row in frame.iterrows():
                with thumbnail[i]:
                    st.subheader(row['Account_Name'])
                    if not pd.isnull(row['imgUrl']):
                        st.image(row['imgUrl'])
                    st.info(row['postContent'])
                    st.write('Publish Date & Time 📆:         ',row['postDate'])
                    st.write('Total Interactions 📈:  ',row['Total Interactions'])
                    st.write('Likes 👍:  ',row['likeCount']) #totInteractions
                    st.write('Comments 💬:  ',row['commentCount']) #totInteractions
                    with st.expander('Link to this Post 📮'):
                        st.write(row['postUrl']) #linktoPost
                    with st.expander('Link to  Profile 🔗'):
                        st.write(row['profileUrl']) #linktoProfile
    else:
        st.image('https://img.freepik.com/premium-vector/hazard-warning-attention-sign-with-exclamation-mark-symbol-white_231786-5218.jpg?w=2000', width =200)
        st.subheader('Oops... No new post found for the selection.')

