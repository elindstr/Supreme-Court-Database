import bs4, io, os
from requests_html import HTMLSession
session = HTMLSession()

#timestamp
from datetime import datetime, timedelta
ct = datetime.now()
print(ct)

#verify directory to save text files
save_directory = "data/"
if not os.path.exists(save_directory):
    os.makedirs(save_directory)

#hard code volume search parameters
volume_start=3  #volume 1 & most of 2 are Pennsylvania, see https://en.wikipedia.org/wiki/United_States_Reports,_volume_1
vol_end=600       

#locate max volume available online
url = "https://supreme.justia.com/cases/federal/us/volume/"
req = session.get(url)
soup_page = bs4.BeautifulSoup(req.text, 'lxml')
soup_links_section = soup_page.find("div", { "class" : "volumes-wrapper" })
soup_links = soup_links_section.find_all("a")
vol_end = len(soup_links)    #optional dynamic vol_end 

#iterate through volumes
for vol in range (volume_start, vol_end+1): 

    #create a list of links to decisions in this volume
    url = 'https://supreme.justia.com/cases/federal/us/' + str(vol)
    req = session.get(url)
    soup_page = bs4.BeautifulSoup(req.text, 'lxml')
    soup_links_div = soup_page.find("div", { "class" : "wrapper jcard has-padding-30 blocks has-no-bottom-padding" })     #decisions section
    soup_links = soup_links_div.find_all("a")
    soup_links_href = []
    for i in range (len(soup_links)):
        if (soup_links[i].get('href')) not in soup_links_href:
            soup_links_href.append(soup_links[i].get('href'))

    #iterate through decision links
    for i in range (len(soup_links_href)):
        url = 'https://supreme.justia.com/' + soup_links_href[i][1:]

        if url == "https://supreme.justia.com/cases/federal/us/585/141-orig/": #Justia error
            continue

        print(url)
        req = session.get(url)
        soup_page = bs4.BeautifulSoup(req.text, 'lxml')
        
        #decision cite & name
        page_title = soup_page.title.text
        page_title = page_title.split(" :: ")
        decision_name = page_title[0]
        decision_cite = page_title[1]
        decision_year =  decision_cite[-5:-1]

        #use docket number as cite for cases since 575 U.S. ___ 
        top_div = soup_page.find(id="top")     #decisions section
        top_div_spans = top_div.find_all("span")
        decision_docket = top_div_spans[0].text
        if vol >= 575:
             decision_cite = str(decision_docket)

        #list of opinion links            
        opinions_section = soup_page.find(id="opinions-list")
        opinion_links = opinions_section.find_all("a")

        #iterate opinions in decision
        for op in range (len(opinion_links)):
            href = opinion_links[op].get("href")[1:]
            opinion = soup_page.find(id=href).text
            
            type_author = opinion_links[op].text  #eg "'Opinion\t\t\t\t\t\t\t\t\t\t\t\t(Roberts)'"
            type_author = type_author.split("\t\t\t\t\t\t\t\t\t\t\t\t")
            if len(type_author) > 1:
                opinion_type = type_author[0]
                opinion_type = opinion_type.replace("/", "-") #to prevent txt file naming error
                opinion_author = type_author[1][1:-1]
            else:
                opinion_type = ""
                opinion_author = ""

            #save content to text file
            if len(decision_name) > 20:
                decision_name_for_file = decision_name[:20]
            else: 
                decision_name_for_file = decision_name
            decision_name_for_file = decision_name_for_file.replace("/", "-")

            txt_file_name = decision_cite + decision_name_for_file + opinion_type + opinion_author
            print(txt_file_name)
            with io.open('data/%s.txt' % txt_file_name, 'w', encoding='utf-8') as f:
                f.write("::decision_cite:: " + decision_cite + "\n")
                f.write("::decision_name:: " + decision_name + "\n")
                f.write("::decision_year:: " + decision_year + "\n")
                f.write("::opinion_author:: " + opinion_author + "\n")
                f.write("::opinion_type:: " + opinion_type + "\n")
                f.write("::opinion:: " + opinion)

#timestamp
print("")
print("complete")
dct = datetime.now()
print(dct)
d = dct - ct
print("total minutes elapsed: ", (d.seconds)/60)
