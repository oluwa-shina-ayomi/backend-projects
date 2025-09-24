### github activity cli

a simple command line tool to fetch and display a user’s recent github activities in plain english.

### features
- shows events like pushes, issues, pull requests, stars, forks, branches or tags created or deleted  
- outputs human readable summaries like: 

pushed 3 commits to kamranahmedse/developer-roadmap
opened a new issue in kamranahmedse/developer-roadmap
starred kamranahmedse/developer-roadmap

### notes
this was my second time working with an api
i had to properly read and parse a json file returned by the api

### usage
```bash
python github-activity.py <username>
example: python github-activity.py torvalds

requirements
install dependencies with: pip install -r requirements.txt
requirements.txt contains: requests