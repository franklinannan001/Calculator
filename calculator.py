def main():
    operation = input("Operation: ").strip()


def addition(o):
    x, y = o.split("+")
    return x + y


def subtraction(o):
    x, y = o.split("-")
    return x - y


def multiplication(o):
    x, y = o.split("*")
    return x * y


def division(o):
    x, y = o.split("/")
    return x / y


if __name__ == "__main__":
    main()