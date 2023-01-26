from urllib.parse import urlparse
from urllib.parse import parse_qs
import requests
from pprint import pprint
from github import Github
import time
import datetime
from datetime import date, timedelta
import csv
token = '<your github token>'
pageNo = 1
pageNoEmpty = False
g = Github("<your github token>")

# Just point base_url to your proxy server
client = Github(base_url="http://localhost:3000", login_or_token="gh_token")

# a simple call to test if it is working
#repo = client.get_repo("hsborges/github-proxy-server")
start = date(2008,1,1)
end=date(2022,6,16)
delta = timedelta(days=365)
#loopstart = start
#loopend = start + delta
loopstart = 100
loopend = loopstart/10
written = 0
apilimit = 1
total = 1
pageNo = -1
file = open("newJestFileTS10to4.csv", "a", newline='')
writer = csv.writer(file)
file_header = ['Name', 'Language', 'Stars', 'Has Snap']
writer.writerow(file_header)
#f = open("TS4.txt", "a")
#ftest = open("TSsnap4.txt", "a")
#while loopstart <= end:
while loopstart >= 0:
    time.sleep(7)
    print(loopstart)
    #loopstart += delta
    #loopend += delta
    loopstart = int(loopstart/10)
    loopend = int(loopend/10)
    print("We are at " + str(loopstart) + "-" + str(loopend))
    queryWords = 'topic:jest sort:stars-desc stars:{}..{}'.format(loopend,loopstart)
    #queryWords = 'language:javascript topic:jest sort:stars-desc created:{}..{}'.format(loopstart,loopend)
    print(queryWords)
    repositories = g.search_repositories(query=queryWords)
    repositories.get_page(0)
    print(str(repositories.totalCount))
    pageNo += 1
    for repos in repositories:
        print(str(written) + " pageNo:" + str(pageNo) + " total:" + str(total) + "startdate:" + str(loopstart) + "apilimit: " + str(apilimit))
        if written <= 200:
            print(repos.html_url)
            #f.write(repos.html_url + "\n")
            findSnap = "repo:{} extension:snap".format(repos.full_name)
            time.sleep(7)
            searchingSnap = g.search_code(query=findSnap)
            hasSnap = False
            for files in searchingSnap:
                if files == None:
                    hasSnap = False
                    # print("test1")
                else:
                    hasSnap = True
                    #ftest.write(repos.html_url + "\n")
                    break
            if hasSnap == True:
                rowInfo = [repos.full_name, "TS", repos.stargazers_count,"true"]
                writer.writerow(rowInfo)
            elif hasSnap == False:
                rowInfo = [repos.full_name, "TS", repos.stargazers_count,"false"]
                writer.writerow(rowInfo)
            written+=1
            total += 1
            apilimit += 1
            if apilimit > 3600:
                print("we're going on break")
                apilimit = 0
                time.sleep(3900)
        else:
            time.sleep(60)
            written = 0
        #print("done2")
        #break
    if loopend == 1:
        break

file.close()

