import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer 
from sklearn.decomposition import NMF
import seaborn as sns
import matplotlib.pyplot as plt
import nltk
from nltk.corpus import stopwords

#Load data
df = pd.read_csv('amazon_clean4.csv')
df =df.dropna()

docs = df['review_body'].values

docs_label = [i[:30]+'...' for i in docs]

#Stop Words
STOP = stopwords.words('english')
STOP += ['one', 'even', 'city', 'sim', 'sims',
'simcity', 'cities', 'really', 'would', 'lot',
'playing', 'many', 'sonic', 'however', 'still',
'since', 'ever', 'way', 'use', 'played', 'also',
'cdata', 'game', 'games', 'windows', 'object', 'video', 'ps']

#CountVectorizer
vectorizer = CountVectorizer(stop_words=STOP, lowercase=True, token_pattern = r'(?u)\b[A-Za-z]+\b')
doc_word = vectorizer.fit_transform(docs)

#NMF Model
nmf_model = NMF(10)
doc_topic = nmf_model.fit_transform(doc_word)

#Display Topics Function
def display_topics(model, feature_names, no_top_words, topic_names=None):
    for ix, topic in enumerate(model.components_):
        if not topic_names or not topic_names[ix]:
            print('\nTopic ', ix)
        else:
            print('\nTopic: '',topic_names[ix],''')
        print(', '.join([feature_names[i]
                        for i in topic.argsort()[:-no_top_words - 1:-1]]))

#New Dataframe H
H = pd.DataFrame(doc_topic.round(5),
             index = docs_label,
             columns = ['game_content', 'download', 'online',
             'critique', 'negative_feedback', 'positive_feeback',
             'dlc', 'worthwhile', 'difficulty', 'performance'])

rating = df['star_rating']
product_title = df['product_title']

H = H.reset_index().join(rating)
H = H.join(product_title)

#Rating Count
rating_count = pd.DataFrame(H.groupby('product_title')['star_rating'].value_counts())
rating_count['count']=H.groupby('product_title')['star_rating'].value_counts()
rating_count = rating_count.drop(columns='star_rating')
rating_count = rating_count.reset_index()
rating_count['star_rating']=rating_count['star_rating'].astype(int)

#Encode H with Positive/Negative
H_new = H.set_index('index')
H_new['star_rating'] = H_new['star_rating'].replace([1,2], 'negative')
H_new['star_rating'] = H_new['star_rating'].replace([4,5], 'positive')


#Header/SideBar
st.title('Amazon Video Game Reviews')
st.sidebar.header('Pick a Game Title to Show Review Info About')
#Side Bar Select
game = st.sidebar.selectbox('Game Titles', sorted(H['product_title'].unique()))

button = st.button('Show Review Info')

if button:
    st.write(
        '''
        ## Review Info for {}
        '''.format(game))
    st.markdown('''---''')

    fig, ax = plt.subplots()
    data1= rating_count[rating_count['product_title']=='{}'.format(game)]
    fig, ax = plt.subplots()
    sns.barplot(data=data1, x='star_rating', y='count', ax=ax)
    ax.set(xlabel='Star Rating', ylabel='Count')
    st.pyplot(fig)

    st.write('Average Rating', H[H['product_title']=='{}'.format(game)].star_rating.mean())

    st.markdown('''---''')
    st.write('Positive Review Topics (4 & 5 Stars)')
    st.write(H_new.loc[(H_new['product_title'] == '{}'.format(game)) & (H_new['star_rating'] == 'positive')].mean().sort_values(ascending=False))
    st.write('Negative Review Topics (1 & 2 Stars)')
    st.write(H_new.loc[(H_new['product_title'] == '{}'.format(game)) & (H_new['star_rating'] == 'positive')].mean().sort_values(ascending=False))