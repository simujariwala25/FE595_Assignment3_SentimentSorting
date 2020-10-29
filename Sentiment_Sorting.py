from collections import Counter
import pandas as pd

data = pd.read_csv("//Users//simranjariwala//PycharmProjects//pythonProject//venv//Merged_files_final.csv")
top_10 = (Counter(" ".join(data["Purpose"].str.lower()).split()).most_common(10))
print(top_10)