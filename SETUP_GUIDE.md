# 🎬 Setup & Run Guide - Movie Recommendation System

## Prerequisites

- **Python 3.8+** installed
- **Git** (optional, for cloning)

---

## Method 1: Local Setup (Recommended)

### Step 1: Clone & Navigate
```bash
git clone https://github.com/karanDebugger/Movie-Recommendation-System.git
cd Movie-Recommendation-System
```

### Step 2: Create Virtual Environment
```bash
# On macOS/Linux
python3 -m venv venv
source venv/bin/activate

# On Windows
python -m venv venv
venv\Scripts\activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Prepare Data & Models
You need to place the following files in the `Artifacts/` directory:

```
Artifacts/
├── main_data.csv          # Movie dataset
├── nlp_model.pkl          # Sentiment analysis model
└── transform.pkl          # Feature vectorizer
```

**If you don't have these files:**
- Download the movie dataset from [Kaggle TMDB dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)
- Place it as `Artifacts/main_data.csv`
- The app will work partially without the NLP models (sentiment analysis will show "Unknown")

### Step 5: Run the App
```bash
python app.py
```

**Output:**
```
==================================================
🎬 Movie Recommendation System
==================================================
Artifacts directory: /path/to/Artifacts
Data file: /path/to/Artifacts/main_data.csv
==================================================

✓ Loaded NLP model from .../Artifacts/nlp_model.pkl
✓ Loaded transformer from .../Artifacts/transform.pkl
✓ Similarity matrix created with XXX movies

 * Running on http://0.0.0.0:5000
```

### Step 6: Access the App
Open your browser and go to: **http://localhost:5000**

---

## Method 2: Docker Setup

### Prerequisites
- **Docker** installed ([Install Docker](https://docs.docker.com/get-docker/))

### Step 1: Clone the Repository
```bash
git clone https://github.com/karanDebugger/Movie-Recommendation-System.git
cd Movie-Recommendation-System
```

### Step 2: Build Docker Image
```bash
docker build -t movie-recommendation-system:latest .
```

### Step 3: Run Docker Container
```bash
docker run -p 5000:5000 \
  -v $(pwd)/Artifacts:/app/Artifacts \
  movie-recommendation-system:latest
```

**On Windows (PowerShell):**
```powershell
docker run -p 5000:5000 `
  -v ${PWD}/Artifacts:/app/Artifacts `
  movie-recommendation-system:latest
```

### Step 4: Access the App
Open your browser and go to: **http://localhost:5000**

---

## Method 3: Quick Docker Compose (Easiest)

Create a `docker-compose.yml` in the project root:

```yaml
version: '3.8'
services:
  app:
    build: .
    ports:
      - "5000:5000"
    volumes:
      - ./Artifacts:/app/Artifacts
    environment:
      - FLASK_ENV=development
```

Then run:
```bash
docker-compose up
```

Access at: **http://localhost:5000**

---

## Troubleshooting

### Issue: `ModuleNotFoundError: No module named 'flask'`
**Solution:** Ensure you've installed requirements:
```bash
pip install -r requirements.txt
```

### Issue: `FileNotFoundError: Artifacts/main_data.csv not found`
**Solution:** Download the dataset and place it in the `Artifacts/` directory

### Issue: Port 5000 already in use
**Solution:** Use a different port:
```bash
python app.py  # Edit app.py, change port=5000 to port=8000
# OR with Docker
docker run -p 8000:5000 movie-recommendation-system:latest
```

### Issue: `⚠ Warning: NLP model not found`
**Solution:** This is OK. The app will still work for recommendations without sentiment analysis.

---

## Features

✅ **Search movies** by title  
✅ **Get recommendations** based on content similarity  
✅ **View cast & crew** information  
✅ **Read IMDB reviews** with sentiment analysis  
✅ **Responsive web UI**  

---

## File Structure

```
Movie-Recommendation-System/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── Dockerfile             # Docker configuration
├── docker-compose.yml     # Docker Compose setup (optional)
├── SETUP_GUIDE.md         # This file
├── run.sh                 # Startup script (Unix)
├── run.bat                # Startup script (Windows)
├── templates/             # HTML templates
├── static/                # CSS/JS assets
├── Artifacts/             # Data & models (create this)
│   ├── main_data.csv
│   ├── nlp_model.pkl
│   └── transform.pkl
└── NoteBook_Experiments/  # Jupyter notebooks
```

---

## Next Steps

1. **Customize the UI** - Edit HTML templates in `templates/`
2. **Add more features** - Implement collaborative filtering
3. **Deploy online** - Use AWS, Heroku, or Render
4. **Improve models** - Train your own NLP sentiment analyzer

---

## Support

- Check console output for detailed error messages
- Ensure all data files are in the correct format (CSV for data, PKL for models)
- Use Python 3.8+ for compatibility

Happy recommending! 🍿
