import time
from adafruit_circuitplayground.express import cpx

# Morse code dictionary (directly included for simplicity)
morse_code = {
    'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.',
    'g': '--.', 'h': '....', 'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..',
    'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.',
    's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-',
    'y': '-.--', 'z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----'
}

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

def display_morse(morse_sentence, unit_length):
    """Displays Morse code using the LEDs on Circuit Playground."""
    for symbol in morse_sentence:
        if symbol == '.':
            cpx.pixels.fill((0, 255, 0))  # Green for dots
            time.sleep(unit_length)
        elif symbol == '-':
            cpx.pixels.fill((0, 0, 255))  # Blue for dashes
            time.sleep(3 * unit_length)
        elif symbol == ' ':
            cpx.pixels.fill((0, 0, 0))  # Off for intra-word spaces
            time.sleep(unit_length)
        else:  # Space between words
            cpx.pixels.fill((0, 0, 0))
            time.sleep(7 * unit_length)
        cpx.pixels.fill((0, 0, 0))  # Ensure LED turns off
        time.sleep(unit_length)  # Gap between symbols

def main():
    """Main function to prompt user and display Morse code."""
    try:
        unit_length = float(input("Enter the unit length (0 to 1 seconds): "))
        if not 0 <= unit_length <= 1:
            raise ValueError("Unit length must be between 0 and 1 seconds.")
        sentence = input("Enter a sentence: ")
        cleaned = clean_sentence(sentence)
        morse_sentence = convert_to_morse(cleaned)
        print("Displaying Morse Code...")
        display_morse(morse_sentence, unit_length)
    except ValueError as e:
        print("Error:", e)

if __name__ == "__main__":
    main()

