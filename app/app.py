# library
import os
import nltk
import numpy as np
import pandas as pd
import streamlit as st

from nltk.util import bigrams
from collections import Counter
from wordcloud import WordCloud
from nltk.probability import FreqDist

#from utama import Utama
#from text_processing import TextProcessing
#from predict_sentiment import PredictSentiment
#from sklearn.feature_extraction.text import CountVectorizer

import plotly.express as px
import plotly.graph_objs as go

#import seaborn as sns
#import matplotlib.pyplot as plt

#tp = TextProcessing()
#ps = PredictSentiment()
#u = Utama()
# Set page title
st.set_page_config(page_title="Portofolio Data Science", layout='wide')
st.title("My Streamlit App")
st.markdown('<style>div.block-container{padding-top:1rem;}</style>', unsafe_allow_html=True)
st.write("Welcome to my Streamlit app! Di sini kamu bisa melihat hasil analisis sentimen Twitter")

  
if st.button("Topik : Kampanye"):
    st.write("Mari lihat sentimen terkait kampanye!")

    ''' 
    Analisis sentimen terkait trending topik di platform twitter bertujuan untuk memahami respon dan interaksi pengguna 
    terkait topik tertentu. Proyek ini dilakukan dengan harapan dapat memberi wawasan kepada pembaca mengenai opini publik 
    dengan membaca hasil tren dan perubahan persepsi yang sedang terjadi. 

    '''


nama_file = 'data_scraping_kampanye.csv'
folder_path = r'D:\Data Science - Sanbercode\belajar\Twitter_Sentimen_\app'

file_path = os.path.join(folder_path, nama_file)
#data = pd.read_csv(file_path)
csv_url = 'https://raw.githubusercontent.com/huwaidanur/streamlit-sentimen-app/master/app/data_scraping_kampanye_prediksi.csv'
#data = pd.read_csv(csv_url)
#from sklearn.feature_extraction.text import TfidfVectorizer
#from joblib import load, dump


# ubah dari pickle ke joblin
#model_pkl = load('random_forest_model.pkl')

#dump(model_pkl, 'random_forest_model.joblib')

# lakukan
# prediksi 
#def prediksi_label(data):
#    model = load('random_forest_model.joblib')
#    X = data['cleaned_tweet']
    #vectorizer = TfidfVectorizer(max_features = 500)
    #X_vector = vectorizer.fit_transform(X).toarray()
    #prediksi = model.predict(X_vector)
    #data['label'] = prediksi
    #return data

import os

# Mendapatkan path ke direktori saat ini
current_directory = os.path.dirname(__file__)

# Membuat path ke file random_forest_model.joblib
file_path = os.path.join(current_directory, 'random_forest_model.joblib')

#prediksi_label(data)
#data.to_csv('data_scraping_kampanye_prediksi.csv')
#print('data hasil prediksi berhasil disimpan')
 
csv_url = 'https://raw.githubusercontent.com/huwaidanur/streamlit-sentimen-app/master/app/data_scraping_kampanye_prediksi.csv'
#csv_url = 'https://raw.githubusercontent.com/huwaidanur/streamlit-sentimen-app/master/app/baru.csv'
data = pd.read_csv(csv_url)
data = pd.DataFrame(data, columns=['tweet', 'cleaned_tweet', 'cleaned_token', 'label'])
st.write(data.columns)
st.dataframe(data)
print(data.info())

options = ["Overview","All Data", "Positive", "Negative"]
selected_option = st.selectbox("Pilih", options)

if selected_option == "Overview":
# =============================================================================================
# KONTAINER PERTAMA 
# = '#24d6e3'
    data = pd.read_csv(csv_url)
    data = pd.DataFrame(data, columns=['tweet', 'cleaned_tweet', 'cleaned_token', 'label'])
    with st.container():
        # row 1 dari 1 
        col1, col2 = st.columns([50, 50])
        with col1:
            data['cleaned_tweet'] = data['cleaned_tweet'].astype(str)
            word_lengths = data['cleaned_tweet'].str.len()
            word_lengths_df = pd.DataFrame({'word_lengths': word_lengths})
            st.dataframe(word_lengths)
            # = '#24d6e3'
            fig = go.Figure(data=[go.Histogram(x=word_lengths)])
            
            fig.update_layout(
                title='Jumlah Kata per Tweet',
                xaxis_title=' Jumlah Kata',
                yaxis_title='Frekuensi',
                bargap=0.1,
                title_x=0.5,
                title_font_size=30,
                width=500,
                height=500)
            st.plotly_chart(fig, use_container_width=False)

        with col2:
            data = pd.DataFrame(data, columns=['tweet', 'cleaned_tweet', 'cleaned_token', 'label'])
            data_pie = data['label'].value_counts().reset_index()
            data_pie.columns = ['label', 'count']
            # = '#24d6e3'
            fig = px.bar(data_pie, x='label', y='count', color='label',
                        title='Sentiment', labels={'label': 'Labels', 'count': 'Counts'},
                        template='plotly', width=300, height=300)
            fig.update_traces(marker=dict(line=dict(width=2, color='Black')), showlegend=False)
            fig.update_layout(xaxis=dict(title=None), yaxis=dict(title=None), legend_title_text='Sentiment',
                            title_x=0.5, title_font_size=30, width=500, height=500, template='seaborn')
            st.plotly_chart(fig, use_container_width=False)

    st.divider()


