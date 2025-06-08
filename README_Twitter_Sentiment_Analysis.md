
# 🐦 Twitter Sentiment Analysis using Tweepy & TextBlob

This project uses Twitter API (via Tweepy) and TextBlob for performing real-time sentiment analysis on tweets. It analyzes public sentiment toward a specific keyword or topic and presents the results visually using matplotlib.

## 📊 Output Example
Below is a sample analysis result for the keyword "fun" with a limit of 10 tweets:

```
Analyzed 10 tweets on 'fun'
General Sentiment: Weakly Positive

Detailed Sentiment Report:
Positive: 30.00%
Weakly Positive: 70.00%
Strongly Positive: 0.00%
Negative: 0.00%
Weakly Negative: 0.00%
Strongly Negative: 0.00%
Neutral: 0.00%
```

Pie chart output was generated as shown in the screenshot.

## 🛠 Features
- Real-time tweet fetching using Twitter API
- Tweet cleaning with regex
- Sentiment analysis using TextBlob
- Pie chart visualization of sentiment distribution
- Export analyzed tweets to a CSV file

## 🧪 How It Works
1. User Input: You enter a keyword and number of tweets to analyze.
2. Tweet Fetching: Tweets are collected using Tweepy.
3. Cleaning: Special characters and mentions are removed.
4. Sentiment Analysis: TextBlob is used to assign a polarity score to each tweet.
5. Classification: Tweets are categorized as:
   - Strongly Positive
   - Positive
   - Weakly Positive
   - Neutral
   - Weakly Negative
   - Negative
   - Strongly Negative
6. Visualization: Results are shown in a pie chart.

## 🔧 Technologies Used
Python, Tweepy, TextBlob, Matplotlib, CSV module, Regular Expressions (re)

## ⚙️ Requirements
Install dependencies with:

```
pip install tweepy textblob matplotlib
python -m textblob.download_corpora
```

## 📌 How to Run (Colab Instructions)
If you're using Google Colab:

```
!pip install tweepy textblob matplotlib
from textblob import download_corpora
download_corpora()
```

Then upload and run the script.

## ⚠️ Note
You must use your own Twitter Developer credentials (API keys and tokens) in the code to access the Twitter API.
