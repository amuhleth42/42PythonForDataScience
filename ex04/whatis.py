import sys

def is_odd(number: int) -> bool:
    return (number % 2 == 1)

def main():
    try:
        assert len(sys.argv) <= 2, "more than one argument is provided"
        if len(sys.argv) < 2:
            exit()
        try:
            number = int(sys.argv[1])
        except ValueError:
            raise AssertionError("argument is not an integer")

        if is_odd(number):
            print("I'm Odd")
        else:
            print("I'm Even")
        
    except AssertionError as err:
        print(AssertionError.__name__ + ':', err)


if __name__ == "__main__":
    main()
