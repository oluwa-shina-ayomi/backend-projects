import requests
import sys

def format_event(event):
    event_type = event["type"]
    repo = event["repo"]["name"]

    if event_type == "IssuesEvent":
        action = event["payload"]["action"]
        if action == "opened":
            return f"Opened a new issue in {repo}"
        if action == "closed":
            return f"Closed an issue in {repo}"
        
    elif event_type == "PushEvent":
        size = event["payload"]["size"]
        commit_word = "commit" if size == 1 else "commits"
        return f"Pushed {size} {commit_word} to {repo}"
    
    elif event_type == "PullRequestEvent":
        action = event["payload"]["action"]
        pr_merged = event["payload"]["pull_request"]["merged_at"]
        if action == "opened":
            return f"Opened a pull request in {repo}"
        if action == "closed":
            if pr_merged:
                return f"Merged a pull request in {repo}"
            else:
                return f"Closed a pull request in {repo}"
            
    elif event_type == "WatchEvent":
        return f"Starred {repo}"

    elif event_type == "ForkEvent":
        return f"Forked {repo}"
    
    elif event_type == "CreateEvent":
        ref_type = event["payload"]["ref_type"]
        ref = event["payload"]["ref"]
        if ref_type == "repository":
            return f"Created a new repository {repo}"
        else:
            return f"Created a new {ref_type} {ref} in {repo}"
        
    elif event_type == "DeleteEvent":
        ref_type = event["payload"]["ref_type"]  
        ref = event["payload"]["ref"]            
        return f"Deleted {ref_type} {ref} in {repo}"
    
    return None

if len(sys.argv) != 2:
    sys.exit("usage: github-activity <username>")

username = sys.argv[1]
response = requests.get(f"https://api.github.com/users/{username}/events")

if response.status_code != 200:
    sys.exit(f"Error: {response.status_code} - {response.text}")

events = response.json()

for event in events:
    output = format_event(event)
    if output:
        print(f"- {output}")
