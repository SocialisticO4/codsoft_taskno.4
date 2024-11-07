import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
movie_df = pd.read_csv('data/movies.csv')

def recommend_items_by_name(movie_name, movie_df, num_recommendations=5):
   
    movie_name = movie_name.strip().lower()

    movie_row = movie_df[movie_df['title'].str.lower() == movie_name]

    if movie_row.empty:
        return [f"Movie '{movie_name}' not found in the dataset. Please try a different name."]

   
    movie_index = movie_row.index[0]
    movie_genre = movie_row['genre'].values[0]

    movie_df['similarity_score'] = movie_df['genre'].apply(lambda x: len(set(movie_genre.split('|')) & set(x.split('|'))))
    recommendations = movie_df.sort_values('similarity_score', ascending=False).head(num_recommendations)

    return recommendations['title'].tolist()
