from flask import Flask, render_template 
import requests

app=Flask(__name__)

@app.route('/hey')
def index():
    url='https://api.themoviedb.org/3/movie/upcoming'
    payload={'api_key': '4bf0bfde70bf5f9bce067c8c462fb440', 'language': 'en-US','page': 1}
    response= requests.get(url,params=payload)

    if response.status_code == 200:
        data = response.json()
        movies = data.get('results')
        return render_template('index.html', movies=movies)
    else:
        return 'Something went wrong!'


if __name__ == "__main__" :
    app.run(debug=True)