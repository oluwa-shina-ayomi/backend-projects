import argparse
import requests
from dotenv import load_dotenv
import os

def configure():
    load_dotenv()

def main():
    configure()

    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--category", help="indicate the type of movie (playing, popular, top, upcoming)", type=str, choices= ["now_playing", "popular", "top_rated", "upcoming"])
    args = parser.parse_args()
    category = args.category


    for movie in get(category):
        print(f"""- {movie["title"]}; {movie["overview"]}. 
{movie["popularity"]} million views, {movie["rating"]} star
total votes: {movie["total_votes"]}, release date:{movie["release_date"]} \n""")
      

def get(category):
    if category in ["now_playing", "top_rated", "upcoming", "popular"]:
        
        try:
            url = f"https://api.themoviedb.org/3/movie/{category}?language=en-US&page=1"

            headers = {
                "accept": "application/json",
                "Authorization": os.getenv("auth_key")
                }

            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()

        except requests.RequestException as e:
            yield {"error": str(e)}

        else:
            for movie in present(response.json()):
                yield movie

def present(response):
        results = response["results"]
        for result in results:
            movie = {
                "title": result["title"],
                "overview": result["overview"],
                "popularity": result["popularity"],
                "rating": result["vote_average"],
                "total_votes": result["vote_count"],
                "release_date": result["release_date"]
                }
            yield movie

if __name__ == "__main__":
    main()


