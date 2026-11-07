import sys


def main():
    print("\n=~=~=~=~=~ CALCULATOR ~=~=~=~=~=")
    while True:
        try:
            operation = input(">>> ").strip()
            values = extract(operation)
            if values is not None:
                signs = ["+", "-", "*", "/", "%", "**"]
                ref = ""
                for character in operation:
                    if character in signs:
                        ref += character
                try:
                    x = int(values[0])
                    y = int(values[1])
                    if ref == "+":
                        print(f"Sum: {x + y}")
                    elif ref == "-":
                        print(f"Difference: {x - y}")
                    elif ref == "*":
                        print(f"Product: {x * y}")
                    elif ref == "**":
                        print(f"Exponential: {x ** y}")
                    elif ref == "/":
                        try:
                            print(f"Division: {x / y:.2f}")
                        except ZeroDivisionError:
                            print("Cannot divide by zero")
                    elif ref == "%":
                        try:
                            print(f"Modulus: {x % y}")
                        except ZeroDivisionError:
                            print("Cannot divide by zero")
                    else:
                        print("Invalid equation")
                except ValueError:
                    print(f"Check your values: {operation}")

            else:
                print(f"{operation} is not a valid equation")
        except KeyboardInterrupt:
            sys.exit("\n=~=~=~=~=~ Thank you for visiting ~=~=~=~=~=\n")


# extracting the values of x and y
def extract(o):
    signs = ["+", "-", "*", "/", "%", "**"]
    ref = ""
    for character in o:
        if character in signs:
            ref += character

    if len(ref) >= 1:
        return o.split(f"{ref}")
    else:
        return None


if __name__ == "__main__":
    main()
