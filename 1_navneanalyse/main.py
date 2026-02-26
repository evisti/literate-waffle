from string import ascii_lowercase
from pathlib import Path
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from wordcloud import WordCloud


namelist_file = 'Navneliste.txt'

with Path(namelist_file).open() as f:
    lines = f.readlines()

names = lines[0].split(',')

# Sort and print names
names_sorted = sorted(names)
names_sorted = sorted(names_sorted, key=len)
print(f'Names sorted:\n {names_sorted}')

# Dict with letter frequencies
letters = lines[0].replace(',', '').lower()
letter_frequency: dict = dict()
for letter in list(letters):
    letter_frequency[letter] = letter_frequency.get(letter, 0) + 1



# Extension to assignment 1

# Letter frequency analysis

fig, ax = plt.subplots(1, 2, figsize=(12,6))

letter_df = pd.DataFrame(list(letter_frequency.items()), columns=['Letter', 'Frequency'])
letter_df = letter_df.sort_values(by="Letter")
vowels = 'aeiouy'
letter_colors = ['orange' if l in vowels else 'darkgrey' for l in letter_df.Letter]
sns.barplot(x=letter_df.Letter, y=letter_df.Frequency, hue=letter_df.Letter, palette=letter_colors, ax=ax[0])


wordcloud = WordCloud(width=480, height=480, margin=0).fit_words(letter_frequency)
ax[1].imshow(wordcloud, interpolation='bilinear')
ax[1].set_axis_off()

plt.show()


# Name length analysis

names_df = pd.DataFrame({'Name': names, 'Name length': [len(name) for name in names]})

fig, ax = plt.subplots()
sns.histplot(x=names_df['Name length'], discrete=True, edgecolor='white', color='cornflowerblue', ax=ax)
ax.set_xticks([3,4,5,6,7,8,9,10,11])
mean_and_median = f'''
Mean:     {names_df['Name length'].mean():.2f}
Median:  {names_df['Name length'].median():.2f}
Std:        {names_df['Name length'].std():.2f}
'''
ax.text(9, 240, mean_and_median, fontsize=11)

plt.show()

