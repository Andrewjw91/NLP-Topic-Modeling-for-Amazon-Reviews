# NLP Project WriteUp: Amazon Video Game Reviews

Andrew Wong

## Abstract

The goal of this project was to apply topic modeling tools and algorithms to process the raw text data from Amazon Video Game reviews. The topic model allowed me to perform exploratory data analysis to help determine the most relevant topics mentioned overall, and for specific game titles.

## Design

To preprocess the text data, I used sklearn's CountVectorizer. I applied this to an NMF (Non-Negative Matrix Facorization) topic model to output 10 topics. I set the word-token parameter to display the top 40 words categorized to each topic. This allowed me to examine the words/terms to add custom stop words to refine the topics, and to produce more defined topics.

Once I had the 10 topics that seemed to be relevant to the video game domain, I applied the topics to each document from the corpus. Through dimensionality reduction, the documents were transformed into numerical representations of the topics. Using aggregation algorithms, my model was able to return the average topic scores for a selected video game, filtered by positive and negative reviews. The business application of this model is that it can help provide insight to game developers the components they should continue to focus on for positive reception, as well as the components they need to address to improve their game.

My final product was an interactive Streamlit web app that allows users to select a game title and display the review statistics.

## Data

I downloaded my dataset as CSV from a Kaggle repository of Amazon reviews. I cleaned the data by removing rows with null values, and I removed rows with reviews less than 30 characters. There were many reviews containing only a few words (e.g. "Five Stars", "Great!", "Nice"), which would not contribute to insightful results. The cleaned dataset consisted of 124,650 review documents, and 3 columns (Product Title, Star Rating, Review Text). The date range of the reviews were from 2010 to 2015.

Below are the 10 topics that I subjectively labeled through the process of examining the top associated terms, and the documents with the highest expression of each topic. The top 15 terms are displayed as summary.

Topic  1 <b>(Game Content)</b>: story, well, first, much, level, character, world, make, combat, find, characters, player, system, different, two

Topic  2 <b>(Platform Availability)</b>: amazon, download, steam, code, buy, origin, work, account, card, install, purchase, product, bought, version, xbox

Topic  3 <b>(Online)</b>: play, online, ea, want, player, able, servers, server, hours, people, pc, mode, single, computer, players

Topic  4 <b>(Critique)</b>: like, feel, much, people, think, things, better, see, bad, thing, something, love, feels, look, little

Topic  5 <b>(Negative Feedback)</b>: get, buy, go, money, want, back, work, things, need, right, level, could, see, free, points

Topic  6 <b>(Positive Feedback)</b>: great, story, graphics, love, price, best, deal, well, buy, gameplay, recommend, xbox, series, awesome, worth

Topic  7 <b>(Downloadable Content)</b>: new, expansion, content, version, old, much, player, dlc, players, world, pack, original, better, release, features

Topic  8 <b>(Worthwhile)</b>: time, first, every, long, hours, back, take, go, money, times, find, around, try, going, start

Topic  9 <b>(Difficulty</b>: fun, much, love, easy, little, pretty, challenging, levels, recommend, hours, well, bit, worth, different, graphics

Topic  10 <b>(Performance)</b>: good, graphics, pretty, story, bad, pc, well, better, price, worth, nice, best, overall, sound, easy

## Algorithms/Models

As previously mentioned, I used NMF as my topic model with CountVectorizer for text feature extraction.

The primary aggregation algorithms used were: <br>
-Sorting algorithms to display the documents with the highest expression for the topic of choice. <br>
-Rating count distribution per game <br>
-Encoding 4 & 5 star reviews as 'positive', and 1 & 2 star reviews as 'negative', then calculating the respective mean topic score distributions. <br>
-Aggregation on game title, to display the mean topic scores, with filtering based on each star rating or by 'positive'/'negative'. <br>

## Results

Using my Streamlit web app, I chose to focus on the game - Tomb Raider. The Top 4 Positive Review Topics were: <br>

Positive Feedback - 0.0348 <br>
Difficulty - 0.0241<br>
Worthwhile - 0.0160 <br>
Downloadability - 0.0159<br>

The high expression in Difficulty and Downloadability can be useful to the game developer, as they are aspects they can control. The results indicate that people who liked this game appreciated the challenging aspect. If a game is too easy the gamer may become bored, whereas an adequately challenging game gives a sense of accomplishment. The results also indicate that the downloadability or platform availability experience was generally positive. <br>

Top 4 Negative Review Topics: <br>

Online - 0.0372<br>
Negative Feedback - 0.0260<br>
Platform Availability - 0.0252<br>
Performance - 0.0151<br>

The Online, Platform Availability, and Performance topics are notable as these all relate to technical user experience. The overall experience is more likely to be negative if the user is having issues connecting to the servers or downloading/purchasing the game. The same goes for Performance, if the game has many bugs and does not run well.

This is a practical application of how my topic model/Streamlit app can be used to provide useful insight/feedback to game developers in the video game industry. 

## Tools

Pandas - data manipulation <br>
Scikit-learn - CountVectorizer, NMF modeling<br>
NLTK - stop words<br>
Matplotlib, Seaborn - Visualization<br>
Streamlit - Web Application
