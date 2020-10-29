import pandas as pd
import re

files = pd.read_csv("//Users//simranjariwala//PycharmProjects//pythonProject//Assignment_2.csv")
df = files.drop(files.columns[[0]], axis=1)


def csv_1():
    data = df
    sent_data = pd.read_csv("//Users//simranjariwala//PycharmProjects//pythonProject//Merged_files.csv")
    for i in range(len(data)):
        name = data.iloc[i, 0]
        purpose = data.iloc[i, 1]
        sent_data = sent_data.append({'Name': name, 'Purpose': purpose}, ignore_index=True)

    sent_data.to_csv("Merged_files1.csv", index=False)

csv_1()


def csv2(file):
    data = pd.read_csv(file)
    sentiment_data = pd.read_csv("//Users//simranjariwala//PycharmProjects//pythonProject//venv//Merged_files1.csv")
    for i in range(len(data)):
        name = data.iloc[i, 1]
        purpose = data.iloc[i, 2]
        sentiment_data = sentiment_data.append({'Name': name, 'Purpose': purpose}, ignore_index=True)

    sentiment_data.to_csv("Merged_files_final.csv", index=False)

csv2("//Users//simranjariwala//PycharmProjects//pythonProject//Simran_results_Assignment2.csv")


def text(File_Name):
    file1 = open(File_Name,"r")
    data = file1.read()
    rx_name = re.compile(r'Name: (?P<name>.*)\n')
    rx_purpose = re.compile(r'Purpose: (?P<purpose>.*)')
    names = rx_name.findall(data)
    purposes = rx_purpose.findall(data)

    senti_data = pd.read_csv("Merged_files_final.csv")
    for i in range(len(purposes)):
        senti_data = senti_data.append({'Name' : names[i], 'Purpose' : purposes[i]},ignore_index=True)

    senti_data.to_csv("Merged_files_final.csv",index=False)

text("//Users//simranjariwala//PycharmProjects//pythonProject//WebScrOutput.txt")
text("//Users//simranjariwala//PycharmProjects//pythonProject//Results2.txt")