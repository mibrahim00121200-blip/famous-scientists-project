import os
import pandas as pd

folder = "scientists_data"
data = []

for file in os.listdir(folder):
    if file.endswith(".txt"):
        path = os.path.join(folder, file)

        with open(path, "r", encoding="utf-8") as f:
            text = f.read()

        name = file.replace(".txt", "")

        data.append({
            "Scientist": name,
            "Text": text,
            "Length": len(text)
        })

df = pd.DataFrame(data)

df.to_csv("scientists_dataset.csv", index=False)

print("Dataset created successfully ✔")
print(f"Total scientists: {len(data)}")