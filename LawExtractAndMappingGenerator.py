import glob
import os
import re
import csv
#import markdown
def law_list_worker(list_to_work_with):
    

    with open('laws.csv', 'w+') as f:
        write = csv.writer(f)
        CSV_Header = ['Titel', 'Abkürzung', 'Ausfertigungsdatum', 'Fundstelle', 'Pfad']
        write.writerow(CSV_Header)
        
        for lawfile in list_to_work_with:
            with open(lawfile,'r') as s:                
                text = s.read()
                markdown = str(text)
                extraction = markdown.split("---")
                header = extraction[1]
                title,abk = extract_values_from_header(header)
                rest = extraction[2]
                ausfertigung,fundstelle = extract_from_rest(rest)
                path = str(lawfile).split('Gesetze/')[1]
                values = concat_values_to_list(path,title,abk,ausfertigung,fundstelle)
                write.writerow(values)

def concat_values_to_list(path,title,abk,ausfertigung,fundstelle):
    values = []
    values.append(title)
    values.append(abk)
    values.append(ausfertigung)
    values.append(fundstelle)
    values.append(path)
    return values

def extract_values_from_header(header):
    title_and_abk = header.split('layout')[0].split('jurabk: ')
    title = title_and_abk[0]
    jurabk = title_and_abk[1]
    title = title.replace('Title: ','')
    title = title.replace('\n','')
    jurabk = jurabk.replace('\n','')
    return title,jurabk

def extract_from_rest(rest):
    try:

        ausfertigungssplit = rest.split('Ausfertigungsdatum\n:')[1]
        ausfertigungssplit = ausfertigungssplit.replace(' ','')
        ausfertigung = ausfertigungssplit.split('\n')[0]
    except IndexError:
        ausfertigung = 'Keine Angabe'
    
    try:
        fundsplit = rest.split('Fundstelle\n:')[1]
        fundsplit = fundsplit.replace(' ','')
        fund = fundsplit.split('\n')[0]
    except IndexError:
        fund = 'Keine Angabe'

    return ausfertigung,fund
def main():
    path = "/home/manuel/Dokumente/Gesetze/gesetze-master/"
    #files = glob.glob(path+'/**/*.md',recursive=True)

    #controlcount = len(files)
    #print(controlcount)

    #for filepath in files:
    #    extract_values_from_file(filepath)

    list_of_files = []
    for root, dirs, files in os.walk(path):
	    for file in files:
		    list_of_files.append(os.path.join(root,file))

    list_of_laws = []
    list_of_other_files = []

    for filepath in list_of_files:
        if str(filepath).__contains__('index.md'):
            list_of_laws.append(filepath)
        else:
            list_of_other_files.append(filepath)

    other_files = len(list_of_other_files)
    laws = len(list_of_laws)

    pdffiles = []
    jpgfiles = []
    mdfiles = []
    more_other_files = []

    for filepath in list_of_other_files:
        if str(filepath).__contains__('.pdf'):
            pdffiles.append(filepath)
        elif str(filepath).__contains__('.jpg'):
            jpgfiles.append(filepath)
        elif str(filepath).__contains__('.md'):
            mdfiles.append(filepath)
        else:
            more_other_files.append(filepath)

    pdffilescount = len(pdffiles)
    jpgfilescount = len(jpgfiles)
    mdfilescount = len(mdfiles)
    more_other_filescount = len(more_other_files)
    

    law_list_worker(list_of_laws)


    zahl = 0

if __name__ == "__main__":
    main()