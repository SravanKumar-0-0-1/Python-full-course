#Creation of file:Files are used to store data in a file and read data from a file
#FILES are three types:normal files,json files,csv files
#normal files are used to store text data   .txt
#json files are used to store data in json format  .json            
#csv files are used to store data in tabular format  .csv

# #normal file reading
file_path="files/text.txt"
with open(file_path,"r") as file:
    content=file.read()
    print(content)
#json file reading
import json
file_path="files/text.json"
with open(file_path,"r") as file:
    data=json.load(file)
    print(data)
#csv file reading
import csv
file_path="files\\text.csv"
with open(file_path,"r") as file:
    read=csv.reader(file)
    for row in read:
        print(row)