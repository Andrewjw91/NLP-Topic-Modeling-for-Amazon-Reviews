# NLP Project MVP: Amazon (Video Game) Reviews

Andrew Wong

I used NMF as my topic model with CountVectorizer to create my word-token sparse matrix. After reviewing my initial topic model results, I did some EDA to try to get some better/more interpretable topics. I cleaned my review dataset to drop rows where reviews were less than 30 characters long. I also added some custom stop words that pertained to a particular game, because these words ended up as a corpus topic.

Here are the 10 topics produced by my model, with the top 15 associated terms:

Topic  0 <b>(performance)</b>:
game, playing, played, graphics, pc, first, hours, version, recommend, issues, make, ever, still, since, many

Topic  1 <b>(game_content)</b>:
also, well, level, story, character, much, way, first, world, use, make, combat, find, player, characters

Topic  2 <b>(platform_availability)</b>:
amazon, download, steam, code, buy, origin, account, card, work, purchase, install, product, xbox, bought, version

Topic  3 <b>(--hard to interpret, may remove)</b>:
games, played, steam, free, best, series, many, hidden, love, plus, pc, playing, first, price, sonic

Topic  4 <b>(online)</b>:
play, online, fun, playing, ea, want, player, servers, able, server, people, hours, still, players, single

Topic  5 <b>(user_feedback)</b>:
like, feel, much, people, think, things, better, bad, see, good, thing, something, feels, look, little

Topic  6 <b>(worth_money)</b>:
get, buy, go, money, way, back, want, work, things, need, right, could, got, good, free

Topic  7 <b>(positives)</b>:
great, good, fun, story, graphics, well, price, pretty, love, gameplay, worth, easy, much, recommend, bit

Topic  8 <b>(DLC)</b>:
new, still, expansion, content, version, much, old, dlc, also, pack, original, world, player, better, cdata

Topic  9 <b>(play_time)</b>:
time, first, long, every, hours, playing, back, take, go, played, money, way, around, going, times

This is a snippet from a document with a high expression for Topic 4 (online):

Update: As you can plainly see, with over 800 reviews on Amazon about this game, EA has really screwed up. I had about an hour to spare and I wanted to give this game another chance tonight so I loaded the game and tried to log in to the server where I have my saved game. Of course it was busy and I was put in a Queue. I now have to wait 19 minutes just to play this game. This is crazy, I paid $60 to sit here and wait and watch a clock countdown until I can play the game. Of course I can select another server, start the game all over, go through the tutorial for the 5th time if I wanted to play, but I have just about had enough.  Not worth the aggravation. Get with the program EA. <b>Internet Connection REQUIRED:As most other reviewers have stated, this game requires a Internet Connection to actually play the game. There is not a off-line single player component available as an option. Even if this is not a huge deal for you and you only play the game at home, EA\'s game servers are almost always too busy to actually use or they are not up. There are multiple servers available (East Coast and West Coast U.S. servers, or Eastern Europe and Western Europe and a few others), </b> but the problem is that whatever server you start your game on, is the server you must use again to continue your game. So if you start a game on a West Coast U.S. server last week, then want to continue playing your game today, you need to be on that same server. The problem is those servers are almost always too busy to join. SO you need to use another server, but your \\\\"saved game\\\\" is not available because it is on the server you used last week. Servers do not synch between each other.Crashing:There is also a huge problem with the game crashing...


## Future Work

I am currently in the process of applying the document-term sparse matrix to Regression models. I will assign 4&5 star reviews to a positive class, and 1&2 star reviews to a negative class. Using regression I want to determine the topics most associated with positive/negative reviews by examining the coefficients for each topic.


```python

```
