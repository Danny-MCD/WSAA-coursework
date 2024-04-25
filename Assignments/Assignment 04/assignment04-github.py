# Assignment 05 : Replacing text in a file with authorisation
# Author : Daniel Mc Donagh


import requests
from github import Github
from config import config as cfg

# Retrieve token key from config file
apikey = cfg["githubkey"]
g = Github(apikey)

# Access and Print the URL of the Repo
repo = g.get_repo("Danny-MCD/APrivateOne")
print(repo.clone_url)

# Access content of text file and downloading URL
FileInfo = repo.get_contents("assignment05.txt")
URLofFile = FileInfo.download_url
print(URLofFile)

# Sending GET request & extracting contents
response = requests.get(URLofFile)
ContentofFile = response.text
print(ContentofFile)

# Replace names in file
NewContent = ContentofFile.replace("Andrew", "Danny")
print(NewContent)

#Update text file and commit
result_changed = repo.update_file(FileInfo.path, "All instances of Andrew replaced with Danny", NewContent, FileInfo.sha, branch="main")
print(result_changed)

