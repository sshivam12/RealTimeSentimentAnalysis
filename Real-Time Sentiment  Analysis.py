#!/usr/bin/env python
# coding: utf-8

# In[1]:


from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
nltk.download('vader_lexicon')


# In[2]:


user_input = input("Please Rate Our Services >>: ")
sid = SentimentIntensityAnalyzer()
score = sid.polarity_scores(user_input)
print(score)


# In[3]:


user_input = input("Please Rate Our Services >>: ")
sid = SentimentIntensityAnalyzer()
score = sid.polarity_scores(user_input)
if score["neg"] != 0:
      print("Negative")
else:
      print("Positive")


# In[ ]:




