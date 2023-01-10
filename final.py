import os
import re
import csv
import numpy as np
import pandas as pd
from datetime import datetime
import statistics


mypath='C:\\Documents\\'


def main():
    FileNames = Files()


    #Gets the amount of files that are found within the path
    FileCount = len(FileNames)

    #Generates the date and time to give a unique name for the CSV file
    time = datetime.now().strftime("%Y_%m_%d-%I_%M_%S_%p")

    #Creates the titles for each column in the CSV file
    with open(f'C:\Documents\{time}.csv', 'a', newline='') as csvfile:
            fieldnames = ['filename', 'RVP max mean', 'RVP max std', 'dPdt max mean', 'dPdt min mean', 'dPdt min std', '15% mean', '15% std']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()


    #While loop that goes through each text file
    while (FileCount > 0):

        #Declares the path.
        path = 'C:\\Documents\\' + FileNames[FileCount-1]

        file = open(path)
        lines=file.readlines()


        #This looks for the number within the string. This was also going to be used to plot things but I didn't have enough time.
        TimeResolution = (re.findall('\d+', lines[1] ))[0]
        

        #Reads the text file in pandas.
        df = pd.read_csv(path, delimiter = '\t', skiprows = 8)
        #Gets the specified columns and filters out some random unneeded columns 
        temp = pd.DataFrame(df, columns= ['  I     ', '  II     ', '  FA     ', "  FA'" ,'  RV     ',"  RV'"])
        #Filters out all rows and only keeps rows that contain the character "E"
        database = temp[temp['  RV     '].astype(str).str.contains("E")]
        #Filters out all of the unwanted characters in the column
        database2 = temp[temp['  RV     '].astype(str).str.contains('E|S|D')==False]
        RV1 = temp["  RV'"]
        RV = database2['  RV     ']

        with open(f'C:\Documents\{time}.csv', 'a', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({'filename': FileNames[FileCount-1], 'RVP max mean': ('{RVP_max_mean}'), 'RVP max std': ('{RVP_max_mean}'), 'dPdt max mean': ('{dpdt_max_mean}'), 'dPdt min mean': ('{dpdt_max_std}'), 'dPdt min std': ('{dpdt_min_mean}'), '15% mean': ('{Mean_15}'), '15% std': ('{std_15}')})
        database.to_csv (r'C:\Documents\export_dataframe.csv', index = None, header=True)
        RV.to_csv(r'C:\Documents\export_RV.csv')
        RV1.to_csv(r'C:\Documents\export_RV1.csv')
        
        FileCount= FileCount - 1
        
def Calc(RV):
    Pmax = RV.max()
    
    RVP_max_std = np.std(Pmax)
    RVP_max_mean = statistics.mean(Pmax)
    
    Mean_15 = []
    std_15 = []
    return RVP_max_std
    return RVP_max_mean
    return Mean_15
    return std_15
    
def Calc1(RV1):
    dpdtmax = RV1.max()
    dpdtmin = RV1.min()
    thres = 0.15*[RV1.max()]
    index = RV1.find(RV1>thres)
    
    dpdt_max_mean = statistics.mean(dpdtmax)
    dpdt_max_std = np.std(dpdtmax)
    
    dpdt_min_mean = statistics.mean(dpdtmin)
    dpdt_min_std = np.std(dpdtmin)
    return dpdt_max_mean
    return dpdt_max_std
    return dpdt_min_mean
    return dpdt_min_std


def Files():
    #Array that holds the path for each file
    PatientFileArray = []
    #Counts all files in a directory 
    for path in os.listdir("C:\Documents"):
        if path.endswith(".txt"):
            PatientFileArray.append(path)
    return PatientFileArray