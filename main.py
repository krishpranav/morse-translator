# morse code dictionary

MORSECODEDICT = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
                    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
                    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
                    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
                    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'}

MORSE_TO_ENGLISH = {}
for key, value in MORSECODEDICT.items():
    MORSE_TO_ENGLISH[value] = key
    
def english_to_morse(message):
    morse = []
    for char in message:
        if char in MORSECODEDICT:
            morse.append(MORSECODEDICT[char])
        
    return " ".join(morse)
    
def morse_to_english(message):
    message = message.split(" ")
    english = []
    for code in message:
        if code in MORSE_TO_ENGLISH:
            english.append(MORSE_TO_ENGLISH[code])
    return " ".join(english)

def banner():
    print("""
            (1) Convert Morse To English 
            (2) English To Morse
          """)

def main():
    while True:
        banner()
        response = input("> ")
        if response == "1" or response == "2":
            break
    
    if response == "1":
        print("Enter Morse Code: ")
        morse = input("> ")
        english = morse_to_english(morse)
        print("MORSE TO ENGLISH")
        print(english)
    
    elif response == "2":
        print("Enter English Text: ")
        english = input("> ").upper()
        morse = english_to_morse(english)
        print("ENGLISH TO MORSE")
        print(morse)

if __name__ == "__main__":
    main()