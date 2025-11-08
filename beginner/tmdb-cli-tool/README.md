### tmdb cli tool

this is a small program you run in the terminal. it asks themoviedb.org for a list of movies and shows some details like the title, description, rating, and release date. it gets the information using a special key called an api key.

note: create a .env file in the project root with your api key
auth_key=your_api_key_here

usage
run the cli tool with the category option:

```bash

python tmdb-cli.py -c <category>

available categories:
- now_playing
- popular
- top_rated
- upcoming

example:

```bash
python tmdb-cli.py -c popular