import sys


def convertToMorse(s: str):
    NESTED_MORSE = {
        " ": "/",
        "A": ".-",
        "B": "-...",
        "C": "-.-.",
        "D": "-..",
        "E": ".",
        "F": "..-",
        "G": "-.",
        "H": "....",
        "I": "..",
        "J": ".---",
        "K": "-.-",
        "L": ".-..",
        "M": "--",
        "N": "-.",
        "O": "---",
        "P": ".--.",
        "Q": "--.-",
        "R": ".-.",
        "S": "...",
        "T": "-",
        "U": "..-",
        "V": "...-",
        "W": ".--",
        "X": "-..-",
        "Y": "-.--",
        "Z": "--..",
        "0": "-----",
        "1": ".----",
        "2": "..---",
        "3": "...--",
        "4": "....-",
        "5": ".....",
        "6": "-....",
        "7": "--...",
        "8": "---..",
        "9": "----."
    }
    res = []
    for c in s:
        res.append(NESTED_MORSE[c])
    print(" ".join(res))



def main():
    try:
        assert len(sys.argv) == 2, "the arguments are bad"
        for c in sys.argv[1]:
            if c.isalnum() == False and c != ' ':
                raise AssertionError("the arguments are bad")
        
        convertToMorse(sys.argv[1].upper())

    except AssertionError as err:
        print(AssertionError.__name__ + ":", err)

if __name__ == "__main__":
    main()