elif selected_option == "All Data":
# =============================================================================================
# KONTAINER KEDUA // ALL DATA =============================================================================================
# = '#24d6e3'
    data = pd.read_csv(csv_url)
    data = pd.DataFrame(data, columns=['tweet', 'cleaned_tweet', 'cleaned_token', 'label'])
    color = '#3ecaed'
    with st.container():
        st.markdown(
            """
            <style>
                .css-1xkftc2 { /* Kelas untuk kontainer */
                    width: 800px !important;
                    height: 1200px !important;
                }
            </style>
            """,
            unsafe_allow_html=True
        )
        st.subheader('All Sentiment Data')
        # row 1 dari 2
        col1, col2, col3 = st.columns([28, 34, 38])
        with col1:
            #data_pie_counts = data['label'].value_counts()
            labels = data['label'].value_counts().index.tolist()
            values = data['label'].value_counts().tolist()
            #pd.Series(data_pie.index).tolist()
            #datavals = pd.Series(data_pie).tolist() 
            trace=go.Pie(labels=labels,
                        values=values,
                        hovertemplate = "%{label}: <br>Value: %{value} ",
                        textposition='inside',
                        )   
            data_pie_chart = [trace]
            # = '#24d6e3'
            fig = go.Figure(data=data_pie_chart)
            fig.update_layout(template="plotly_dark")
            st.plotly_chart(fig, theme=None, use_container_width=True)   
        with col2:
            #tv = TextVisual()
            #tv.plot_top_words(data)
            data['cleaned_tweet'] = data['cleaned_tweet'].astype(str)
            word_counts = Counter(data['cleaned_tweet'].str.split().sum())
            top_10_words = dict(word_counts.most_common(10))
            # = '#24d6e3'
            fig = go.Figure(data=[go.Bar(y=list(top_10_words.keys()), x=list(top_10_words.values()), orientation='h')])
            #fig = go.Figure(go.Bar(
            #   x=word_counts.values,
            #  y=word_counts.index,
            # orientation='h'), #=#)
            fig.update_layout(
                plot_bgcolor='white',
                title='Top 10 Most Common Words',
                xaxis_title='Frequency',
                yaxis_title='Word',
                title_x=0.5,
                title_font_size=20,
                width=500, height=500,
                xaxis=dict(type='category'),
                template='seaborn')
            fig.update_traces(hovertemplate="<b>%{y}</b><br>Count=%{x}")
            st.plotly_chart(fig, theme=None, use_container_width=True)  # Untuk membuat urutan bar dari atas ke bawah
            
        with col3:
            data['cleaned_token'] = data['cleaned_token'].astype(str)
            all_tokens = [token for sublist in data['cleaned_token'].str.split() for token in sublist]
            #tv.plot_top_bigrams(data)
            bigram_counts = Counter(bigrams(all_tokens))
            top_10_bigrams = bigram_counts.most_common(10)
            # = '#24d6e3'
            fig = go.Figure(go.Bar(
                x=[count for bigram, count in top_10_bigrams],
                y=[" ".join(bigram) for bigram, count in top_10_bigrams],
                orientation='h'))
            # Mengatur layout plot
            fig.update_layout(
                plot_bgcolor='white',
                title='Top 10 Most Common Bigrams',
                xaxis_title='Frequency',
                yaxis_title='Bigram',width=500, height=500,
                yaxis=dict(autorange="reversed"), template='seaborn')  # Untuk membuat urutan bar dari atas ke bawah
            fig.update_traces(hovertemplate="<b>%{y}</b><br>Count=%{x}")
            st.plotly_chart(fig, theme=None, use_container_width=True) 
        
        # row 2 dari 2
        col1, col2 = st.columns([50, 50])
        with col1:
            df_ = data[['label', 'tweet']]
            st.dataframe(df_)
        with col2:
            #tv.plot_wordcloud(data)
            all_tokens = ' '.join(data['cleaned_token'])
            wordcloud = WordCloud(width=500, height=500, background_color='white').generate(all_tokens)
            # = '#24d6e3'
            fig = go.Figure(go.Image(z=wordcloud.to_array()))

            # Mengatur layout plot
            fig.update_layout(
                title='Wordcloud',
                xaxis=dict(visible=False),
                yaxis=dict(visible=False), template='seaborn')
            # Menampilkan wordcloud
            st.plotly_chart(fig, theme=None, use_container_width=True) 

    with st.container(height=30, border=False):
        pass
    st.divider()


