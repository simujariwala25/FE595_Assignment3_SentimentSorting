from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pprint
import pandas as pd

data = pd.read_csv("//Users//simranjariwala//PycharmProjects//pythonProject//venv//Merged_files_final.csv")
analyzer = SentimentIntensityAnalyzer()

scores = []
# Declare variables for scores
compound_list = []
positive_list = []
negative_list = []
neutral_list = []

for i in range(data['Purpose'].shape[0]):
    compound = analyzer.polarity_scores(data['Purpose'][i])["compound"]
    pos = analyzer.polarity_scores(data['Purpose'][i])["pos"]
    neu = analyzer.polarity_scores(data['Purpose'][i])["neu"]
    neg = analyzer.polarity_scores(data['Purpose'][i])["neg"]

    scores.append({"Compound": compound,
                   "Positive": pos,
                   "Negative": neg,
                   "Neutral": neu
                   })

# Converting dictionary to dataframe
data = pd.DataFrame.from_dict(scores)

# Finding row with maximum compound score
print("The company with the best business idea after conducting Sentiment Analysis is: \n")
pprint.pprint(data[data.Compound == data.Compound.max()])

# Finding row with minimum compound score
print("The companies with the worst business idea after conducting Sentiment Analysis is: \n")
pprint.pprint(data[data.Compound == data.Compound.min()])

#data.to_csv("Merged_files2.csv", index=False)