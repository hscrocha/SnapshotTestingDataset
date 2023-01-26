## SPDX-License-Identifier: MIT
## Copyright 2023, 2022 Emily Bui
from urllib.parse import urlparse
from urllib.parse import parse_qs
import requests
from pprint import pprint
from github import Github
import time
import datetime
from datetime import date, timedelta
import csv
username = "username"
token = '<your token here>'
pageNo = 1
pageNoEmpty = False
g = Github("<your token here>")
# Just point base_url to your proxy server
client = Github(base_url="http://localhost:3000", login_or_token="<your token here>")

#Open Files to read from and append to
jestFile = open("yourOutputFile.csv", "r")
csvreader = csv.reader(jestFile)
infoFile = open("countingFile.csv", "a", newline='')
#next(csvreader, None)
writer = csv.writer(infoFile)
file_header = ["Name",'# test']
writer.writerow(file_header)
count = 0


# the logic of this for loop is similar to the one in fullInfo. It will loop through the GitHub URLs in the spreadsheet,
# but instead of retrieving attributes, it counts the test files in the repository
for row in csvreader:
    if count == 500:
        time.sleep(10)
        count = 0
    text = row[0]
    print(text)
    #repos = g.get_repo(text)
    try:
        time.sleep(3)
        #searches for any file named test in the repository to attempt to find all test files
        #to specifically find snapshot files, replace filename:test with extension:snap
        search = "filename:test repo:{}".format(text)
        #print(search)
        repositories = g.search_code(query=search)

    #Repository can no longer be accessed
    except:
        print("Deleted!")
        continue
    else:
        snapCount = 0
        #repos = g.get_repo(text)
    #The program loops through the file and counts up the
        try:
            for repo in repositories:
                if repo == None:
                    hasSnap = False
                    # print("test1")
                else:
                    hasSnap = True
                    snapCount += 1
            rowInfo = [text,snapCount]
            writer.writerow(rowInfo)
        except:
            print("Error!")
    count+=1
infoFile.close()

