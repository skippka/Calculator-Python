def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y !=0:
        return x / y
    else:
        return "Error"

def main():
    print("Welcome to the calculator!")
    x = float(input("Enter the first number: "))
    y = float(input("Enter the second: "))
    operation = input("Enter the operation (+, -, *, /): ")

    if operation == "+":
        print(f"Result: {add(x, y)}")

    elif operation == "-":
        print(f"Result: {subtract(x, y)}")

    elif operation == "*":
        print(f"Result: {multiply(x, y)}")

    elif operation == "/":
        print(f"Result: {divide(x, y)}")
    else:
        print("Invalid operation!")



if __name__ == "__main__":
    main()