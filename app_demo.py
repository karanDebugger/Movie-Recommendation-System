import json
import os
from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Demo movie data (no external files needed)
DEMO_MOVIES = {
    'avatar': {
        'title': 'Avatar',
        'poster': 'https://image.tmdb.org/t/p/w500/jRXYfXnC0z2COJQdsFRP7Sdyq1U.jpg',
        'genre': 'Science Fiction, Adventure',
        'overview': 'A paraplegic Marine dispatched to the moon Pandora on a unique mission becomes torn between following his orders and protecting the world he feels is his home.',
        'rating': '7.8',
        'release_date': '2009-12-18',
        'runtime': '162 min',
        'recommendations': ['Avatar: The Way of Water', 'Interstellar', 'Guardians of the Galaxy', 'Gravity', 'The Fifth Element']
    },
    'interstellar': {
        'title': 'Interstellar',
        'poster': 'https://image.tmdb.org/t/p/w500/gEU2QniE6E77NI6lCu244myL724.jpg',
        'genre': 'Science Fiction, Drama, Adventure',
        'overview': 'A team of explorers travel through a wormhole in space in an attempt to ensure humanity\'s survival.',
        'rating': '8.6',
        'release_date': '2014-11-07',
        'runtime': '169 min',
        'recommendations': ['Avatar', 'Inception', 'Tenet', 'The Martian', 'Gravity']
    },
    'inception': {
        'title': 'Inception',
        'poster': 'https://image.tmdb.org/t/p/w500/9gk7adHYeDMwZC0Bv6ppFiK83fV.jpg',
        'genre': 'Science Fiction, Action, Thriller',
        'overview': 'A skilled thief who steals corporate secrets through dream-sharing technology is given the inverse task of planting an idea into the mind of a C.E.O.',
        'rating': '8.8',
        'release_date': '2010-07-16',
        'runtime': '148 min',
        'recommendations': ['The Matrix', 'Interstellar', 'Tenet', 'The Prestige', 'Memento']
    },
    'the matrix': {
        'title': 'The Matrix',
        'poster': 'https://image.tmdb.org/t/p/w500/vgqKVmKKmL3C+C0394p+XW-xanP.jpg',
        'genre': 'Science Fiction, Action',
        'overview': 'A computer hacker learns from mysterious rebels about the true nature of his reality and his role in the war against its controllers.',
        'rating': '8.7',
        'release_date': '1999-03-31',
        'runtime': '136 min',
        'recommendations': ['Inception', 'The Matrix Reloaded', 'Dark City', 'Blade Runner', 'Tron']
    },
    'gravity': {
        'title': 'Gravity',
        'poster': 'https://image.tmdb.org/t/p/w500/q0R4crx2SehMEF5oPnE9hdO4p5Z.jpg',
        'genre': 'Science Fiction, Thriller, Drama',
        'overview': 'Two astronauts work together to survive after an accident leaves them stranded in space.',
        'rating': '7.7',
        'release_date': '2013-10-04',
        'runtime': '91 min',
        'recommendations': ['Interstellar', 'Avatar', 'The Martian', 'Space Odyssey', 'Sunshine']
    }
}

# Dummy cast data
DEMO_CASTS = {
    'avatar': {
        'Sam Worthington': ['Sam Worthington', 'Jake Sully', 'https://image.tmdb.org/t/p/w500/euX5D13KE3Z60o6nhrIMV5sDXl9.jpg'],
        'Zoe Saldana': ['Zoe Saldana', 'Neytiri', 'https://image.tmdb.org/t/p/w500/xvx2sKlI5LxDjbmV8tzJJfOQMs8.jpg']
    },
    'interstellar': {
        'Matthew McConaughey': ['Matthew McConaughey', 'Cooper', 'https://image.tmdb.org/t/p/w500/nXMbVagXi6e86GZn6HXwPDp56nY.jpg'],
        'Anne Hathaway': ['Anne Hathaway', 'Brand', 'https://image.tmdb.org/t/p/w500/lMrKlGo9sW8q5hMvkM3zqT4ryWd.jpg']
    }
}

