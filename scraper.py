import requests
from bs4 import BeautifulSoup
import os
import re

folder = "scientists_data"
os.makedirs(folder, exist_ok=True)

# Large list (you can expand more)
scientists = [
    "Albert Einstein",
    "Isaac Newton",
    "Marie Curie",
    "Nikola Tesla",
    "Galileo Galilei",
    "Charles Darwin",
    "Stephen Hawking",
    "Ada Lovelace",
    "Louis Pasteur",
    "Michael Faraday",
    "James Clerk Maxwell",
    "Gregor Mendel",
    "Niels Bohr",
    "Richard Feynman",
    "Carl Sagan"
]

base_url = "https://en.wikipedia.org/wiki/"

for name in scientists:
    url = base_url + name.replace(" ", "_")

    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        res = requests.get(url, headers=headers)
        res.raise_for_status()  # Raise an error for bad status codes
        soup = BeautifulSoup(res.text, "html.parser")

        content = soup.find("div", {"id": "mw-content-text"})
        paragraphs = content.find_all("p")

        text = ""

        # 🔥 Long dataset (30 paragraphs if available)
        for p in paragraphs[:30]:
            text += p.get_text()

        # clean references like [1]
        text = re.sub(r"\[\d+\]", "", text)

        filename = os.path.join(folder, name.replace(" ", "_") + ".txt")

        with open(filename, "w", encoding="utf-8") as f:
            f.write(text)

        print(name, "saved ✔")

    except Exception as e:
        print("Error:", name)