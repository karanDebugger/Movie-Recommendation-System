# 🎬 Movie Recommendation System - API Documentation

## Demo Mode Endpoints

These endpoints are available in demo mode (`app_demo.py`) without any data files.

---

## 1. Home Page

**URL:** `GET /` or `GET /home`

**Description:** Renders the home page with movie search

**Response:** HTML page with search interface

**Example:**
```
http://localhost:5000/
```

---

## 2. Get Recommendations

**URL:** `POST /similarity`

**Description:** Get movie recommendations based on a search query

**Parameters:**
- `name` (string): Movie title to search for

**Response:** Pipe-separated (---) list of recommended movies

**Example:**
```bash
curl -X POST http://localhost:5000/similarity \
  -d "name=avatar"
```

**Response:**
```
Avatar: The Way of Water---Interstellar---Guardians of the Galaxy---Gravity---The Fifth Element
```

---

## 3. Get Movie Details

**URL:** `POST /recommend`

**Description:** Get detailed information about a specific movie

**Parameters:**
- `title` (string): Movie title

**Response:** HTML page with full movie details including:
- Title, poster, overview
- Rating, release date, runtime
- Genre and status
- Cast information
- User reviews
- Recommendations

**Example:**
```bash
curl -X POST http://localhost:5000/recommend \
  -d "title=Inception"
```

---

## 4. 🎯 Get a Random Joke

**URL:** `GET /api/joke`

**Description:** Get a random programming joke from JokeAPI

**Response:** JSON with joke data

**Response Format:**
```json
{
  "joke": "Why do programmers prefer dark mode? Because light attracts bugs!",
  "type": "single"
}
```

**Example:**
```bash
curl http://localhost:5000/api/joke
```

**JavaScript/Fetch Example:**
```javascript
fetch('/api/joke')
  .then(response => response.json())
  .then(data => console.log(data.joke))
  .catch(error => console.error('Error:', error));
```

**Python Example:**
```python
import requests

response = requests.get('http://localhost:5000/api/joke')
data = response.json()
print(data['joke'])
```

---

## 5. Health Check

**URL:** `GET /health`

**Description:** Check if the server is running and healthy

**Response:** JSON with server status

**Response Format:**
```json
{
  "status": "healthy",
  "app": "Movie Recommendation System (Demo)",
  "version": "1.0",
  "mode": "demo (no external data files needed)"
}
```

**Example:**
```bash
curl http://localhost:5000/health
```

---

## Demo Movies Available

The demo comes with 5 pre-loaded movies:

1. **Avatar** (`avatar`)
   - Rating: 7.8/10
   - Release: 2009
   - Runtime: 162 min

2. **Interstellar** (`interstellar`)
   - Rating: 8.6/10
   - Release: 2014
   - Runtime: 169 min

3. **Inception** (`inception`)
   - Rating: 8.8/10
   - Release: 2010
   - Runtime: 148 min

4. **The Matrix** (`the matrix`)
   - Rating: 8.7/10
   - Release: 1999
   - Runtime: 136 min

5. **Gravity** (`gravity`)
   - Rating: 7.7/10
   - Release: 2013
   - Runtime: 91 min

---

## Usage Examples

### 1. Search for a Movie
```bash
# Using curl
curl -X POST http://localhost:5000/similarity -d "name=interstellar"

# Output: Interstellar recommendations
```

### 2. Get Joke in Python
```python
import requests

def get_joke():
    response = requests.get('http://localhost:5000/api/joke')
    if response.status_code == 200:
        joke_data = response.json()
        print(f"😄 {joke_data['joke']}")
    else:
        print("Could not fetch joke")

get_joke()
```

### 3. Get Joke in JavaScript
```javascript
async function getJoke() {
  try {
    const response = await fetch('/api/joke');
    const data = await response.json();
    console.log('😄 ' + data.joke);
  } catch (error) {
    console.error('Error fetching joke:', error);
  }
}

getJoke();
```

### 4. Check Server Health
```bash
curl http://localhost:5000/health | python -m json.tool
```

---

## Error Handling

### Movie Not Found
```
Sorry! The movie you requested is not in our demo database. 
Try: avatar, interstellar, inception, the matrix, or gravity
```

### Joke API Unavailable
```json
{
  "joke": "😅 Joke API unavailable: Connection timeout",
  "type": "error"
}
```

---

## Rate Limits

- **Demo Mode:** No rate limits (local testing)
- **Joke API:** 100 requests per hour

---

## CORS Support

CORS is **not enabled by default** in demo mode. To enable CORS for frontend integration:

```bash
pip install flask-cors
```

Then add to `app_demo.py`:
```python
from flask_cors import CORS
CORS(app)
```

---

## Response Time

- Homepage: ~50ms
- Movie Search: ~20ms
- Joke API: ~500-1000ms (depends on external API)
- Health Check: ~5ms

---

## Supported Movie Titles (Case-Insensitive)

✅ Works:
- `avatar`
- `Avatar`
- `AVATAR`
- `interstellar`
- `inception`
- `the matrix`
- `gravity`

❌ Doesn't work:
- `avtar` (typo)
- `matrix` (without "the")

---

## Integration Guide

### Frontend Integration

```html
<button onclick="getMovieRecommendation('avatar')">Get Recommendations</button>
<button onclick="fetchJoke()">Get a Joke</button>

<script>
async function getMovieRecommendation(movieName) {
  const response = await fetch('/similarity', {
    method: 'POST',
    headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
    body: 'name=' + movieName
  });
  const recommendations = await response.text();
  console.log(recommendations.split('---'));
}

async function fetchJoke() {
  const response = await fetch('/api/joke');
  const data = await response.json();
  alert('😄 ' + data.joke);
}
</script>
```

---

## Troubleshooting

| Error | Solution |
|-------|----------|
| `ConnectionRefusedError` | Make sure app is running: `python app_demo.py` |
| `Module not found` | Install requirements: `pip install -r requirements.txt` |
| `Port 5000 in use` | Use different port in `app_demo.py`: change `port=5000` to `port=8000` |
| `Joke API timeout` | Check internet connection or try again later |

---

## License

This demo is provided as-is for educational purposes.

---

Happy exploring! 🍿🎬
