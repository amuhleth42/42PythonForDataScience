import sys

def readInput() -> str:
    while True:
        try:
            line = input()
        except EOFError:
            break
    print(line)
    return line

def main():
    """
    The main function
    """
    try:
        assert len(sys.argv) <= 2, "more than one argument is provided"
    except AssertionError as err:
        print(AssertionError.__name__ + ':', err)

    if len(sys.argv) < 2:
        print("What is the text to count?")
        s = readInput()
        s += "\n"
    else:
        s = sys.argv[1]
    print(f"The text contains {len(s)} characters:")

    upper = sum(1 for c in s if c.isupper())
    lower = sum(1 for c in s if c.islower())
    punctuation = ".?!,;:-()[]{}'\""
    marks = sum(1 for c in s if c in punctuation)
    spaces = sum(1 for c in s if c.isspace())
    digits = sum(1 for c in s if c.isdigit())

    print(f"{upper} upper letters")
    print(f"{lower} lower letters")
    print(f"{marks} punctuation marks")
    print(f"{spaces} spaces")
    print(f"{digits} digits")


if __name__ == "__main__":
    main()
