## SPDX-License-Identifier: MIT
## Copyright 2023, 2022 Emily Bui
import csv
from github import Github
import time
import datetime
from datetime import date, timedelta
g = Github("<your token here>")

jestFile = open("yourOutputFile.csv", "r")
csvreader = csv.reader(jestFile)

infoFile = open("yourOutputFileFull.csv", "a", newline='')
#add empty line
next(csvreader, None)
writer = csv.writer(infoFile)

#Headers, these can be edited depending what attributes the user wants to represent on the csv.
file_header = ["Name", 'Star Count', 'Size', 'Fork #', 'Watchers #', 'Created','Updated','Organization','Subscribers','Issues','Network']
    #["Name",'forks', 'watchers', 'networks' ]
writer.writerow(file_header)
count = 0

for row in csvreader:
    #To not exceed API limits, the program pauses after 500 repos
    if count == 500:
        time.sleep(10)
        count = 0

    #The first column retrieves the Github link to the repo where the program retrieves repo attributes
    text = row[0]
    print(text)
    try:
        repos = g.get_repo(text) #checks to see if the repo exists (this will filter out any repos on the spreadsheet that have been removed from GitHub
                                # and are thus invalid )
    except:
        print("Deleted!")
        continue
    else:
        rowInfo = [repos.full_name, repos.stargazers_count, repos.size, repos.forks_count, repos.watchers_count, repos.created_at, repos.updated_at, repos.organization, repos.subscribers_count, repos.open_issues_count, repos.network_count]
        writer.writerow(rowInfo)
        print(repos.full_name)
    count+=1
infoFile.close()