@app.route("/")
@app.route("/home")
def home():
    suggestions = list(DEMO_MOVIES.keys())
    return render_template('home.html', suggestions=suggestions)

@app.route("/similarity", methods=["POST"])
def similarity():
    movie = request.form.get('name', '').lower()
    
    if movie not in DEMO_MOVIES:
        return 'Sorry! The movie you requested is not in our demo database. Try: avatar, interstellar, inception, the matrix, or gravity'
    
    recommendations = DEMO_MOVIES[movie]['recommendations']
    return '---'.join(recommendations)

@app.route("/recommend", methods=["POST"])
def recommend():
    title = request.form.get('title', 'Movie')
    
    # Get movie data from demo
    movie_lower = title.lower()
    if movie_lower not in DEMO_MOVIES:
        return f"<h1>Movie '{title}' not found in demo</h1><p>Try: Avatar, Interstellar, Inception, The Matrix, or Gravity</p>"
    
    movie_data = DEMO_MOVIES[movie_lower]
    
    # Prepare recommendations
    rec_movies = movie_data['recommendations']
    movie_cards = {f"https://image.tmdb.org/t/p/w500/demo{i}.jpg": rec for i, rec in enumerate(rec_movies)}
    
    # Get cast info
    cast_info = DEMO_CASTS.get(movie_lower, {})
    casts = {name: [name, char, img] for name, (_, char, img) in cast_info.items()}
    cast_details = {name: [name, img, '1990-01-01', 'Unknown', 'Demo actor'] for name, (_, _, img) in cast_info.items()}
    
    # Dummy reviews
    dummy_reviews = {
        'This movie is absolutely amazing!': 'Good',
        'Incredible visuals and storytelling': 'Good',
        'Not as good as I expected': 'Bad',
        'Outstanding cinematography': 'Good'
    }
    
    return render_template(
        'recommend.html',
        title=movie_data['title'],
        poster=movie_data['poster'],
        overview=movie_data['overview'],
        vote_average=movie_data['rating'],
        vote_count='50000+',
        release_date=movie_data['release_date'],
        runtime=movie_data['runtime'],
        status='Released',
        genres=movie_data['genre'],
        movie_cards=movie_cards,
        reviews=dummy_reviews,
        casts=casts,
        cast_details=cast_details
    )

@app.route("/api/joke", methods=["GET"])
def get_joke():
    """Get a random joke from JokeAPI (no auth needed)"""
    try:
        response = requests.get('https://v2.jokeapi.dev/joke/Programming?format=json', timeout=5)
        if response.status_code == 200:
            data = response.json()
            if data['type'] == 'single':
                return jsonify({'joke': data['joke'], 'type': 'single'})
            else:
                joke_text = f"{data['setup']} {data['delivery']}"
                return jsonify({'joke': joke_text, 'type': 'two-part'})
        else:
            return jsonify({'joke': '😅 Could not fetch joke right now', 'type': 'error'})
    except Exception as e:
        return jsonify({'joke': f'😅 Joke API unavailable: {str(e)}', 'type': 'error'})

@app.route("/health", methods=["GET"])
def health():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'app': 'Movie Recommendation System (Demo)',
        'version': '1.0',
        'mode': 'demo (no external data files needed)'
    })

if __name__ == '__main__':
    print("\n" + "="*60)
    print("🎬 Movie Recommendation System - DEMO MODE")
    print("="*60)
    print("✓ Demo data loaded (no CSV files needed)")
    print("✓ 5 sample movies available: Avatar, Interstellar, Inception, The Matrix, Gravity")
    print("✓ Joke API integrated")
    print("="*60)
    print("\n📍 Access the app at: http://localhost:5000")
    print("🛑 Press Ctrl+C to stop\n")
    
    app.run(debug=True, host="0.0.0.0", port=5000)
