def tokenize(sentences):
    """Generator that tokenizes sentences into words."""
    for sentence in sentences:
        for word in sentence.split():
            yield word


def remove_stop_words(words, stop_words):
    """Generator that removes stop words from a stream of words."""
    for word in words:
        if word.lower() not in stop_words:
            yield word


def count_frequency(words):
    """Generator that counts the frequency of words."""
    frequency = {}
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    for word, count in frequency.items():
        yield (word, count)


# Sample data and stop words
sentences = [
    "This is a sample sentence.",
    "This sentence is another example sentence.",
    "Is this the third sentence?",
]
stop_words = {"is", "a", "the", "this"}

# Running the pipeline
# Step 1: Tokenization
tokens = tokenize(sentences)

# Step 2: Stop word removal
filtered_tokens = remove_stop_words(tokens, stop_words)

# Step 3: Frequency count
word_frequencies = count_frequency(filtered_tokens)

# Collecting and printing the results
result = list(word_frequencies)
print(result)
