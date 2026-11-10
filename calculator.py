import sys
import re


def main():
    print("\n=~=~=~=~=~ CALCULATOR ~=~=~=~=~=")
    while True:
        try:
            operation = input(">>> ").strip()
            values = extract_values(operation)
            if values is not None:
                ref = get_ref(operation)
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
                            print(f"Quotient: {x / y:.2f}")
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


# extracting and storing the sign in the equation
def get_ref(o):
    if equation := re.search(r"^[0-9]+\s*(-|\+|\*\*?|/|%)\s*[0-9]+$", o):
        return equation.group(1)
    else:
        return None


# extracting the values of x and y
def extract_values(o):
    ref = get_ref(o)
    if ref is not None:
        return o.split(f"{ref}")
    else:
        return None


if __name__ == "__main__":
    main()
