import requests

username = input("Git login: ", )         # alenaPy
token = input("Git token: ", )
repo = input("Git repo: ", )              # devops_lab
pull_num = input("Git pull number: ", )   # 23

repo_url = requests.get("https://api.github.com/repos/" + username + "/" + repo + "/pulls/" + pull_num)

gh_session = requests.Session()
gh_session.auth = (username, token)

repo_url.raise_for_status()
data = repo_url.json()

with open("pull_status.txt", "w") as f:
    print("State:", data["state"],
          "\nCreate by user:", data["user"]["login"],
          "\nUser ID:", data["user"]["id"],
          "\nUser URL:", data["user"]["html_url"],
          "\nRepo ID:", data["base"]["repo"]["id"],
          "\nRepo URL:", data["base"]["repo"]["full_name"],
          "\nTitle name:", data["title"],
          "\nCreated at:", data["created_at"],
          "\nUpdated at:", data["updated_at"],
          "\nComments:", data["comments"],
          "\nCommits:", data["commits"],
          "\nAdditions:", data["additions"],
          "\nChanged files:", data["changed_files"],
          "\nDeletions files:", data["deletions"],
          "\nClosed:", data["closed_at"],
          file=f)
    f.close()