elif selected_option == "Positive":
# =============================================================================================
# KONTAINER KETIGA // POSITIVE =============================================================================================
    data = pd.read_csv(csv_url)
    data = pd.DataFrame(data, columns=['tweet', 'cleaned_tweet', 'cleaned_token', 'label'])
    positive_data = data[data['label'] == 'positif']
    data_visual_p = pd.DataFrame(positive_data['cleaned_token'])
    color = '#51f23f'
    with st.container():
        st.markdown(
        """
        <style>
            .css-1xkftc2 { /* Kelas untuk kontainer */
                width: 800px !important;
                height: 1200px !important;
            }
        </style>
        """,
        unsafe_allow_html=True
    )
        st.subheader('Positive Sentiment Data')
        # Plot pie chart for sentiment distribution
        # row 1 dari 2
        col1, col2, col3 = st.columns([28, 34, 38])
        with col1:
            #data_pie_counts = data['label'].value_counts()
            labels = positive_data['label'].value_counts().index.tolist()
            values = positive_data['label'].value_counts().tolist()
            #pd.Series(data_pie.index).tolist()
            #datavals = pd.Series(data_pie).tolist() 
            trace=go.Pie(labels=labels,
                        values=values,
                        hovertemplate = "%{label}: <br>Value: %{value} ",
                        textposition='inside',
                        )   
            data_pie_chart = [trace]
            fig = go.Figure(data=data_pie_chart)
            fig.update_layout(template="plotly_dark")
            st.plotly_chart(fig, theme=None, use_container_width=True)   
        # Display top words and top bigrams
        with col2:
            positive_data['cleaned_tweet'] = positive_data['cleaned_tweet'].astype(str)
            word_counts = Counter(positive_data['cleaned_tweet'].str.split().sum())
            top_10_words = dict(word_counts.most_common(10))
            # = '#24d6e3'
            fig = go.Figure(data=[go.Bar(y=list(top_10_words.keys()), x=list(top_10_words.values()), orientation='h')])
            fig.update_layout(
                plot_bgcolor='white',
                title='Top 10 Most Common Words',
                xaxis_title='Frequency',
                yaxis_title='Word',
                title_x=0.5,
                title_font_size=20,
                xaxis=dict(type='category'),
                template='seaborn')
            fig.update_traces(hovertemplate="<b>%{y}</b><br>Count=%{x}")
            st.plotly_chart(fig, theme=None, use_container_width=True)
        with col3:
            positive_data['cleaned_tweet'] = positive_data['cleaned_tweet'].astype(str)
            all_tokens = [token for sublist in positive_data['cleaned_token'].str.split() for token in sublist]
            #tv.plot_top_bigrams(data)
            bigram_counts = Counter(bigrams(all_tokens))
            top_10_bigrams = bigram_counts.most_common(10)
            # = '#24d6e3'
            fig = go.Figure(go.Bar(
                x=[count for bigram, count in top_10_bigrams],
                y=[" ".join(bigram) for bigram, count in top_10_bigrams],
                orientation='h'))
            # Mengatur layout plot
            fig.update_layout(
                plot_bgcolor='white',
                title='Top 10 Most Common Bigrams',
                xaxis_title='Frequency',
                yaxis_title='Bigram',
                yaxis=dict(autorange="reversed"))  # Untuk membuat urutan bar dari atas ke bawah
            fig.update_traces(hovertemplate="<b>%{y}</b><br>Count=%{x}")
            st.plotly_chart(fig, theme=None, use_container_width=True) 
        
        # row 2 dari 2
        col1, col2 = st.columns([60, 40])
        with col1:
            df_positif = positive_data[['label', 'tweet']]
            st.dataframe(df_positif)
        with col2:
            all_tokens = ' '.join(positive_data['cleaned_token'])
            wordcloud = WordCloud(width=800, height=800, background_color='white').generate(all_tokens)
            fig = go.Figure(go.Image(z=wordcloud.to_array()))

            # Mengatur layout plot
            fig.update_layout(
                title='Wordcloud',
                xaxis=dict(visible=False),
                yaxis=dict(visible=False))
            # Menampilkan wordcloud
            st.plotly_chart(fig, theme=None, use_container_width=True) 

    with st.container(height=30, border=False):
        pass
    st.divider()


