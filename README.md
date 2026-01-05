📽️ Movie Recommender System (Content-Based)
📌 Project Overview

This project implements a content-based movie recommender system using the TMDB 5000 Movies dataset from Kaggle.
The system recommends movies based on similarity in content features such as genres, keywords, cast, and crew.

The goal of the project is to demonstrate data cleaning, preprocessing, feature engineering, and similarity-based recommendation, which are core skills in data science and applied machine learning.

🗂️ Dataset

Source: Kaggle – TMDB 5000 Movies Dataset

Files used:

tmdb_5000_movies.csv

tmdb_5000_credits.csv

Size: ~5000 movies

⚙️ Methodology
1. Data Cleaning & Preprocessing

Merged movie metadata and credits datasets

Parsed JSON-like columns (genres, keywords, cast, crew)

Selected relevant features for recommendation

Handled missing values and removed unnecessary fields

2. Feature Engineering

Extracted and processed:

Genres

Keywords

Top cast members

Director information

Combined features into a single textual representation

Applied text normalization (lowercasing, tokenization)

3. Recommendation Technique

Implemented a content-based filtering approach

Used CountVectorizer to convert text features into vectors

Calculated cosine similarity between movie vectors

Recommended top similar movies based on similarity scores

🧠 Recommendation Logic

Given a movie title:

Identify the movie index

Compute similarity scores with all other movies

Rank movies by similarity

Return top-N most similar movies

🛠️ Technologies Used

Python

Pandas

NumPy

scikit-learn

NLTK (basic text processing)

Jupyter Notebook

📊 Example Output

For a given movie (e.g., Inception), the system recommends movies with similar genres, themes, and cast, based purely on content similarity.

📁 Project Structure
Movie-Recommender-System/
│
├── data/
│   ├── tmdb_5000_movies.csv
│   ├── tmdb_5000_credits.csv
│
├── notebook/
│   └── movie_recommender.ipynb
│
├── README.md

🎯 Learning Outcomes

Hands-on experience with real-world data cleaning

Practical understanding of content-based recommendation systems

Feature engineering for NLP-style tasks

Similarity computation using vector space models

🚀 Future Improvements

Add collaborative filtering

Hybrid recommendation system

Deploy as a web application

Improve text preprocessing using advanced NLP techniques
