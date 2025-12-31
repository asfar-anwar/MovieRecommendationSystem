import pandas as pd

def get_recommendations():
    try:
        # Load dataset
        df = pd.read_csv("movies.csv")
        
        # Clean column names and data
        df.columns = df.columns.str.strip()
        
        # Show user the options
        genres = df['genre'].unique()
        print(f"Available Genres: {', '.join(genres)}")
        
        # Get user input
        user_genre = input("\nEnter a genre to get recommendations: ").strip().lower()

        # Filter and Sort by rating (Highest to Lowest)
        recommendations = df[df['genre'].str.lower() == user_genre].sort_values(by='rating', ascending=False)

        if not recommendations.empty:
            print(f"\nTop {user_genre.capitalize()} Movies for You:")
            for index, row in recommendations.iterrows():
                print(f"⭐ {row['rating']} | {row['title']}")
        else:
            print(f"Sorry, we don't have any movies in the '{user_genre}' genre yet.")
            
    except FileNotFoundError:
        print("Error: movies.csv not found!")

if __name__ == "__main__":
    get_recommendations()