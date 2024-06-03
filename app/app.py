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

import plotly.express as px
import plotly.graph_objs as go

st.set_page_config(page_title="Portfolio Data Science", layout='wide')
st.title("Streamlit Sentiment Analysis App")
st.markdown('<style>div.block-container{padding-top:1rem;}</style>', unsafe_allow_html=True)
st.write("Welcome to my Streamlit app! This is a sentiment analysis project of tweets related to the 2024 Campaign in Indonesia")

import os

# Mendapatkan path ke direktori saat ini
current_directory = os.path.dirname(__file__)

# Membuat path ke file random_forest_model.joblib
file_path = os.path.join(current_directory, 'random_forest_model.joblib')
 
csv_url = 'https://raw.githubusercontent.com/huwaidanur/streamlit-sentimen-app/master/app/data_scraping_kampanye_prediksi_clean.csv'

options = ["Overview","All Data", "Positive", "Negative"]
selected_option = st.selectbox("Choose", options)

if selected_option == "Overview":
# =============================================================================================
# KONTAINER PERTAMA 
# = '#24d6e3'
    data = pd.read_csv(csv_url)
    data = pd.DataFrame(data, columns=['tweet', 'cleaned_tweet', 'cleaned_token', 'label'])
    with st.container():
        # row 1 dari 1 
        col1, col2 = st.columns([60, 40])
        with col1:
            data['cleaned_tweet'] = data['cleaned_tweet'].astype(str)
            word_lengths = data['cleaned_tweet'].str.split().apply(len)
            word_lengths_df = pd.DataFrame({'word_lengths': word_lengths})
            #st.dataframe(word_lengths)
            # = '#24d6e3'
            fig = go.Figure(data=[go.Histogram(x=word_lengths)])
            
            fig.update_layout(
                title='Number of Words per Tweet',
                xaxis_title=' Word Count',
                yaxis_title='Frequency',
                bargap=0.1,
                title_x=0.2,
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
            fig.update_layout(xaxis=dict(title=None), yaxis=dict(title=None), legend_title_text='Sentiment',yaxis_title='Frequency',
                            title_x=0.5, title_font_size=30, width=500, height=500)
            st.plotly_chart(fig, use_container_width=False)
            

    st.divider()


elif selected_option == "All Data":
# =============================================================================================
# KONTAINER KEDUA // ALL DATA =============================================================================================
# = '#24d6e3'

# Baca data
    data = pd.read_csv(csv_url)
    data = pd.DataFrame(data, columns=['tweet', 'cleaned_tweet', 'cleaned_token', 'label'])

    # Gaya untuk kontainer
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

    # Baris 1 dari 2
    col1, col2, col3 = st.columns([28, 34, 38])

    with col1:
        # Pie chart untuk distribusi sentiment
        sentiment_counts = data['label'].value_counts().reset_index()
        sentiment_counts.columns = ['label', 'count']
        fig = px.pie(sentiment_counts, names='label', values='count', title='Sentiment Distribution', template='plotly_dark')
        st.plotly_chart(fig, theme=None, use_container_width=True)

    with col2:
        data_ = data.copy()
        data_['cleaned_tweet'] = data_['cleaned_tweet'].astype(str)
        word_counts = Counter(data_['cleaned_tweet'].str.split().sum())
        top_10_words = dict(word_counts.most_common(10))
        
        # Membuat DataFrame dari top 10 kata teratas
        word_freq = pd.DataFrame(list(top_10_words.items()), columns=['word', 'frequency'])
        
        # Bar chart untuk kata paling umum
        fig = px.bar(word_freq, x='frequency', y='word', orientation='h', title='Top 10 Most Common Words')
        fig.update_layout(width=500, height=500, yaxis=dict(autorange="reversed", tickmode='linear', automargin=True))
        fig.update_traces(hovertemplate="<b>%{y}</b><br>Count=%{x}")
        st.plotly_chart(fig, theme=None, use_container_width=True)

    with col3:
        # Menghitung bigram
        data['cleaned_tweet'] = data['cleaned_tweet'].astype(str)
        all_tokens = [token for sublist in data['cleaned_tweet'].str.split() for token in sublist]
        bigram_counts = Counter(bigrams(all_tokens))
        top_10_bigrams = bigram_counts.most_common(10)
        
        # DataFrame untuk bigram
        bigram_freq = pd.DataFrame(top_10_bigrams, columns=['bigram', 'frequency'])
        bigram_freq['bigram'] = bigram_freq['bigram'].apply(lambda x: ' '.join(x))

        # Bar chart untuk bigram paling umum
        fig = px.bar(bigram_freq, x='frequency', y='bigram', orientation='h', title='Top 10 Most Common Bigrams')
        fig.update_layout(width=500, height=500, yaxis=dict(autorange="reversed", tickmode='linear', automargin=True))
        fig.update_traces(hovertemplate="<b>%{y}</b><br>Count=%{x}")
        st.plotly_chart(fig, theme=None, use_container_width=True)

    # Baris 2 dari 2
    col1, col2 = st.columns([60, 40])

    with col1:    
        df_ = data[['label', 'tweet']]
        st.write(df_)

    with col2:
        all_tokens = ' '.join(data['cleaned_tweet'])
        wordcloud = WordCloud(width=500, height=500, background_color='white').generate(all_tokens)
        fig = px.imshow(wordcloud.to_array(), title='Wordcloud')
        fig.update_layout(width=500, height=500, xaxis=dict(visible=False), yaxis=dict(visible=False))
        st.plotly_chart(fig, theme=None, use_container_width=True)

    # Divider
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

            labels = positive_data['label'].value_counts().index.tolist()
            values = positive_data['label'].value_counts().tolist()
 
            trace=go.Pie(labels=labels,
                        values=values,
                        hovertemplate = "%{label}: <br>Value: %{value} ",
                        textposition='inside',
                        )   
            data_pie_chart = [trace]
            fig = go.Figure(data=data_pie_chart)
            fig.update_layout(template="plotly_dark",
                              title='Sentiment Distribution', 
                              title_font_size=20, title_x=0.5)
            st.plotly_chart(fig, theme=None, use_container_width=True)   
        
        with col2:
            positive_data['cleaned_tweet'] = positive_data['cleaned_tweet'].astype(str)
            word_counts = Counter(positive_data['cleaned_tweet'].str.split().sum())
            top_10_words = dict(word_counts.most_common(10))
            
            # Membuat DataFrame dari top 10 kata teratas
            word_freq = pd.DataFrame(list(top_10_words.items()), columns=['word', 'frequency'])
            
            # Bar chart untuk kata paling umum
            fig = px.bar(word_freq, x='frequency', y='word', orientation='h', title='Top 10 Most Common Words')
            fig.update_layout(width=500, height=500,yaxis=dict(autorange="reversed", tickmode='linear', automargin=True))
            fig.update_traces(hovertemplate="<b>%{y}</b><br>Count=%{x}")
            st.plotly_chart(fig, theme=None, use_container_width=True)

        with col3:
            positive_data['cleaned_tweet'] = positive_data['cleaned_tweet'].astype(str)
            all_tokens = [token for sublist in positive_data['cleaned_tweet'].str.split() for token in sublist]
            bigram_counts = Counter(bigrams(all_tokens))
            top_10_bigrams = bigram_counts.most_common(10)

            bigram_freq = pd.DataFrame(top_10_bigrams, columns=['bigram', 'frequency'])
            bigram_freq['bigram'] = bigram_freq['bigram'].apply(lambda x : ' '.join(x))
            
            fig = px.bar(bigram_freq, x='frequency', y='bigram', orientation='h', title='Top 10 Most Common Bigrams')
            fig.update_layout(width=500,height=500,yaxis=dict(autorange="reversed", tickmode='linear', automargin = True))
            fig.update_traces(hovertemplate="<b>%{y}</b><br>Count=%{x}")
            st.plotly_chart(fig, theme=None, use_container_width=True) 
        
        # row 2 dari 2
        col1, col2 = st.columns([60, 40])
        with col1:
            df_positif = positive_data[['label', 'tweet']]
            st.write(df_positif)

        with col2:
            all_tokens = ' '.join(positive_data['cleaned_token'])
            wordcloud = WordCloud(width=800, height=800, background_color='white').generate(all_tokens)
            wordcloud_array = wordcloud.to_array()
            fig = px.imshow(wordcloud_array, title='Wordcloud')

            # Mengatur layout plot
            fig.update_layout(
                title='Wordcloud',
                title_font_size=20,title_x=0.5,
                width=500,height=500,
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
                title_font_size=20,
                title='Sentiment Distribution',
                title_x=0.5)
                            
            st.plotly_chart(fig, theme=None, use_container_width=True)   
            
        with col2:
            negative_data['cleaned_tweet'] = negative_data['cleaned_tweet'].astype(str)
            words = negative_data['cleaned_tweet'].str.split().sum()
            word_counts = Counter(words)
            top_10_words = dict(word_counts.most_common(10))
            
            # Membuat DataFrame dari top 10 kata teratas    
            word_freq = pd.DataFrame(list(top_10_words.items()), columns=['word', 'frequency'])

            fig = px.bar(word_freq, x='frequency', y='word', orientation='h', title='Top 10 Most Common Words')
            fig.update_layout(width=500,height=500,yaxis=dict(autorange="reversed", automargin=True))             
            fig.update_traces(hovertemplate="<b>%{y}</b><br>Count=%{x}")
            st.plotly_chart(fig, theme=None, use_container_width=True)

        with col3:
            negative_data['cleaned_tweet'] = negative_data['cleaned_tweet'].astype(str)
            all_tokens = [token for sublist in negative_data['cleaned_tweet'].str.split() for token in sublist]
            bigram_counts = Counter(bigrams(all_tokens))
            top_10_bigrams = bigram_counts.most_common(10)
            # Membuat DataFrame dari top 10 bigram teratas
            bigram_freq = pd.DataFrame(top_10_bigrams, columns=['bigram', 'frequency'])
            bigram_freq['bigram'] = bigram_freq['bigram'].apply(lambda x: ' '.join(x))

            fig = px.bar(bigram_freq, x='frequency', y='bigram', orientation='h', title='Top 10 Most Common Bigrams')
            fig.update_layout(width=500,height=500,yaxis=dict(autorange="reversed", automargin=True))  
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
            wordcloud_image = wordcloud.to_array()
            fig = px.imshow(wordcloud_image)

            # Mengatur layout plot
            fig.update_layout(
                title='Wordcloud',
                title_font_size=20,
                width=500,height=500,
                title_x=0.5,
                xaxis=dict(visible=False),
                yaxis=dict(visible=False))
            # Menampilkan wordcloud
            st.plotly_chart(fig, theme=None, use_container_width=True) 


    with st.container(height=30, border=False):
        pass
    st.divider()

# =============================================================================================
