# 🌟 Famous Scientists Dataset

A Python-based web scraping project that collects biographical information about famous scientists from Wikipedia and generates a structured dataset.

---

## 📌 Overview

This project automates the process of extracting, cleaning, and organizing textual data of well-known scientists. The final output is a CSV dataset that can be used for data analysis, NLP tasks, or machine learning projects.

---

## 📁 Project Structure

* **scraper.py**
  Scrapes Wikipedia pages and saves cleaned text into individual `.txt` files.

* **merge.py**
  Combines all text files into a single dataset (`scientists_dataset.csv`).

* **requirements.txt**
  Contains required Python libraries.

* **scientists_data/**
  Folder with individual scientist text files.

* **scientists_dataset.csv**
  Final dataset with columns:

  * Scientist
  * Text
  * Length

---

## 👨‍🔬 Scientists Included

Albert Einstein
Isaac Newton
Marie Curie
Nikola Tesla
Galileo Galilei
Charles Darwin
Stephen Hawking
Ada Lovelace
Louis Pasteur
Michael Faraday
James Clerk Maxwell
Gregor Mendel
Niels Bohr
Richard Feynman
Carl Sagan

---

## ⚙️ How to Run

### 1️⃣ Install dependencies

```
pip install -r requirements.txt
```

### 2️⃣ Run scraper

```
python scraper.py
```

### 3️⃣ Generate dataset

```
python merge.py
```

---

## 🧠 Features

* Automated web scraping from Wikipedia
* Text cleaning (removes references like `[1]`)
* Structured dataset generation
* Lightweight and easy to run

---

## 📝 Notes

* Uses a custom User-Agent to follow Wikipedia policies
* Extracts up to 30 paragraphs per scientist
* Designed for educational and research purposes

---

## 🚀 Future Improvements

* Add more scientists
* Convert dataset into JSON format
* Integrate NLP preprocessing (tokenization, stopword removal)
* Build a simple GUI for interaction

---

## 👤 Author

**Ibrahim**
BS Artificial Intelligence Student

---

## 📜 License

This project is licensed under the MIT License.
