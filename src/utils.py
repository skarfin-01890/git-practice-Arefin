def add(a, b):
    try:
        return a + b
    except TypeError:
        return "Error: Please enter numbers only"


def subtract(a, b):
    try:
        return a - b
    except TypeError:
        return "Error: Please enter numbers only"


def multiply(a, b):
    try:
        return a * b
    except TypeError:
        return "Error: Please enter numbers only"