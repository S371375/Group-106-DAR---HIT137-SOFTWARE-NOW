import csv
from collections import Counter
import string

# Read the text from the .txt file
with open('Q1-task1_output.txt', 'r', encoding='utf-8') as txt_file:
    text = txt_file.read()

# Remove punctuation and convert to lowercase
translator = str.maketrans('', '', string.punctuation)
text = text.translate(translator).lower()

# Tokenize the text into words
words = text.split()

# Count word occurrences
word_counts = Counter(words)

# Get the top 30 most common words
top_30_words = word_counts.most_common(30)

# Store the top 30 words and their counts in a CSV file
csv_file_path = 'Q1-task3-1_output.csv'
with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)
    
    # Write header
    csv_writer.writerow(['Word', 'Count'])
    
    # Write data
    csv_writer.writerows(top_30_words)

# Print or use the top 30 words and their counts
for word, count in top_30_words:
    print(f"{word}: {count}")

print(f"Top 30 words and counts saved to {csv_file_path}.")
