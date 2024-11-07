from flask import Flask, render_template, request
import pandas as pd
from recommendation_system import recommend_items_by_name  


movie_df = pd.read_csv('data/movies.csv')

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    recommendations = None
    if request.method == 'POST':
        try:
            
            movie_name = request.form['movie_name'].strip()
            num_recommendations = 5

            
            recommendations = recommend_items_by_name(movie_name, movie_df, num_recommendations)
        except Exception as e:
            recommendations = [f"Error: {e}"]

    
    movie_titles = movie_df['title'].tolist()

    return render_template('index.html', recommendations=recommendations, movies=movie_titles)

if __name__ == "__main__":
    app.run(debug=True)
