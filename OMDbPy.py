import requests
import json


def OMDbPy(movie):
    url = 'http://www.omdbapi.com/?t='+movie
    try:
        response = requests.get(url)
        json_data = json.loads(response.text)
        return json_data
    except requests.exceptions.RequestException as e:
        sys.exit(1)

if __name__ == "__main__":
    movie = raw_input("Enter movie: ")
    data = OMDbPy(movie)
    print data['Title']
    print data['Year']
    print data['imdbRating']
