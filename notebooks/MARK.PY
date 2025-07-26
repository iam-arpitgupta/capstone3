from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# 1. Get the list of English stopwords
# NLTK supports multiple languages. 'english' is one of the most common.
stop_words = set(stopwords.words('english')) # Using a set for faster lookup

print("First 10 English stopwords:", list(stop_words)[:10])
print("-" * 30)

# 2. Example Text
text = "This is a sample sentence, demonstrating the removal of common words from the text."

# 3. Tokenize the text (break it into individual words)
# Tokenization is usually the first step before removing stopwords
words = word_tokenize(text)

print("Original words:", words)
print("-" * 30)

# 4. Filter out stopwords
filtered_words = [word for word in words if word.lower() not in stop_words]

print("Words after removing stopwords:", filtered_words)

