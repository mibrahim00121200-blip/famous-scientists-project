# Famous Scientists Dataset

This project scrapes Wikipedia pages for famous scientists and creates a dataset containing their biographical information.

## Files

- `scraper.py`: Scrapes Wikipedia pages for the listed scientists and saves text data to individual .txt files in the `scientists_data` folder.
- `merge.py`: Combines the scraped text files into a single CSV dataset (`scientists_dataset.csv`).
- `requirements.txt`: Lists the required Python packages.
- `scientists_data/`: Folder containing individual text files for each scientist.
- `scientists_dataset.csv`: The final dataset with columns: Scientist, Text, Length.

## Scientists Included

- Albert Einstein
- Isaac Newton
- Marie Curie
- Nikola Tesla
- Galileo Galilei
- Charles Darwin
- Stephen Hawking
- Ada Lovelace
- Louis Pasteur
- Michael Faraday
- James Clerk Maxwell
- Gregor Mendel
- Niels Bohr
- Richard Feynman
- Carl Sagan

## Usage

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Run the scraper:
   ```
   python scraper.py
   ```

3. Run the merger:
   ```
   python merge.py
   ```

## Notes

- The scraper includes a user-agent header to comply with Wikipedia's policies.
- Text is cleaned to remove reference numbers like [1].
- The dataset contains up to 30 paragraphs of introductory text from each scientist's Wikipedia page.