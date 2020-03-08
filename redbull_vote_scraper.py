import requests
from bs4 import BeautifulSoup
import json

url = "https://addons-redbullbasementuniversity2019.redbull.com//public-api/submissions/?limit=&offset=&list=&finalists=0&country=in"
page = requests.get(url)
data = page.json()
# data = json.dumps(data)
votes = []
submissions = data["submissions"]
propel_votes = []
for i in range(len(submissions)):
    votes.append(submissions[i]["vote_count"])
    if submissions[i]["title"] == "Propel | Fighting Depression Together":
        propel_votes.append(submissions[i]["vote_count"])

max_vote = max(votes)
votes.sort(reverse=True)
max_votes_projects = []

for i in range(len(submissions)):
    max_vote_project = {}
    if submissions[i]["vote_count"] == votes[0]:
        max_vote_project["name"] = submissions[i]["title"]
        max_vote_project["votes"] = submissions[i]["vote_count"]
        max_votes_projects.append(max_vote_project)
    if submissions[i]["vote_count"] == votes[1]:
        max_vote_project["name"] = submissions[i]["title"]
        max_vote_project["votes"] = submissions[i]["vote_count"]
        max_votes_projects.append(max_vote_project)
    if submissions[i]["vote_count"] == votes[2]:
        max_vote_project["name"] = submissions[i]["title"]
        max_vote_project["votes"] = submissions[i]["vote_count"]
        max_votes_projects.append(max_vote_project)
    if submissions[i]["vote_count"] == votes[3]:
        max_vote_project["name"] = submissions[i]["title"]
        max_vote_project["votes"] = submissions[i]["vote_count"]
        max_votes_projects.append(max_vote_project)
    if submissions[i]["vote_count"] == votes[4]:
        max_vote_project["name"] = submissions[i]["title"]
        max_vote_project["votes"] = submissions[i]["vote_count"]
        max_votes_projects.append(max_vote_project)
    if submissions[i]["vote_count"] == votes[5]:
        max_vote_project["name"] = submissions[i]["title"]
        max_vote_project["votes"] = submissions[i]["vote_count"]
        max_votes_projects.append(max_vote_project)
    if submissions[i]["vote_count"] == votes[6]:
        max_vote_project["name"] = submissions[i]["title"]
        max_vote_project["votes"] = submissions[i]["vote_count"]
        max_votes_projects.append(max_vote_project)
    if submissions[i]["vote_count"] == votes[7]:
        max_vote_project["name"] = submissions[i]["title"]
        max_vote_project["votes"] = submissions[i]["vote_count"]
        max_votes_projects.append(max_vote_project)
    if submissions[i]["vote_count"] == votes[8]:
        max_vote_project["name"] = submissions[i]["title"]
        max_vote_project["votes"] = submissions[i]["vote_count"]
        max_votes_projects.append(max_vote_project)
    if submissions[i]["vote_count"] == votes[9]:
        max_vote_project["name"] = submissions[i]["title"]
        max_vote_project["votes"] = submissions[i]["vote_count"]
        max_votes_projects.append(max_vote_project)


print('Propel Votes: ', propel_votes)
print('Max votes holder: ' + str(max_votes_projects))
print('Votes lead: ', abs(votes[0]-votes[1]))
print('Number of votes in decreasing order: ', votes)
