# 📚 Plagiarism Detection using Python

This is a simple Python project that detects the level of similarity between text files to identify possible **plagiarism**. It uses Natural Language Processing (NLP) techniques and cosine similarity.

---

## 🧠 How It Works

- The program reads multiple `.txt` files from a folder.
- It preprocesses the text (lowercasing, removing punctuation, etc.).
- It calculates **cosine similarity** between file pairs using TF-IDF vectorization.
- Outputs a similarity score matrix showing which files are most alike.

---

## 🚀 Features

- Detects similarity between multiple documents
- Uses `TfidfVectorizer` from `sklearn`
- Simple command-line interface
- Lightweight and fast

---

## 🛠️ Technologies Used

- Python 3.x
- Scikit-learn (`sklearn`)
- NumPy
- OS module

---

## 📦 Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/plagiarism-detector.git
   cd plagiarism-detector
