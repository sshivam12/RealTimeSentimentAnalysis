# RealTimeSentimentAnalysis

 **This repository demonstrates how to perform real-time sentiment analysis using Python. In this example, we use the Natural Language Toolkit (NLTK) library to analyze the sentiment of user input**

# Prerequisites

### Before running the code, make sure you have the NLTK library installed. You can install it using pip:

`pip install nltk
`
## You will also need to download the VADER lexicon data for sentiment analysis. You can do this by running the following code in your Jupyter notebook or Python script:

`from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
nltk.download('vader_lexicon')`

# Code Explanation
**We use the SentimentIntensityAnalyzer class from NLTK to perform sentiment analysis. Here's a breakdown of the code:**

`from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
nltk.download('vader_lexicon')`

# These lines import the necessary NLTK modules and download the VADER lexicon.

`user_input = input("Please Rate Our Services >>: ")
sid = SentimentIntensityAnalyzer()
score = sid.polarity_scores(user_input)
print(score)`

This code snippet takes user input and calculates sentiment scores using VADER. It prints the sentiment scores, which include 'neg' (negative), 'neu' (neutral), 'pos' (positive), and 'compound' scores.

`if score["neg"] != 0:
    print("Negative")
else:
    print("Positive")`

# Based on the 'neg' score, we determine whether the sentiment is positive or negative. If the 'neg' score is not equal to 0, we consider it negative; otherwise, it's positive.

[image] (https://github.com/sshivam12/RealTimeSentimentAnalysis/blob/main/image.png)

# Thank You 