elif selected_option == "Negative":
# =============================================================================================
# KONTAINER KEEMPAT // NEGATIVE =============================================================================================
    data = pd.read_csv(csv_url)
    data = pd.DataFrame(data, columns=['tweet', 'cleaned_tweet', 'cleaned_token', 'label'])
    negative_data = data[data['label'] == 'negatif']
    negative_data = pd.DataFrame(negative_data, columns=['tweet', 'cleaned_tweet', 'cleaned_token', 'label'])
    color = '#f2b13f'
    with st.container():
        st.markdown(
            """
            <style>
                .css-1xkftc2 { /* Kelas untuk kontainer */
                    width: 800px !important;
                    height: 1200px !important;
                }
            </style>
            """,
            unsafe_allow_html=True
        )
        st.subheader('Negative Sentiment Data')
        # Plot pie chart for sentiment distribution
        # row 1 dari 2
        col1, col2, col3 = st.columns([28, 34, 38])
        with col1:
            #data_pie_counts = data['label'].value_counts()
            labels = negative_data['label'].value_counts().index.tolist()
            values = negative_data['label'].value_counts().tolist()
            trace=go.Pie(labels=labels,
                        values=values,
                        hovertemplate = "%{label}: <br>Value: %{value} ",
                        textposition='inside',
                        )   
            data_pie_chart = [trace]
            # = '#24d6e3'
            fig = go.Figure(data=data_pie_chart)
            fig.update_layout(template="plotly_dark",
                title='Sentiment Distribution',
                title_x=0.5)
                            
            st.plotly_chart(fig, theme=None, use_container_width=True)   
        # Display top words and top bigrams
            
        with col2:
            negative_data['cleaned_tweet'] = negative_data['cleaned_tweet'].astype(str)
            #word_counts = Counter(negative_data['cleaned_tweet'].str.split().sum())
            words = negative_data['cleaned_tweet'].str.split().sum()
            word_counts = Counter(words)
            top_10_words = dict(word_counts.most_common(10))
            # = '#24d6e3'
            fig = go.Figure(data=[go.Bar(y=list(top_10_words.keys()), x=list(top_10_words.values()), orientation='h')])
            fig.update_layout(
                plot_bgcolor='white',
                title='Top 10 Most Common Words',
                xaxis_title='Frequency',
                yaxis_title='Word',
                title_x=0.5,
                title_font_size=20,
                xaxis=dict(type='category'),
                template='seaborn')
            fig.update_traces(hovertemplate="<b>%{y}</b><br>Count=%{x}")
            st.plotly_chart(fig, theme=None, use_container_width=True)

        with col3:
            negative_data['cleaned_token'] = negative_data['cleaned_token'].astype(str)
            all_tokens = [token for sublist in negative_data['cleaned_token'].str.split() for token in sublist]
            #tv.plot_top_bigrams(data)
            bigram_counts = Counter(bigrams(all_tokens))
            top_10_bigrams = bigram_counts.most_common(10)
            # = '#24d6e3'
            fig = go.Figure(go.Bar(
                x=[count for bigram, count in top_10_bigrams],
                y=[" ".join(bigram) for bigram, count in top_10_bigrams],
                orientation='h'))
            # Mengatur layout plot
            fig.update_layout(
                plot_bgcolor='white',
                title='Top 10 Most Common Bigrams',
                xaxis_title='Frequency',
                yaxis_title='Bigram',
                yaxis=dict(autorange="reversed"))  # Untuk membuat urutan bar dari atas ke bawah
            fig.update_traces(hovertemplate="<b>%{y}</b><br>Count=%{x}")
            st.plotly_chart(fig, theme=None, use_container_width=True)  
        # row 2 dari 2
        col1, col2 = st.columns([60, 40])
        with col1:
            df_negatif = negative_data[['label', 'tweet']]
            st.write(df_negatif)
        with col2:
            all_tokens = ' '.join(negative_data['cleaned_token'])
            wordcloud = WordCloud(width=800, height=800, background_color='white').generate(all_tokens)
            # = '#24d6e3'
            fig = go.Figure(go.Image(z=wordcloud.to_array()))

            # Mengatur layout plot
            fig.update_layout(
                title='Wordcloud',
                xaxis=dict(visible=False),
                yaxis=dict(visible=False))
            # Menampilkan wordcloud
            st.plotly_chart(fig, theme=None, use_container_width=True) 


    with st.container(height=30, border=False):
        pass
    st.divider()

# =============================================================================================
