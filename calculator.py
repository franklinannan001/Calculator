import sys

def main():
    while True:
        try:
            operation = input("Operation: ").strip()
            values = extract(operation)
            if values is not None:
                try:
                    x = int(values[0])
                    y = int(values[1])
                    if "+" in operation:
                        print(f"Sum: {addition(x, y)}")
                    elif "-" in operation:
                        print(f"Difference: {subtraction(x, y)}")
                    elif "*" in operation:
                        print(f"Product: {multiplication(x, y)}")
                    elif "/" in operation:
                        print(f"Division: {division(x, y):.2f}")
                except ValueError:
                    print(f"Please check your values: {operation}")

            else:
                print(f"{operation} is not a valid equation")
        except KeyboardInterrupt:
            sys.exit("\nThank you for visiting")


#extracting the values of x and y
def extract(o):
    signs = ["+", "-", "*", "/"]
    for character in o:
        if character in signs:
            return o.split(f"{character}")
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


if __name__ == "__main__":
    main()