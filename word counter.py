def count_words(text):
    """
    Counts the number of words in the given text.
    """
    # Remove punctuation and convert the text to lowercase
    cleaned_text = ''.join(e for e in text if e.isalnum() or e.isspace()).lower()

    # Split the cleaned text into words
    words = cleaned_text.split()

    # Count the number of words
    num_words = len(words)

    return num_words

def main():
    """
    The main function of the program.
    """
    # Prompt the user to enter a sentence or paragraph
    text = input("Enter a sentence or paragraph: ")

    # Check if the input is empty
    if not text:
        print("Error: The input is empty.")
        return

    # Count the number of words in the input
    num_words = count_words(text)

    # Print the word count to the console
    print(f"The input has {num_words} words.")

if __name__ == "__main__":
    main()