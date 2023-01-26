## SPDX-License-Identifier: MIT
## Copyright 2023, 2022 Emily Bui

from urllib.parse import urlparse
from urllib.parse import parse_qs
#import requests
from pprint import pprint
from github import Github
import time
import datetime
from datetime import date, timedelta
import csv
token = '<your token here>'
pageNo = 1
pageNoEmpty = False
g = Github('<your token here>')

# Just point base_url to your proxy server
client = Github(base_url="http://localhost:3000", login_or_token='<your token here>')

# a simple call to test if it is working
#repo = client.get_repo("hsborges/github-proxy-server")

#specifying date ranges of the gathered repos
start = date(2008,1,1)
end=date(2022,6,16)
delta = timedelta(days=365)

#specify number of stars increments. Queries are broken up into these incremented bounds as to not overload the server

loopstart = 100
loopend = loopstart/10
written = 0
apilimit = 1
total = 1
pageNo = -1

#open a basic csv to input the repo info in. This CSV only contains basic info, as the attributes we were looking for were
#not yet fleshed out. This script is moreso used to get the general info into a CSV, which can be later used to extract all
#necessary attributes
file = open("yourOutputFile.csv", "a", newline='')
writer = csv.writer(file)
file_header = ['Name', 'Language', 'Stars', 'Has Snap']
writer.writerow(file_header)

#while the lower bound of the star increment boundary is above or equal to 0
while loopstart >= 0:
    #slowing down the program as to not go over the API limit
    time.sleep(7)
    print(loopstart)
    #deincrement the upper and lower bounds
    loopstart = int(loopstart/10)
    loopend = int(loopend/10)
    print("We are at " + str(loopstart) + "-" + str(loopend))

    #The queries were split up by these star increments and by language, as not doing so would make the query too large
    #and time consuming at the time to manage.
    queryWords = 'language:javascript topic:jest sort:stars-desc stars:{}..{}'.format(loopend,loopstart)
    #queryWords = 'language:TypeScript topic:jest sort:stars-desc created:{}..{}'.format(loopstart,loopend)
    print(queryWords)

    #Query the repositories and increment by pages
    repositories = g.search_repositories(query=queryWords)
    repositories.get_page(0)
    print(str(repositories.totalCount))
    pageNo += 1
    for repos in repositories:
        #print repo information and current API limit
        print(str(written) + " pageNo:" + str(pageNo) + " total:" + str(total) + "startdate:" + str(loopstart) + "apilimit: " + str(apilimit))
        if written <= 200:
            print(repos.html_url)

            #for each repo, locate if the repository has snap files. This into will later be used to fetch the exact
            #number of snap files
            findSnap = "repo:{} extension:snap".format(repos.full_name)
            time.sleep(7)
            searchingSnap = g.search_code(query=findSnap)
            hasSnap = False
            for files in searchingSnap:
                if files == None:
                    hasSnap = False

                else:
                    hasSnap = True
                    break

            #record necessary information into spreadsheet
            if hasSnap == True:
                rowInfo = [repos.full_name, "JS", repos.stargazers_count,"true"]
                writer.writerow(rowInfo)
            elif hasSnap == False:
                rowInfo = [repos.full_name, "JS", repos.stargazers_count,"false"]
                writer.writerow(rowInfo)

            #increment counts
            written+=1
            total += 1
            apilimit += 1

            #In order to bypass the API limit, the program needs to take a break when the limit has been reached and wait
            #until it has the permission to continue
            if apilimit > 3600:
                print("Break")
                apilimit = 0
                time.sleep(3900)

        #To not go over the API limit, the program will sleep for a minute every 200 repositories recorded, and then resets
        else:
            time.sleep(60)
            written = 0

    if loopend == 1:
        break

file.close()
