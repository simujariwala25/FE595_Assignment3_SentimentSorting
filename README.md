# FE595_Assignment3_SentimentSorting
This GitHub Repository is to perform Sentiment Sorting on the Companies Data set which includes Company name and Company Purpose. The dataset is formed by combining multiple 'csv' and 'text' files. The following Files will help you to understand and perform the code:

1. Merge_files.py : 
This file will help to combine the different formats into 1 csv which will be used in further files. There are 2 CSV's, the 1st is merged with a blank "Merged_files.csv" I created and then a merged csv file is created. The 2nd CSV is then merged with the "Merged_final_file.csv" file. Then the 2 text files are also appended to the "Merged_final_file.csv" and exported in the working directory.

2. Sentiment_Analysis.py : 
This file uses the final CSV from the previous python file and conducts sentiment analysis Vader Sentiment which gives a Compound Score.
Using the Compound Score, the best and worst business ideas are given using the min and max functions.

3. Sentiment_Sorting.py : 
Instead of using tokenization, NLTK; I have used Counter package from collections library, to read the text from the "Purpose" column and split words and find the most 10 repeated words. 
