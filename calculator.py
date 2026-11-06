import sys

def main():
    while True:
        try:
            operation = input("Operation: ").strip()
            values = extract(operation)
            if values is not None:
                signs = ["+", "-", "*", "/", "//", "**"]
                ref = ""
                for character in operation:
                    if character in signs:
                        ref += character
                try:
                    x = int(values[0])
                    y = int(values[1])
                    if ref == "+":
                        print(f"Sum: {addition(x, y)}")
                    elif ref == "-":
                        print(f"Difference: {subtraction(x, y)}")
                    elif ref == "*":
                        print(f"Product: {multiplication(x, y)}")
                    elif ref == "**":
                        print(f"Power: {power(x, y)}")
                    elif ref == "/":
                        print(f"Division: {division(x, y):.2f}")
                    elif ref == "//":
                        print(f"Modulus: {modulus(x, y)}")
                except ValueError:
                    print(f"Please check your values: {operation}")

            else:
                print(f"{operation} is not a valid equation")
        except KeyboardInterrupt:
            sys.exit("\nThank you for visiting")


#extracting the values of x and y
def extract(o):
    signs = ["+", "-", "*", "/", "//", "**"]
    ref = ""
    for character in o:
        if character in signs:
            ref += character

    if len(ref) >= 1:
        return o.split(f"{ref}")
    else:
        return None


def addition(x, y):
    return x + y


def subtraction(x, y):
    return x - y


def multiplication(x, y):
    return x * y


def division(x, y):
    return x / y


def modulus(x, y):
    return x // y


def power(x, y):
    return x ** y


if __name__ == "__main__":
    main()