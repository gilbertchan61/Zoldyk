# importing panda library
import pandas as pd
import json, csv  
from xml.dom import minidom 
import os 
import xml.etree.ElementTree as ET
import xml.etree.ElementTree as ET
from lxml import etree
import sys



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
    root = etree.Element('data')
    with open("HW2/NFL_stats.txt", encoding="UTF-8") as xmlf:
        csv_reader = csv.DictReader(xmlf, delimiter='\t')
        header = next(csv_reader)
        for row in csv_reader:
            eg = etree.SubElement(root, 'eg')
        for h, v in zip(header, row):
            etree.SubElement(eg, h).text = v

    xml_file = 'text_as_xml.xml'
    f = open(xml_file, "w")
    f.write(etree.tostring(root))
    f.close()

# def makeXML(fileNme):
#     root = etree.Element('data')
#     with open(fileNme, encoding="ISO-8859-1") as xmlf:
#         xml_file = 'text_as_xml.xml'
#         txtReader = csv.reader(root , delimiter = '\t')
#         data = []
#         temp = []
#         next(txtReader)
#         with open(xml_file, 'w') as fh:
#             for i in txtReader:
#                 fh.write(f"""<Year>{i[0]}</Year>
#     <Player>{i[1]}</Player>
#     <Age>{i[2]}</Age>
#     <Hometown>{i[3]}</Hometown>
#     <State>{i[4]}</State>
#     <Tm>{i[5]}</Tm>
#     <G>{i[6]}</G>
#     <GS>{i[7]}</GS>
#     <Cmp>{i[8]}</Cmp>
#     <Att>{i[9]}</Att>
#     <Yds>{i[10]}</Yds>
#     <TD>{i[11]}</TD>
#     <Int>{i[12]}</Int>
#     <Att>{i[13]}</Att>
#     <Yds>{i[14]}</Yds>
#     <Y/A>{i[15]}</Y/A>
#     <TD>{i[16]}</TD>
#     <Rec>{i[17]}</Rec>
#     <Yds>{i[18]}</yDs>
#     <Y/R>{i[19]}</Y/R>
#     <TD>{i[20]}</TD>
#     <FantPos>{i[21]}</FantPos>
#     <FantPt>{i[22]}</FantPt>
#     <Height (inches)>{i[23]}</Height (inches)>
#     <Weight>{i[24]}</Weight>
#     <College>{i[25]}</College>
#     <Conference>{i[26]}</Conference>
#     <College wins>{i[27]}</College wins>
#     <College losses>{i[28]}</College losses>
#     <DOB>{i[29]}</DOB>
#     <Draft Round>{i[30]}</Draft Round>
#     <Draft Year>{i[31]}</Draft Year>
#     <Wonderlic>{i[32]}</Wonderlic> 
#     <40 Yard>{i[33]}</40 Yard> 
#     <Bench Press>{i[34]}<Bench Press>
#     <Vert Leap(in)>{i[35]}</Vert Leap(in)>
#     <Broad Jump(in)>{i[36]}</Broad Jump(in)>
#     <Shuttle>{i[37]}</Shuttle>
#     <3Cone>{i[38]}</3Cone>
#     """)
#     fh.close()

   
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

fileFormat = input("What type of file? CSV,JSON,XML\nC,J,X: ")

makeFile("HW2/NFL_stats.txt", fileFormat)
