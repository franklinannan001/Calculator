# CLI Calculator

A lightweight, interactive command-line calculator built in Python that evaluates basic and exponential arithmetic expressions using regular expressions.

## Features

* **Supported Operations:** Addition (`+`), subtraction (`-`), multiplication (`*`), division (`/`), exponentiation (`**`), and modulus (`%`).
* **Flexible Input Parsing:** Uses regular expressions to parse equations with or without spaces (e.g., `5+5` or `5 + 5`).
* **Error Handling:** Gracefully handles division by zero, malformed equations, and invalid inputs without crashing.
* **Clean Exit:** Supports exiting smoothly via `Ctrl+C` (`KeyboardInterrupt`).

## Prerequisites

* Python 3.8 or higher (uses the walrus operator `:=` introduced in Python 3.8).
* No external third-party libraries required (uses only Python's built-in `sys` and `re` modules).

## Installation & Usage

1. **Clone the repository** (or download the script):
   ```bash
   git clone https://github.com
   cd your-repo-name
   ```

2. **Run the calculator:**
   ```bash
   python calculator.py
   ```
   *(Replace `calculator.py` with your actual filename if different.)*

3. **Enter equations at the prompt:**
   Type an expression containing two positive integers separated by a valid operator and press **Enter**.

4. **Exit the program:**
   Press `Ctrl + C` at any time to exit cleanly.

## Example Session

```text
=~=~=~=~=~ CALCULATOR ~=~=~=~=~=
>>> 12 + 8
Sum: 20
>>> 15 / 4
Quotient: 3.75
>>> 2 ** 5
Exponential: 32
>>> 10 % 3
Modulus: 1
>>> 10 / 0
Cannot divide by zero
>>> hello
hello is not a valid equation
>>> ^C
=~=~=~=~=~ Thank you for visiting ~=~=~=~=~=
```


## Limitations

* Currently supports **non-negative integers** only (`0-9`). Negative numbers and floating-point (decimal) inputs are not yet supported.
* Evaluates two operands at a time (`x <operator> y`).
