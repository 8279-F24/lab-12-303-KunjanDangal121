from morse_code import morse_code

def clean_sentence(sentence):
    """Converts sentence to lowercase and removes invalid characters."""
    return ''.join(char for char in sentence.lower() if char in morse_code or char.isspace())

def convert_to_morse(sentence):
    """Converts a cleaned sentence into Morse code."""
    morse_sentence = []
    words = sentence.split()
    for word in words:
        morse_word = [morse_code[char] for char in word]
        morse_sentence.append(' '.join(morse_word))
    return '   '.join(morse_sentence)

def main():
    """Main function to prompt user and process input."""
    sentence = input("Enter a sentence: ")
    cleaned = clean_sentence(sentence)
    morse_sentence = convert_to_morse(cleaned)
    print("Morse Code:", morse_sentence)

if __name__ == "__main__":
    main()
