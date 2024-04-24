from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter
import nltk

nltk.download("stopwords")
nltk.download('punkt')

# Read text file
with open('./app/paragraphs.txt', 'r') as text_file:
  text = text_file.read()

# Split the text into words
word_tokens = word_tokenize(text)

# Lowering each word
lowered_words = [word.lower() for word in word_tokens]

# Setting it to English stopwords
stop_words = set(stopwords.words("english"))

# Filter out stopwords to get a count
stopword_counts = Counter(word for word in lowered_words if word in stop_words)

# Print the frequency of each stop word
for stopword, count in stopword_counts.items():
  print(f"'{stopword}' appears {count} times as a stop word.")
