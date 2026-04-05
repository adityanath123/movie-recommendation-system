# 🚀 Movie Recommendation API (Flask)

A machine learning-powered web application that recommends movies based on similarity. Built using Flask and deployed for real-time access.

---

## 🔗 Live Demo

👉 [Click here to try the app](Link 🔗 <a "https://movie-recommendation-system-nhs6.onrender.com" > Click here</a>)

---

## 📌 Features

* 🎯 Recommend similar movies instantly
* 🖼️ Fetch movie posters using API
* ⚡ Lightweight backend using Flask
* 🔍 Simple and user-friendly interface
* 🌐 Deployed and accessible online

---

## 🛠️ Tech Stack

* **Backend:** Flask
* **Language:** Python
* **Machine Learning:** Scikit-learn, Pandas
* **API:** TMDB API
* **Deployment:** Render

---

## ⚙️ Installation (Run Locally)

```bash
# Clone the repository
git clone https://github.com/adityanath123/movie-recommendation-system.git

# Navigate to project folder
cd movie-recommendation-system

# Install dependencies
pip install -r requirements.txt

# Run the Flask app
python app1.py
```

---

## 📂 Project Structure

```
├── app1.py
├── similarity.pkl
├── movies_dict.pkl
├── requirements.txt
└── README.md
```

---

## 🧠 How It Works

* Movie data is processed and converted into vectors
* Cosine similarity is used to find similar movies
* Flask serves the backend and handles user requests

---

## 📡 Routes

### 🔹 Home Page

```
/
```

### 🔹 Get Recommendations

```
/recommend?movie=movie_name
```

Example:

```
/recommend?movie=Inception
```

---

## 🚀 Future Improvements

* Add user authentication
* Improve UI design
* Add filters (genre, rating, year)
* Convert to FastAPI for scalability

---

## 🤝 Contributing

Feel free to fork and improve this project.

---

## 📬 Contact

For any queries or suggestions, feel free to reach out.

---

⭐ Star this repo if you found it useful!

