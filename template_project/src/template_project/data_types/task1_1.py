def reverse_words(str: str) -> str:
    # Split the input string into words
    words = str.split()
    # Reverse each word
    reversed_words = [word[::-1] for word in words]
    # Join the reversed words back into a single string
    reversed_str = " ".join(reversed_words)
    return reversed_str


if __name__ == "__main__":
    input_str = input("Enter a string: ")
    reversed_str = reverse_words(input_str)
    print(reversed_str)
