# 🎬 Quick Start - Demo Mode (No Data Files Required)

## Run Demo in 30 Seconds

### **Windows:**
```bash
python -m pip install -r requirements.txt
python app_demo.py
```

### **macOS/Linux:**
```bash
pip install -r requirements.txt
python app_demo.py
```

### **Docker:**
```bash
docker run -p 5000:5000 -v $(pwd):/app movie-recommendation-system:latest python app_demo.py
```

---

## 🎯 Access

Open your browser: **http://localhost:5000**

---

## 📚 Demo Features

✅ **5 Sample Movies:**
- Avatar
- Interstellar
- Inception
- The Matrix
- Gravity

✅ **Full Functionality:**
- Search by movie title
- Get recommendations
- View cast information
- Read dummy reviews
- **Bonus: Joke Generator API** (/api/joke)

✅ **No Setup Needed:**
- No CSV files required
- No model files required
- No external authentication needed
- Works offline (except joke API)

---

## 🔗 API Endpoints

### Get a Random Joke
```bash
curl http://localhost:5000/api/joke
```

### Health Check
```bash
curl http://localhost:5000/health
```

---

## 📝 Demo Data Included

The app comes with hardcoded demo data for:
- Movie details (title, poster, overview, rating)
- Cast information
- Recommendations
- Dummy reviews with sentiment

---

## Next Steps

When you have real data:

1. **Add main_data.csv** to `Artifacts/` folder
2. **Run the full app**: `python app.py`
3. **Use real recommendations** based on your dataset

---

## 🚀 Try It Out

1. Open http://localhost:5000
2. Search for "Avatar"
3. Click on a recommendation
4. View full movie details with cast
5. Enjoy some jokes while browsing! 😄

Happy exploring! 🍿
