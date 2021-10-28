"""
    Parser to create a JSON from
    the given Lawfile from the Bundesgit

    author:     Manuel Kreft
    date:       28.10.2021
    version:    1.0.0

    Created following the DHBW course:
    WebEngineering II
"""

#=====Imports=========================================
import os
import re
import json


#=====Functions=======================================
def createJson(lawlist):
    """
    Writes the laws and information to a json file
    param - {obj} - lawlist - Holding all laws as list of dictionarys
    """
    with open('/home/manuel/Dokumente/Gesetze/laws.json','w+',encoding='utf-8') as fileoutput:
        json.dump(lawlist,fileoutput,indent=4)



def extractLawInformation(law_list):
    '''
    Iterates over a list of filepaths and extracts all necessary information
    param - {list} - list of strings containing filepaths
    '''
    laws_with_extracted_information = {}


    for lawfile in law_list:
            with open(lawfile,'r') as s:                
                extraction = str(s.read()).split("---")
                title,abk = extractHeaderInformation(extraction[1])
                ausfertigung,fundstelle = extractBodyInformation(extraction[2])
                path = str(lawfile)
                lawvalues = {'title':title,'abreviation':abk,'creationDate':ausfertigung,'foundingPlace':fundstelle,'Path':path}
                laws_with_extracted_information[abk] = {                    
                        'title':title,
                        'creationDate': ausfertigung,
                        'foundingPlace': fundstelle,
                        'path':path                    
                }
    createJson(laws_with_extracted_information)


def extractHeaderInformation(header):
    '''
    Extracts the title and abreviaton out of the law header
    param - {string} - header of a law file

    return - {string, string} - returns the title and the abreviation of a law in stringformat
    '''
    header = header.replace('"','')
    headerinformation = header.split('layout')[0].split('jurabk: ')
    title = headerinformation[0]
    jurabk = headerinformation[1]
    title = title.replace('Title: ','')
    title = title.replace('\n','')
    jurabk = jurabk.replace('\n','')
    return title,jurabk


def extractBodyInformation(body):
    '''
    Extracts the creationDate and foundPlace out of the law body
    param - {string} - body of a law

    return - {string,string} - returns the creationDate and the foundPlace of a law in stringformat
    '''
    try:
        dateExtraction = body.split('Ausfertigungsdatum\n:')[1]
        dateExtraction = dateExtraction.replace(' ','')
        creationDate = dateExtraction.split('\n')[0]
    except IndexError:
        creationDate = 'Keine Angabe'
    
    try:
        foundExtraction = body.split('Fundstelle\n:')[1]
        foundExtraction = foundExtraction.replace(' ','')
        foundPlace = foundExtraction.split('\n')[0]
    except IndexError:
        foundPlace = 'Keine Angabe'

    return creationDate,foundPlace


#=====Main============================================
def main():
    
    path = "/home/manuel/Dokumente/Gesetze/gesetze-master/"

    list_of_laws = []

    for root, dirs, files in os.walk(path):
        for file in files:
            filepath = os.path.join(root,file)
            if str(filepath).__contains__("index.md"):
                list_of_laws.append(filepath)
    extractLawInformation(list_of_laws)

if __name__=="__main__":
    main()
