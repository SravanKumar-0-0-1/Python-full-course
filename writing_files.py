#Writing files:Files are used to store data in a file and read data from a file
#FILES are three types:normal files,json files,csv files

#normal file creation
file_path="files/text.txt"
with open(file_path,"w") as file:
    file.write("Hello World")
with open(file_path,"a") as file:
    file.write("\nthis is the second line")
    print("files is created")
#json file creation
import json
data={
    "name":"tej",
    "character":"gold",
    "stage":"mental"
}
file_path="files/text.json"
with open(file_path,"w") as file:
    json.dump(data,file,indent=4)
    print("json file is created")
#csv file creation
import csv
data=[
    ["name","character","stage"],
    ["tej","gold","mental"],
    ["sravan","diamond","intelligent"]
]
file_path="files/text.csv"
with open(file_path,"w") as file:
    writer=csv.writer(file)
    for row in data:
        writer.writerow(row)
    print("csv file is created")