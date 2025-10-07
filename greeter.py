# greeter.py
import sys

def greet(name: str, caps: bool = False) -> str:
    if caps:
        name = name.upper()
    return f"Hello, {name}"

if __name__ == "__main__":
    # Very tiny "parser": if user types --caps anywhere, turn it on
    caps = "--caps" in sys.argv
    name = input("Your name (--caps optional): ")
    print(greet(name, caps=caps))

