from pathlib import Path
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


parent_dir = Path.cwd().parent
namelist_filepath = parent_dir / "data/Navneliste.txt"

with open(namelist_filepath, 'r') as f:
    lines = f.readlines()

# sort and print names
def sort_and_print_names(names: list[str]) -> None: 
    names_sorted = sorted(names)
    names_sorted = sorted(names_sorted, key=len)
    print(names_sorted)

names = lines[0].split(',')
#sort_and_print_names(names)


# dict with letter frequencies
letters = lines[0].replace(',', '').lower()
letter_frequency: dict = dict()
for letter in list(letters):
    letter_frequency[letter] = letter_frequency.get(letter, 0) + 1



# Extension to exercise 1

# Barplot
fig, ax = plt.subplots()
df = pd.DataFrame(list(letter_frequency.items()), columns=['Letter', 'Frequency'])
df = df.sort_values(by="Letter")
vowels = 'aeiouy'
colors = ['orange' if l in vowels else 'darkgrey' for l in df.Letter]
print(colors)
sns.barplot(x=df.Letter, y=df.Frequency, palette=colors, ax=ax)
plt.show()


