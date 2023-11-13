#documented issues: 
##1. The scraped decisions in the "data" directory include some
#special cases, e.g., review of petitions for certiorari or applications for stay
#of injunctions. The SCDB apparently doesn't track these cases. When this script 
#cannot locate a decision in the SCDB, the SCDB_caseId is coded as "0".
##2. Some decision (especially in vol 2) have the same U.S. page cite and 
#result in multiple possible fo SCDB case_ids

#timestamp
from datetime import datetime, timedelta
ct = datetime.now()
print(ct)

#load SCDB into pandas
import pandas
SCDB = pandas.read_csv('assets/combined_case.csv')  #"court-centered" database; merged legacy and modern
SCDB['caseName'] = SCDB['caseName'].str.upper()
SCDB['caseName'] = SCDB['caseName'].str.replace(",","")
SCDB['caseName'] = SCDB['caseName'].str.replace(".","")
SCDB['caseName'] = SCDB['caseName'].str.replace("-","")
SCDB['caseName'] = SCDB['caseName'].str.replace(" ","")

#get citation from decision files
import os, glob, re
from os import path
directory = "data/"
for filename in glob.glob(os.path.join(directory, '*.txt')):
    print("filename: ", filename)
    with open(filename, 'r') as original: 
        data = original.read()

        caseCite = filename[len(directory):]
        page_begin = caseCite.find("U.S. ") + 5
        for i in range (page_begin, len(caseCite)):
            if re.fullmatch(r"\d+", caseCite[i]) == None:
                page_end = i
                caseCite = caseCite[:page_end]
                break

        if caseCite.find("U.S.") != -1: #us cite form
            #eg us_cite = "2 U.S. 401"

            usCite_match = SCDB[SCDB['usCite'] == caseCite]
            if len(usCite_match) == 0:
                match_string = 0
            elif len(usCite_match) == 1:
                match_string = usCite_match["caseId"].to_string(index=False)
            
            else:   #multiple decisions cited at same page number; attempting to compare case names with reformatting to standardize databases
                title_part = ""
                with open(filename, 'r') as original: 
                    for line in original:
                        if line.find("::decision_name:: ") != -1:
                            title_part = line.replace(",","")
                            title_part = title_part.replace(".","")
                            title_part = title_part.replace("-","")
                            title_part = title_part.replace(" ","")
                            title_part = title_part[-6:-1].upper()
                            break
                usCite_and_title_match = usCite_match[usCite_match['caseName'].str.contains(title_part, na=False)]
                if len(usCite_and_title_match) == 0:
                    match_string = 0
                elif len(usCite_and_title_match) > 0:
                    match_string = usCite_and_title_match["caseId"].to_string(index=False)

            #print(caseCite, " SCDB: ", match_string)
        
        else:   #docket cite form
            docket_match = SCDB[SCDB['docket'] == caseCite]
            if len(docket_match) == 0:
                match_string = 0
            else:
                match_string = docket_match["caseId"].to_string(index=False)
            #print(caseCite, " SCDB: ", match_string)
        
        with open(filename, 'w') as modified: 
            modified.write("::SCDB_caseID:: " + str(match_string) + "\n" + data)

#timestamp
print("")
dct = datetime.now()
print(dct)
d = dct - ct
print("Completed in: ", (d.seconds), " seconds.")