# importing panda library
import pandas as pd
import json, csv
import xml.etree.ElementTree as ET


def makeCSV(fileNme):
    # reading a given csv file and creating dataframe
    dataframe1 = pd.read_csv("HW2/NFL_stats.txt", delimiter = '\t', encoding = "ISO-8859-1")

    # Makes a CSV file
    csv = open("text_as_csv.csv", "w")
    csv.close()

    # storing this dataframe in a csv file
    dataframe1.to_csv('text_as_csv.csv', index = None)


def makeJSON(fileNme):
  
    dict1 = {}
    # read file 
    with open("HW2/NFL_stats.txt", encoding = "ISO-8859-1" ) as fn:
        CSV_reader = csv.DictReader(fn , delimiter = '\t')
        for row in CSV_reader:
            key = row["Year"]
            dict1[key] = row
            
     # Makes a JSON file
    jsonFile = ("text_as_json.json")
    with open(jsonFile, "w") as jsonf:
        jsonf.write(json.dumps(dict1, indent= 4))



def makeXML(fileNme):
    # users_list = ["GeeksForGeeks", "Arka", "Computer Science", "Engineering", "Portal"]
    # usrconfig = ET.Element("usrconfig")
    # usrconfig = ET.SubElement(usrconfig, "usrconfig")
    # for user in range(len( users_list)):
    pass

  


def makeFile(fileNme, dataType):
    dataType = dataType.lower()
    if(dataType == "c" ):
        makeCSV(fileNme)
    elif(dataType == "j"):
        makeJSON(fileNme)
    elif(dataType == "x"):
        makeXML(fileNme)
    else:
        print("error")

fileFormat = input("What type of file? CSV,JSON,XML\nC,J,X")

makeFile("HW2/NFL_stats.txt", fileFormat)
