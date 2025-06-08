# Save the provided code into a downloadable Python file

code_content = """
import tweepy
import csv
import re
from textblob import TextBlob
import matplotlib.pyplot as plt

class SentimentAnalysis:

    def __init__(self):
        self.tweetText = []

    def DownloadData(self):
        # Twitter API v2 Bearer Token
        bearer_token = 'YOUR_BEARER_TOKEN_HERE'  # Replace this with your real token

        # Authenticate
        client = tweepy.Client(bearer_token=bearer_token)

        # User input
        searchTerm = input("Enter Keyword/Tag to search about: ")
        NoOfTerms = int(input("Enter how many tweets to search (max 100): "))
        if NoOfTerms > 100:
            print("Only up to 100 tweets allowed in basic tier. Using 100 tweets.")
            NoOfTerms = 100

        query = f"{searchTerm} -is:retweet lang:en"
        tweets = client.search_recent_tweets(query=query, max_results=NoOfTerms, tweet_fields=['text'])

        # Initialize counts
        polarity = 0
        positive = 0
        wpositive = 0
        spositive = 0
        negative = 0
        wnegative = 0
        snegative = 0
        neutral = 0

        # Save to CSV
        with open('/content/result.csv', 'w', newline='', encoding='utf-8') as csvFile:
            csvWriter = csv.writer(csvFile)
            csvWriter.writerow(["Tweet Text"])

            for tweet in tweets.data:
                cleaned = self.cleanTweet(tweet.text)
                self.tweetText.append(cleaned)
                csvWriter.writerow([cleaned])

                analysis = TextBlob(cleaned)
                pol = analysis.sentiment.polarity
                polarity += pol

                if pol == 0:
                    neutral += 1
                elif 0 < pol <= 0.3:
                    wpositive += 1
                elif 0.3 < pol <= 0.6:
                    positive += 1
                elif 0.6 < pol <= 1:
                    spositive += 1
                elif -0.3 < pol < 0:
                    wnegative += 1
                elif -0.6 < pol <= -0.3:
                    negative += 1
                elif -1 <= pol <= -0.6:
                    snegative += 1

        total = len(tweets.data)
        if total == 0:
            print("No tweets found.")
            return

        # Calculate percentages
        positive = self.percentage(positive, total)
        wpositive = self.percentage(wpositive, total)
        spositive = self.percentage(spositive, total)
        negative = self.percentage(negative, total)
        wnegative = self.percentage(wnegative, total)
        snegative = self.percentage(snegative, total)
        neutral = self.percentage(neutral, total)
        polarity = polarity / total

        # General Report
        print(f"\\nAnalyzed {total} tweets on '{searchTerm}'")
        print("General Sentiment:", self.getSentimentLabel(polarity))

        # Detailed Report
        print("\\nDetailed Sentiment Report:")
        print(f"Positive: {positive}%")
        print(f"Weakly Positive: {wpositive}%")
        print(f"Strongly Positive: {spositive}%")
        print(f"Negative: {negative}%")
        print(f"Weakly Negative: {wnegative}%")
        print(f"Strongly Negative: {snegative}%")
        print(f"Neutral: {neutral}%")

        self.plotPieChart(positive, wpositive, spositive, negative, wnegative, snegative, neutral, searchTerm, total)

    def cleanTweet(self, tweet):
        return ' '.join(re.sub(r"(@[A-Za-z0-9_]+)|([^0-9A-Za-z \\t])|(\\w+:\\/\\/\\S+)", " ", tweet).split())

    def percentage(self, part, whole):
        return format(100 * float(part) / float(whole), '.2f')

    def getSentimentLabel(self, polarity):
        if polarity == 0:
            return "Neutral"
        elif 0 < polarity <= 0.3:
            return "Weakly Positive"
        elif 0.3 < polarity <= 0.6:
            return "Positive"
        elif 0.6 < polarity <= 1:
            return "Strongly Positive"
        elif -0.3 < polarity < 0:
            return "Weakly Negative"
        elif -0.6 < polarity <= -0.3:
            return "Negative"
        elif -1 <= polarity <= -0.6:
            return "Strongly Negative"

    def plotPieChart(self, positive, wpositive, spositive, negative, wnegative, snegative, neutral, searchTerm, total):
        labels = [
            f'Positive [{positive}%]', f'Weakly Positive [{wpositive}%]', f'Strongly Positive [{spositive}%]',
            f'Neutral [{neutral}%]', f'Negative [{negative}%]', f'Weakly Negative [{wnegative}%]',
            f'Strongly Negative [{snegative}%]'
        ]
        sizes = [float(positive), float(wpositive), float(spositive), float(neutral),
                 float(negative), float(wnegative), float(snegative)]
        colors = ['yellowgreen', 'lightgreen', 'darkgreen', 'gold', 'red', 'lightsalmon', 'darkred']
        patches, _ = plt.pie(sizes, colors=colors, startangle=90)
        plt.legend(patches, labels, loc="best")
        plt.title(f'Sentiment on "{searchTerm}" from {total} Tweets')
        plt.axis('equal')
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    sa = SentimentAnalysis()
    sa.DownloadData()
"""

# Write the content to a Python file
file_path = "/mnt/data/twitter_sentiment_analysis.py"
with open(file_path, "w") as f:
    f.write(code_content)

file_path
